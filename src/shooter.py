# Aca voy a definir las funciones que se encargan de procesar los datos de las rondas 
# y calcular el ranking de los jugadores.

# Esta función se encarga de calcular el puntaje de un jugador en base a sus kills, assists y muertes.
# Los kills valen 3 puntos, las assists 1 punto y cada muerte resta 1 punto.
def calcular_puntaje(kills, assists, deaths):
    puntos = kills * 3 + assists * 1
    if deaths:
        puntos -= 1
    return puntos

# Esta función se encarga de actualizar el estado general de cada jugador
# en base a los datos de la ronda actual.
def actualizar_estadisticas(ronda, estadisticas, mvp_name):
    for jugador, datos in ronda.items():
        # Actualizamos las estadisticas del jugador
        # sumando las kills, assists y deaths de la ronda actual.
        estadisticas[jugador]['kills'] += datos['kills']
        estadisticas[jugador]['assists'] += datos['assists']
        estadisticas[jugador]['deaths'] += 1 if datos['deaths'] else 0
        # Mando a calcular el puntaje del jugador
        # y lo sumo a los puntos totales del jugador.
        puntos = calcular_puntaje(datos['kills'], datos['assists'], datos['deaths'])
        estadisticas[jugador]['puntos'] += puntos
        # Si el jugador es el MVP de la ronda, le sumo 1 a su contador de mvps.
        if jugador == mvp_name:
            estadisticas[jugador]['mvps'] += 1

# Busco el MVP de la ronda
# en base a los puntos obtenidos por cada jugador.
def determinar_mvp(ronda):
    # Inicializo el MVP con un puntaje muy bajo
    # y un nombre vacio.
    max_puntos = float('-inf')
    mvp_name = ""
    for jugador, datos in ronda.items():
        puntos = calcular_puntaje(datos['kills'], datos['assists'], datos['deaths'])
        # Formato de calculo de maximos de siempre
        if puntos > max_puntos:
            max_puntos = puntos
            mvp_name = jugador
    return mvp_name

# Esta función se encarga de mostrar el ranking de los jugadores
# en base a sus puntos totales.
def mostrar_ranking(estadisticas, ronda_actual):
    print(f"\nRanking ronda {ronda_actual}:")
    print("Jugador     Kills  Asists  Muertes  MVPs  Puntos")
    print("-" * 50)
    # Ordeno de mayor a menor los jugadores en base a sus puntos
    # y los muestro en pantalla.
    ranking = sorted(estadisticas.items(), key=lambda item: item[1]['puntos'], reverse=True)
    for nombre, stats in ranking:
        print(f"{nombre:<12}{stats['kills']:<7}{stats['assists']:<8}{stats['deaths']:<9}{stats['mvps']:<6}{stats['puntos']}")