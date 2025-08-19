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

    print(agora)
    print(uso_cpu)
    print(uso_ram.percent)
    print(uso_disco.percent)

    dados_cpu_ram_disco = {
        "timestamp": agora,
        "cpu": uso_cpu,
        "ram": uso_ram.percent,
        "disco": uso_disco.percent
    }


    df = pandas.DataFrame([dados_cpu_ram_disco])

    #Estrutura condicional necessaria para evitar renomear o cabeçalho e permitir a inserção de novas linhas com o "mode = a"
    if not os.path.isfile("dados-servidor.csv"):
        df.to_csv("dados-servidor.csv", encoding="utf-8", index=False)

    else:
        df.to_csv("dados-servidor.csv", encoding="utf-8", mode="a", index=False, header=False)
    
    time.sleep(10)