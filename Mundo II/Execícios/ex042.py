r1 = float(input('Valor da primeira reta: '))
r2 = float(input('Valor da segunda reta: '))
r3 = float(input('Valor da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas retas PODEM formar um triângulo!')
    if r1 == r2 == r3:
        print('Essas retas formam um triângulo Equilátero!')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('Essas retas formam um triângulo Isóceles!')
    else:
        print('Essas retas formam um triângulo Escaleno!')
else:
    print('Essas retas NÃO podem formar um triângulo!')
