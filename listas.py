valor = []

for c in range(0, 5):
    a = int(input(f'digite o {c+1}° valor: '))
    valor.append(a)
print(max(valor))
print(min(valor))
