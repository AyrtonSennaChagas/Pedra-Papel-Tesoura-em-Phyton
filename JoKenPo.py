import random
a = ["tesoura", "papel", "pedra"]
print("bem vindo ao jogo pedra, papel ou tesoura")
print("digite abaixo: pedra, papel ou tesoura")
humano = input()
# print(humano)

numero_aleatorio = random.randint(0, 2)
maquina = a[numero_aleatorio]
print(a[numero_aleatorio])
    
if maquina == humano: print("declarado empate")

if maquina=="papel" and humano=="pedra":
    print("maquina ganhou!")

if maquina=="pedra" and humano=="tesoura":
    print("maquina ganhou!")
    
if maquina=="tesoura" and humano=="papel":
    print("maquina ganhou!")
    
#cenário onde usuário ganha:
    
if maquina=="pedra" and humano=="papel":
    print("humano ganhou!")

if maquina=="papel" and humano=="tesoura":
    print("humano ganhou!")
    
if maquina=="tesoura" and humano=="pedra":
    print("humano ganhou!")
    
    