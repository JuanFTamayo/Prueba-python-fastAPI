from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import sqlite3
import requests


app= FastAPI()

class Nombres(BaseModel):
    nombre:str
    nombre2:str

class Winner(BaseModel):
    winner:str

async def getStats(nombre):
    url= f"https://pokeapi.co/api/v2/pokemon/{nombre}"
    res=requests.get(url)
    if res.status_code!=200:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    data=res.json()
    stats=data['stats']
    lista={}
    lista['name']=nombre
    for stat in stats:
        stat_name=stat['stat']['name']
        base_stat=stat['base_stat']
        if stat_name=='hp':
            lista[stat_name]=base_stat
        if stat_name=='speed':
            lista[stat_name]=base_stat
        if stat_name=='attack':
            lista[stat_name]=base_stat
        if stat_name=='defense':
            lista[stat_name]=base_stat
    return lista

async def getWinner(nombre,nombre2):
    poke1= await getStats(nombre)
    poke2= await getStats(nombre2)
    if poke1['speed']>poke2['speed']:
        attacker=poke1
        defender=poke2
    else:
        attacker=poke2
        defender=poke1
    while poke1['hp']>0 and poke2['hp']>0:
        
        damage= max(attacker['attack']- defender['defense'],0)

        defender['hp']-=damage

        attacker,defender=defender,attacker

    if poke1['hp']<=0:
        winner=poke2['name']
    else:
        winner=poke1['name']
    return winner

def saveBattle(winner,nombre,nombre2):
    con = sqlite3.connect("tutorial.db")
    c = con.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS battle(winner TEXT, nombre TEXT, nombre2 TEXT)")
    c.execute(" INSERT INTO battle(winner, nombre, nombre2) VALUES(?,?,?)",(winner,nombre,nombre2))
    con.commit()
    con.close()
    
def battleExist(nombre,nombre2):
    con = sqlite3.connect("tutorial.db")
    c = con.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS battle(winner TEXT, nombre TEXT, nombre2 TEXT)")
    c.execute("SELECT winner FROM battle WHERE(nombre=? AND nombre2=?) OR (nombre=? AND nombre2=?) ",(nombre,nombre2,nombre2,nombre))
    result=c.fetchone()
    con.close()

    if result:
        return result[0]
    else:
        return None


@app.post("/url",response_model=Winner,status_code=201)
async def url(request:Nombres):
    try:
        if battleExist(request.nombre,request.nombre2):
            winner=battleExist(request.nombre,request.nombre2)
            return Winner(winner=winner)
        else:
            winner= await getWinner(request.nombre,request.nombre2)
            saveBattle(winner,request.nombre,request.nombre2)
            return Winner(winner=winner)
    except HTTPException as http:
        raise http

    # except Exception as e:
    #     raise HTTPException(status_code=500,detail=str(e))
    

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)