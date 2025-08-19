import pandas as pd
import datetime

while True:
    print("O que deseja fazer? \n")
    print("Digite 1 para Exibir o uso médio da RAM na última hora \n")
    print("Digite 2 para Exibir o pico de CPU nas últimas 2 horas \n")
    print("Digite 3 para Exibir o uso médio de disco nos últimos n minutos (n é escolhido pelo usuário) \n")
    opcao = input()

    if opcao == "1":
        df = pd.read_csv("dados-servidor.csv")

        df["timestamp"] = pd.to_datetime(df["timestamp"])

        agora = datetime.datetime.now()
        ultima_hora = agora - datetime.timedelta(hours = 1)
        ultima_hora_ram = df[df["timestamp"] >= ultima_hora]

        print("\n" * 5)
        print(ultima_hora_ram["ram"].mean())

    elif opcao == "2":
        df = pd.read_csv("dados-servidor.csv")

        df["timestamp"] = pd.to_datetime(df["timestamp"])

        agora = datetime.datetime.now()
        ultimas_horas = agora - datetime.timedelta(hours = 2)
        ultima_horas_cpu = df[(df["timestamp"] >= ultimas_horas)]

        print("\n" * 5)
        print(ultima_horas_cpu["cpu"].max())

    elif opcao == "3":
        input_ultimos_minutos = int(input("\n Digite Quantos minutos: "))
        df = pd.read_csv("dados-servidor.csv")

        df["timestamp"] = pd.to_datetime(df["timestamp"])

        agora = datetime.datetime.now()
        ultimos_minutos = agora - datetime.timedelta(minutes = input_ultimos_minutos)
        ultimos_minutos_disco = df[(df["timestamp"] >= ultimos_minutos)]

        print("\n" * 5)
        print(ultimos_minutos_disco["disco"].mean())
        
    else:
        print("digite 1, 2 ou 3 \n")
