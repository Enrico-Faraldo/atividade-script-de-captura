import time
import psutil
import pandas
import datetime
import os

while True:
    uso_cpu = psutil.cpu_percent(10, percpu=False)
    uso_ram = psutil.virtual_memory()
    uso_disco = psutil.disk_usage("/")
    agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nome_usuario = "Enrico"

    for p in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        pass  

    time.sleep(1)
    processos = []
    for p in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        info = p.info
        info["timestamp"] = agora
        processos.append(info)

    print("nome do usuário: " + nome_usuario)
    print("agora: " + agora)
    print("uso de cpu (%): ", uso_cpu)
    print("uso de ram (%): ", uso_ram.percent)
    print("uso de disco (%): ", uso_disco.percent)
    print("processos: ", processos)
    print("\n")

    dados_cpu_ram_disco = {
        "nome de usuario": nome_usuario,
        "timestamp": agora,
        "cpu": uso_cpu,
        "ram": uso_ram.percent,
        "disco": uso_disco.percent
    }

    

    df_componentes_fisicos = pandas.DataFrame([dados_cpu_ram_disco])
    df_processos = pandas.DataFrame(processos, columns=['pid', 'name', 'cpu_percent', 'timestamp'])



    #df_processos.reset_index(inplace=True)
    #df_processos.rename(columns={"index": "pid"}, inplace=True)

    #Estrutura condicional necessaria para evitar renomear o cabeçalho e permitir a inserção de novas linhas com o "mode = a"
    if not os.path.isfile("dados-servidor.csv"):
        df_componentes_fisicos.to_csv("dados-servidor.csv", encoding="utf-8", index=False, sep=";")

    else:
        df_componentes_fisicos.to_csv("dados-servidor.csv", encoding="utf-8", mode="a", index=False, header=False, sep=";")

    if not os.path.isfile("dados-processos.csv"):
        df_processos.to_csv("dados-processos.csv", encoding="utf-8", index=False, sep=";")

    else:
        df_processos.to_csv("dados-processos.csv", encoding="utf-8", mode="a", index=False, header=False, sep=";")
    
    time.sleep(10)