faturamento_estado = {
    'SP' : 67836.43,
    'RJ' : 36678.66,
    'MG' : 29229.88,
    'ES' : 27165.48,
    'Outros' : 19849.53
}

faturamento_total = sum(faturamento_estado.values())

percentual_estado = {}
for estado, faturamento_estado in faturamento_estado.items():
    percentual = (faturamento_estado / faturamento_total) *100
    percentual_estado[estado] = percentual
    
print(f"Percentual por estado: ")
for estado, percentual in percentual_estado.items():
    print(f"{estado}: {percentual:.2f}%")