import time
import psutil
import pandas
import datetime

while True:
    usoCpu = psutil.cpu_percent(10, percpu=False)
    usoRam = psutil.virtual_memory()
    usoDisco = psutil.disk_usage("/")
    agora = datetime.datetime.now().timestamp()

    print(usoCpu)
    print(usoRam.percent)
    print(usoDisco.percent)
    print(agora)

    dadosCpuRamDisco = {
        "timestamp": agora,
        "cpu": usoCpu,
        "ram": usoRam.percent,
        "disco": usoDisco.percent
    }

    dataFrame = pandas.DataFrame(dadosCpuRamDisco)
    dataFrame.to_csv("dados-servidor.csv", encodings="utf-8", index=False)

    time.sleep(10)