# Prueba tecnica python fastAPI

### Instalar FastAPI [FastAPI](https://fastapi.tiangolo.com/es/tutorial/ "FastAPI")

#### Para probar el endpoint ejecutar en terminal: uvicorn prueba-fastapi:app --reload

Luego ir a localhost/docs en el navegador --> http://127.0.0.1:8000/docs

### Enunciado

Se requiere hacer un servicio web que tenga un endpoint para simular una batalla Pokémon. Para esto
u;lizaremos la API publica de Pokemon que nos permi;rá obtener los datos. La idea es que el servicio
retorne al ganador de la batalla, sin embargo. Para que en el caso de que alguien solicite simular de
nuevo una batalla, no tengamos que simularla vamos a almacenar en una base de datos los resultados
de quien gana entre un Pokémon y otro, para así retornar el ganador.
Para lograr esto debemos tener cuenta lo siguiente:
1. Crear un servicio WEB que tenga un endpoint POST /pokemon-baNle que reciba lo siguiente:
{
“nombre-pokemon-1”:”xxxx”,
“nombre-pokemon-2”:”xxxx”
}
2. Controlar los errores que puedan surgir durante el proceso y traducirlos a errores HTTP.
3. Crear una tabla para almacenar los resultados de las batallas.
4. Validar si existe en la BD una batalla entre esos dos Pokémones. Sino la debe simular.
5. Simular una batalla Pokemon en función del atributo stats que retorna el API de Pokemón. En
este caso necesitamos los siguientes stats dentro de la respuesta:

a. hp: Puntos de salud

b. speed: Velocidad para atacar primero que otro

c. aNack: Puntos de ataque

d. defense: Puntos de defensa

La batalla se debe realizar por turnos y comienza primero el Pokémon que tenga más velocidad.
En cada turno el Pokémon atacante resta del defensor los puntos de salud en una can;dad de:
puntos de ataque del atacante menos los puntos de defensa del defensor. Gana el Pokémon que
primero lleve a cero el otro.
7. Almacenar en una base de datos el resultado para que en un próximo request busque si ya tengo
un resultado de dicha batalla y así poder retornar.

## Como se veria
![fapi 1](https://github.com/JuanFTamayo/Prueba-python-fastAPI/assets/88947668/44a18415-4eae-4e9a-8e39-842fc7f7fc99)
### Probando el endpoint pikachu vs bulbasaur(mirar responses/server response)
![fapi 2](https://github.com/JuanFTamayo/Prueba-python-fastAPI/assets/88947668/c3ce4303-0a4f-45b8-9d9f-56f42c153447)
### Probando con datos erroneos(mirar responses/server response)
![fapi 3](https://github.com/JuanFTamayo/Prueba-python-fastAPI/assets/88947668/fdae33a8-8d0d-4afc-af9e-f13265d7eb61)

