#calculadora em python
def calculadora():
    operacao = input('''

Digite a operação matemática que você deseja concluir:
+ para adicao
- para subtracao
* para multiplicacao
/ para divisiao
''')


numero1 = int(input("digite seu primeiro numero: ")) #entrada de dados
numero2 = int(input("digite seu segundo numerp: ")) #entrada de dados

#adição
if operacao == '+':
print('{} + {} = '.format(numero1, numero2))  #formatadores de string
print (numero1 + numero2) #mostra a soma dos numeros

#subtração
elif operacao == '-':
print('{} - {} = '.format(numero1, numero2))  #formatadores de string
print (numero1 - numero2) #mostra a subtração dos numeros

#multiplicação
elif operacao == '*':
print('{} * {} = '.format(numero1, numero2))  #formatadores de string
print (numero1 * numero2)#mostra a multiplicação

#mostra a divisão
elif operacao == '/':
print('{} / {} = '.format(numero1, numero2))  #formatadores de string
print (numero1 / numero2)

else:
    print ('Você não digitou um operador válido, execute o programa novamente.
')
           
           
           def novamente():
            calc_novamente = input('''

Deseja calcular novamente?
Digite S para SIM ou N para NÃO.

''')

    if calc_novamente.upper() == 'Y':
        calculate()
    elif calc_novamente.upper() == 'N':
        print('ok')
    else:
        novamente()
           
           calculadora ()
