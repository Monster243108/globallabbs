a = int(input('Primeiro bimestre: '))
while a > 10:
    a = int(input('Você digitou errado. Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
while b > 10:
    b = int(input('Você digitou errado. Segundo bimestre:'))
c = int(input('Terceiro bimestre: '))
while c > 10:
    c = int(input('Você digitou errado. Terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
while d > 10:
    d = int(input('Você digitou errado. Quarto bimestre'))
media = (a + b + c + d) / 4
print('media: {}'.format(media))


# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('media: {}' .format(media))
# else:
#     print('foi informado alguma nota errada')
#
# a = int(input('Primeiro Valor:'))
# b = int(input('Segundo Valor: '))
# c = int(input('Terceiro Valor'))
# if a > b and a < c:
#     print('o maior valor é {}' .format(a))
# elif b > a and b > c:
#     print('o maior número é {}' .format (b))
# else:
#     print('o maior número é {}'.format(c))
# print('final do programa')