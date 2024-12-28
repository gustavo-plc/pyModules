#DEFINIÇÃO DAS FUNÇÕES

def fatorial(n):
    i = 1
    for c in range(1, n + 1):
        i *= c
    return i

def dobro(n):
    return 2 * n

def triplo(n):
    return 3 * n