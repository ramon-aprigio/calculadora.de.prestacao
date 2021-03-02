#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.


casa = float(input('Olá, qual será o valor da casa: R$ '))
salario = float(input('Qual o valor do seu salário: R$ '))
anos = int(input('Em quantos anos você pretender pagar: '))
minimo = salario * 30/100
mensal = casa /(anos * 12)

print('Para comprar uma casa de R${:.2f}, você deverá pagar R${:.2f} por mês durante {} anos.'.format(casa,mensal,anos))

if mensal <=minimo:
    print('Parabéns pela compra da sua nova casa!!!')
else:
    print('Desculpe. O empréstimo não pôde ser autorizado. Salário ou prazo insuficiente')









