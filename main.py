#menu do projeto
menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[x] Sair

=>
'''

#variáveis globais
saldo = 0
limite = 500
LIMITE_SAQUES = 3
num_saques = 0
extrato = ""

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
        extrato += "Depósito: R$"+str(round(x, 2))+", \n"
            
    elif op == 's':
        #Saque
        y = float(input('Digite o valor que deseja sacar \n=>' ))

        if y>saldo:
            print('Saque inválido! Valor maior que o saldo.')
            continue  

        elif y>limite:
            print(f'Valor acima do permitido.  Digite um valor abaixo de R$ {limite}')
            continue    

        elif num_saques >= LIMITE_SAQUES:
            print('Limite de saques diários atingidos.')
            continue
        
        else:
            num_saques+=1
            saldo-=y
            extrato += "Saque: R$"+str(round(y, 2))+', \n'
            print('Valor sacado!')
            print(num_saques)

    elif op == 'e':
        #Extrato
        print(f'----- Extrato -----\n******************** \nSaldo: R${saldo: .2f} \n******************** \nTodas as operações: \n{extrato}')
        
    elif op == 'x':
        print('Até logo!')
        break
    else:
        print('Essa opção não existe.')


