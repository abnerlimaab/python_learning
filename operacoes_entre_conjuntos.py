#Este programa realiza operações entre dois conjuntos utilizando as operações estudadas na Aula 6 do curso de introdução à programação em Python na Digital Inovation One

print('Operações básicas entre dois conjuntos...' + '\n')

conjA = {1, 2, 3, 4, 5}
print('Conjunto A: {}'.format(conjA))
conjB = {1, 3, 5}
print('Conjunto B: {}'.format(conjB) + '\n')

uniao = conjA.union(conjB)
print('União: {}'.format(uniao))

interseccao = conjA.intersection(conjB)
print('Intersecção: {}'.format(interseccao))

diferencaAB = conjA.difference(conjB)
if diferencaAB:
    print('Diferença de A em B: {}'.format(diferencaAB))
else:
    print('O conjunto diferença de A em B é vazio.')

diferencaBA = conjB.difference(conjA)
if diferencaBA:
    print('Diferença de B em A: {}'.format(diferencaBA))
else:
    print('O conjunto diferença de B em A é vazio.')

difsimetric = conjA.symmetric_difference(conjB)
print('Diferença simétrica: {}'.format(difsimetric))

pertinencia = True
if conjA.issubset(conjB):
    print('O conjunto A pertence a B')
elif conjB.issubset(conjA):
    print('O conjunto B pertence a A')
else:
    print('Não há relação de pertinência entre os conjuntos.')
