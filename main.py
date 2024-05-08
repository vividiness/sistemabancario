import os

#saques armazenados em um variável e exibidos na operação

#menu do projeto
menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[x] Sair

=>
'''

#limpar o terminal
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')


#variáveis globais
saldo = 0
limite = 500
LIMITE_SAQUES = 3
num_saques = 0
extrato = []

while True:
    op = input(menu).lower()

    if op == 'd':
        #Depósito
        x = float(input('Digite quanto deseja depositar  \n=>'))
        
        while x > 500:
            print('Valor acima do permitido. Digite outro valor.')
            x = float(input('Digite quanto deseja depositar \n=>'))

        saldo+=x
        print('Saldo depositado!')
            
    elif op == 's':
        #Saque
        y = float(input('Digite o valor que deseja sacar \n=>' ))

        #TODO consertar erro
        while True:
            if y>saldo:
                print('Saque inválido! Valor maior que o saldo.')
                

            elif y>limite:
                print(f'Valor acima do permitido.  Digite um valor abaixo de R$ {limite}')
                

            elif num_saques > LIMITE_SAQUES:
                print('Limite de saques diários atingidos.')
                break

        num_saques+=1
        saldo-=y
        extrato += str(y)+', '
        print('Valor sacado!')

    elif op == 'e':
        #Extrato
        print(f'Saldo: {saldo} \nTodos os extratos: {extrato}')

    elif op == 'x':
        print('See you soon!')
        break
    else:
        print('Essa opção não existe.')
        limpar()



