n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

m = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, m))
if m < 5.0:
    print('ALUNO REPROVADO!')
elif m < 7 or m >= 5.0:
    print('ALUNO EM RECUPERAÇÃO!')
elif m >= 7.0:
    print('ALUNO APROVADO!')