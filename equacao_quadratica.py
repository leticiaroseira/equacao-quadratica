import math

a = float(input('Insira o valor de a: '))
b = float(input('Insira o valor de b: '))
c = float(input('Insira o valor de c: '))

delta = b ** 2 - 4 * a * c

if delta > 0:
    print(f'Delta é igual a {delta}, sendo um valor maior que 0. Portanto, há duas raízes reais para delta.')
elif delta == 0:
    print(f'Delta é igual {delta}, sendo um valor igual a 0. Portanto, há uma raiz real para delta.')
else:
    print(f'Delta é igual a {delta}, sendo um valor menor que 0. Portanto, não há raiz real para delta.')

if delta >= 0:
    print('A raiz quadrada de delta é: ', math.sqrt(delta))
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f'O valor da raiz 1 é: ', raiz1, 'e o valor da raiz 2 é: ', raiz2)