def contar_palabra(palabra, vector, contador=0):
    if not vector:
        return contador
    else:
        if vector[0] == palabra:
            contador += 1
        return contar_palabra(palabra, vector[1:], contador)

vectordepalabras = ["fútbol", "remera", "equipo", "partido", "fútbol", "fútbol"]
palabrabuscada = "fútbol"

resultado = contar_palabra(palabrabuscada, vectordepalabras)
print(f"La palabra '{palabrabuscada}' aparece {resultado} veces en el vector.")