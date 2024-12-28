def fatorial(n):
    i = 1
    for c in range(1, n + 1):
        i *= c
    return i


num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')