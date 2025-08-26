#servidor = cpu, memória, ram
#processos = processos
df_processos <- dados.processos
df_servidor <- dados.servidor

#vendo os dados mais recentes do servidor
tail(df_servidor, n = 10)

#média ram todo período (pouco útil)
mean(df_servidor$ram[df_servidor$ram!=0])
mean(df_servidor$ram[df_servidor$ram>=55])

#média cpu todo período (pouco útil)
mean(df_servidor$cpu[df_servidor$cpu!=0])
mean(df_servidor$cpu[df_servidor$cpu>=1])

#média disco todo período (pouco útil)
mean(df_servidor$disco[df_servidor$disco!=0])
mean(df_servidor$disco[df_servidor$disco>=90])

#adicionando colunas de alerta
df_servidor$alerta_disco <- df_servidor$disco > 90
df_servidor$alerta_ram <- df_servidor$ram > 60
df_servidor$alerta_cpu <- df_servidor$cpu > 10
df_processos$alerta_processo <- df_processos$cpu_percent >= 100


#mediana (melhor que a média)
median(df_servidor$cpu)
median(df_servidor$ram)
median(df_servidor$disco)

#exibindo sem processos não problemáticos: 0%
df_processos <- df_processos$cpu_percent != 0
df_processos[df_processos$cpu_percent != 0, ]
mean(df_processos$cpu_percent != 0)

#histogramas
hist(df_processos$cpu_percent[df_processos$cpu_percent >= 1],
     main = "Histograma de porcentagem de cpu a partir de 1%
     por processo durante todo o período (todos os núcleos lógicos)",
     xlab = "uso de cpu %",
     ylab = "frequência")

hist(df_processos$cpu_percent[df_processos$cpu_percent >= 100],
     main = "Histograma de porcentagem de cpu a partir de 100%
     por processo durante todo o período (todos os núcleos lógicos)",
     xlab = "uso de cpu %",
     ylab = "frequência")

hist(df_servidor$cpu[df_servidor$cpu >= 0],
     main = "Histograma de porcentagem de cpu a partir de 1%
     durante todo o período",
     xlab = "uso de cpu %",
     ylab = "frequência")

hist(df_servidor$cpu[df_servidor$alerta_cpu == TRUE],
     main = "Histograma de porcentagem de cpus alertas
     durante todo o período",
     xlab = "uso de cpu %",
     ylab = "frequência")

hist(df_servidor$ram[df_servidor$alerta_ram == TRUE],
     main = "Histograma de porcentagem de ram alertas
     durante todo o período",
     xlab = "uso de ram",
     ylab = "frequência")

hist(df_servidor$disco[df_servidor$alerta_disco == TRUE],
     main = "Histograma de porcentagem de ram alertas
     durante todo o período",
     xlab = "uso de disco",
     ylab = "frequência")

hist(df_servidor$ram[df_servidor$ram >= 0],
     main = "Histograma de porcentagem de ram
     durante todo o período",
     xlab = "uso de ram",
     ylab = "frequência")

hist(df_servidor$disco[df_servidor$disco >= 0],
     main = "Histograma de porcentagem de disco
     durante todo o período",
     xlab = "uso de disco",
     ylab = "frequência")

# número de alertas. Função sum: true = 1, false = 0
sum(df_processos$alerta_processo)
sum(df_servidor$alerta_cpu)
sum(df_servidor$alerta_ram)
sum(df_servidor$alerta_disco)

# número de não alertas
sum(df_processos$alerta_processo == FALSE)
sum(df_servidor$alerta_cpu == FALSE)
sum(df_servidor$alerta_ram == FALSE)
sum(df_servidor$alerta_disco == FALSE)
