#Desenvolva um programa para calcular e mostrar o desconto no valor de uma compra (fornecido pelo usuário)
valorCompra = float(input('Digite o valor do produto: '))
if valorCompra <=1000:
    des = valorCompra * (10/100)
    novValor = valorCompra - des
    print('O valor da compra foi: {:.1f}'.format(novValor))
    print('O desconto foi: {:.1f}' .format(des))
elif valorCompra >= 1001 or valorCompra <=5000:
    des = valorCompra *(20/100)
    novValor = valorCompra - des
    print('O valor da compra foi: {:.1f}'.format(novValor))
    print('O desconto foi: {:.1f}'.format(des))
elif valorCompra > 5000:
    des = valorCompra * (30/100)
    novValor = valorCompra - des
    print('O valor da compra foi: {:.1f}'.format(novValor))
    print('O desconto foi: {:.1f}'.format(des))
