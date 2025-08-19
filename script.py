import time
import psutil
import pandas
import datetime

primeiraVez = True
while True:
    usoCpu = psutil.cpu_percent(10, percpu=False)
    usoRam = psutil.virtual_memory()
    usoDisco = psutil.disk_usage("/")
    agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(agora)
    print(usoCpu)
    print(usoRam.percent)
    print(usoDisco.percent)

    dadosCpuRamDisco = {
        "timestamp": agora,
        "cpu": usoCpu,
        "ram": usoRam.percent,
        "disco": usoDisco.percent
    }


    dataFrame = pandas.DataFrame([dadosCpuRamDisco])

    #Estrutura condicional necessaria para evitar renomear o cabeçalho e permitir a inserção de novas linhas com o "mode = a"
    if primeiraVez:
        dataFrame.to_csv("dados-servidor.csv", encoding="utf-8", index=False)

    else:
        dataFrame.to_csv("dados-servidor.csv", encoding="utf-8", mode="a", index=False, header=False)
    
    primeiraVez = False
    time.sleep(10)