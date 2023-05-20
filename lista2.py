lista = []
valores_ordenados = []
c = 0
pos = 0
while True:
    a = str(input(f'digite o {c+1}° valor ou sair: \n-->'))
    if a == 'sair':
        break
    else:
        lista.append(int(a))
    c += 1

for x in range(0, len(lista)):
    for i in range(0, len(lista)):
        if lista[x] < lista[i]:
            pos += 1
        else:
            break
    valores_ordenados.insert(pos, lista[x])
    pos = 0

print(len(lista))
print(valores_ordenados)
cincos = lista.count(5)
print(f'exiten {cincos} numeros 5')
