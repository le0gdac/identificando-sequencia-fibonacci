n = int(input('Digite o número desejado: '))
a, b = 0, 1;

while a < n:
    a, b = b, a + b

if a == n:
    print('O número indicado pertence a sequência.')
if a != n:
    print('O número indicado não pertence a sequência.')