# DESAFIO 86 - Guanabara

# crie um programa de uma matriz dimensional 3x3
# ... e preencha os valores lidos pelo teclado
# no final mostre a matriz na tela com formatação correta

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz [l][c] = int(input(f'digite um valor para [l, c]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz [l] [c]:^5}]', end='')
    print()