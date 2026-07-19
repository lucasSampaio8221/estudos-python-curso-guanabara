#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.

times = ("Corinthians", "Palmeiras", "Santos", "Grêmio", "Cruzeiro", "Flamengo", "Vasco", "Chapecoense", "Atlético",
         "Botafogo", "Atlético-PR", "Bahia", "São Paulo", "Fluminense", "Sport Recife", "EC Vitória", "Coritiba",
        "Avaí", "Ponte Preta", "Atletico-GO")

print("-=" *15)
print(f"Lista de time do Brasileirão: {times}")
print("-=" *15)
print(f"Os 5 primeiros são {times[0:5]}")
print("-=" *15)
print(f"Os 4 últimos são {times[-4:]}")
print("-=" *15)
print(f"Os times em ordem alfabetica: {sorted(times)}")
print("-=" *15)
print(f"A chapecoense está na posição {times.index("Chapecoense")+1}")