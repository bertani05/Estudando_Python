produto = ('lapis', 1.75, 'borracha', 2.00, 'caderno', 15.90)
for c in range(0, len(produto), 2):
    print(produto[c], end= '')
    print(5*'.', end= '')
    print(f'R${produto[c+1]}')
