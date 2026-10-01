import random

# 10 estaciones de Puntarenas
#  temperatura base, humedad base, presion base
estaciones = {
    "Puntarenas": [28, 85, 1012],
    "Caldera": [28, 84, 1012],
    "Jaco": [27, 86, 1011],
    "Quepos": [27, 88, 1011],
    "Dominical": [27, 87, 1011],
    "Paquera": [28, 84, 1012],
    "Tambor": [27, 85, 1012],
    "Montezuma": [27, 86, 1011],
    "Golfito": [27, 88, 1011],
    "Puerto Jimenez": [27, 87, 1011]
}

dias = ["Lunes", "Martes", "Miercoles", "Jueves",
        "Viernes", "Sabado", "Domingo"]

datos = []


def generar_datos():
    for zona in estaciones:
        temp_base = estaciones[zona][0]
        humedad_base = estaciones[zona][1]
        presion_base = estaciones[zona][2]

        for dia in dias:
            # uno cada 10 minutos
            for numero in range(144):
                hora = numero // 6
                minuto = (numero % 6) * 10

                if 10 <= hora <= 16:
                    temperatura = random.uniform(temp_base, temp_base + 6)
                else:
                    temperatura = random.uniform(temp_base - 4, temp_base + 2)

                humedad = random.uniform(humedad_base - 5, humedad_base + 8)
                presion = random.uniform(presion_base - 2, presion_base + 2)

                lectura = {
                    "zona": zona,
                    "dia": dia,
                    "hora": f"{hora:02d}:{minuto:02d}",
                    "temperatura": round(temperatura, 1),
                    "humedad": round(min(99, humedad), 1),
                    "presion": round(presion, 1)
                }

                datos.append(lectura)


# Consulta 1 (lo cambie porque use el for xd
def temperatura_por_zona():
    zona = input("Digite la zona: ")

    if zona not in estaciones:
        print("Zona no encontrada.")
        return

    zona_datos = list(filter(
        lambda x: x["zona"] == zona,
        datos
    ))

    def promedio_hora(hora):
        texto_hora = f"{hora:02d}:"

        lecturas = list(filter(
            lambda x: x["hora"].startswith(texto_hora),
            zona_datos
        ))

        temperaturas = list(map(
            lambda x: x["temperatura"],
            lecturas
        ))

        promedio = sum(temperaturas) / len(temperaturas)

        return f"{hora:02d}:00 -> {promedio:.1f} °C"

    resultados = list(map(promedio_hora, range(24)))

    print("\n".join(resultados))


#2
# Consulta 2
def dia_mas_caluroso():

    def buscar_mayor(zona):
        zona_datos = list(filter(
            lambda x: x["zona"] == zona,
            datos
        ))

        mayor = max(
            zona_datos,
            key=lambda x: x["temperatura"]
        )

        return (
            zona + " - " +
            mayor["dia"] + " " +
            mayor["hora"] + " - " +
            str(mayor["temperatura"]) + " °C"
        )

    resultados = list(map(buscar_mayor, estaciones))

    print("\n".join(resultados))


# 3
# Consulta 3
def fluctuacion_presion():
    dia = input("Digite el dia: ").capitalize()

    if dia not in dias:
        print("Dia no valido.")
        return

    def calcular_presion(zona):
        lecturas = list(filter(
            lambda x: x["zona"] == zona and x["dia"] == dia,
            datos
        ))

        presiones = list(map(
            lambda x: x["presion"],
            lecturas
        ))

        minima = min(presiones)
        maxima = max(presiones)
        diferencia = maxima - minima

        return (
            zona +
            " - Min: " + str(minima) +
            " Max: " + str(maxima) +
            " Fluctuacion: " + str(round(diferencia, 1)) +
            " hPa"
        )

    resultados = list(map(calcular_presion, estaciones))

    print("\n".join(resultados))


# 4
def buscar_bochorno():

    alertas = list(filter(
        lambda x: x["temperatura"] > 32 and x["humedad"] > 80,
        datos
    ))

    alertas = sorted(
        alertas,
        key=lambda x: x["temperatura"],
        reverse=True
    )

    if len(alertas) == 0:
        print("No se encontraron alertas.")
        return

    def mostrar_alerta(alerta):
        return (
            alerta["zona"] + " - " +
            alerta["dia"] + " " +
            alerta["hora"] +
            " - Temp: " + str(alerta["temperatura"]) + " °C" +
            " - Humedad: " + str(alerta["humedad"]) + " %"
        )

    resultados = list(map(mostrar_alerta, alertas))

    print("\n".join(resultados))

# 1

generar_datos()

print("Datos generados:", len(datos))

opcion = ""

while opcion != "0":
    print("\n--- ESTACION METEOROLOGICA ---")
    print("1. Temperatura esperada por zona")
    print("2. Dia y hora mas calurosos")
    print("3. Fluctuacion de presion")
    print("4. Alertas de bochorno")
    print("0. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        temperatura_por_zona()
    elif opcion == "2":
        dia_mas_caluroso()
    elif opcion == "3":
        fluctuacion_presion()
    elif opcion == "4":
        buscar_bochorno()
    elif opcion == "0":
        print("Programa finalizado.")
    else:
        print("Opcion no valida.")
