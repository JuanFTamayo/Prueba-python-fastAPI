# Prueba-python-fastAPI

### Instalar FastAPI [FastAPI](https://fastapi.tiangolo.com/es/tutorial/ "FastAPI")

#### Para probar el endpoint ejecutar e ir a localhost/docs en el navegador --> http://127.0.0.1:8000/docs

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

