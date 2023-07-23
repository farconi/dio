# SISTEMA BANCÁRIO COM PYTHON

# O programa a seguir permite que você deposite valores positivos, faça saques com um limite diário de R$500, 
# e exiba o extrato com todas as operações realizadas e o saldo atual da conta. 
# Caso o usuário tente sacar um valor acima do saldo disponível ou acima do limite diário de saque, 
# o programa exibirá uma mensagem adequada para informar a restrição.


# Nas linhas a seguir, criaremos uma string menu que contém as opções disponíveis para o usuário. 
# Essas opções serão: "Depositar", "Sacar", "Extrato" e "Sair". 
# Cada opção estará representada por uma letra entre colchetes.

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>
"""

# Aqui serão inicializadas algumas variáveis importantes do programa.
# saldo: Armazena o saldo atual da conta do usuário. Inicialmente, o saldo é definido como zero.
# limite: Define o valor máximo que o usuário pode sacar por vez. O valor inicial é de R$500.
# extrato: É uma string que irá armazenar todas as operações de depósito e saque realizadas pelo usuário.
# numero_saques: É uma variável que contará o número de saques realizados pelo usuário em um determinado dia.
# LIMITE_SAQUES: Define o limite máximo de saques permitidos em um único dia, que é de 3 saques.

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Aqui começaremos um loop infinito que mantém o programa em execução até que o usuário escolha sair.

while True:

# O programa exibe o menu de opções e solicita ao usuário que escolha uma delas.
# O valor digitado é armazenado na variável opcao.

    opcao = input(menu)

# Se o usuário escolher a opção "d", entra nesse bloco de código e exibe a mensagem "Depósito".

    if opcao == "d":
        print("Depósito")
        
# O programa solicitará ao usuário que digite o valor a ser depositado e armazena esse valor na variável valor_deposito. 
# O float antes do input é usado para garantir que o valor digitado seja interpretado como um número de ponto flutuante (com casas decimais).
        
        valor_deposito = float(input("Digite o valor a ser depositado: "))

# Se o valor digitado for maior que zero, isso indica que é um depósito válido. 
# Então, o valor será somado ao saldo atual (variável saldo) 
# uma linha é adicionada ao extrato informando o valor e a natureza da operação e 
# uma mensagem indicará caso o depósito tenha sido bem sucedido.

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R${valor_deposito:.2f}\n"
            print(f"Depósito de R${valor_deposito:.2f} bem sucedido.")

# Caso contrário, se o valor digitado for menor ou igual a zero, é considerado inválido para depósito, 
# e o programa exibirá uma mensagem informando que o valor deve ser positivo.

        else:
            print("Valor inválido para depósito. O valor deve ser positivo.")

# Se o usuário escolher a opção "s", entrará nesse bloco de código que exibirá a mensagem "Saque".

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            print("Saque")

# O programa solicitará ao usuário que digite o valor a ser sacado e armazenará esse valor na variável valor_saque.

            valor_saque = float(input("Digite o valor a ser sacado: "))

# Se o valor do saque for maior que zero, menor ou igual ao saldo atual (saldo) 
# e menor ou igual ao limite de saque (limite), então será um saque válido.

            if 0 < valor_saque <= saldo and valor_saque <= limite:

# O valor do saque será subtraído do saldo atual (saldo), 
# uma linha será adicionada ao extrato informando o valor e a natureza da operação, 
# e o contador de saques diários (numero_saques) será incrementado em 1.

                saldo -= valor_saque
                extrato += f"Saque: R${valor_saque:.2f}\n"
                numero_saques += 1
                print(f"Saque de R${valor_saque:.2f} bem sucedido. Retire o seu dinheiro. Você tem R${saldo:.2f} em conta.")

# Se o valor do saque não atender a alguma das condições acima, é considerado inválido, 
# e o programa exibirá uma mensagem informando que o saque é inválido 
# devido ao saldo insuficiente ou ao limite de saque excedido.
# Caso atenda, exibirá a mensagem do dinheiro que deverá ser retirado.

            else:
                print("Saque inválido. Verifique o saldo ou limite de saques diários.")

# Se o usuário já tiver atingido o limite diário de saques (LIMITE_SAQUES), o programa exibirá essa mensagem:
        
        else:
            print("Limite diário de saques atingido. Aguarde até amanhã para fazer mais saques.")

# Se o usuário escolher a opção "e", entra nesse bloco de código e exibe a mensagem "Extrato".

    elif opcao == "e":
        print("Extrato")

# Se o extrato não estiver vazio (ou seja, se houver alguma operação registrada), 
# o programa exibirá todas as operações registradas no extrato, além do saldo atual da conta.

        if extrato:
            print(extrato)
            print(f"Saldo atual: R${saldo:.2f}")

# Se o extrato estiver vazio, o programa exibirá essa mensagem 
# informando que ainda não houve nenhuma operação registrada no extrato:

        else:
            print("Nenhuma operação registrada no extrato ainda.")

# Se o usuário escolher a opção "q", o loop infinito é quebrado, e o programa é encerrado.

    elif opcao == "q":
        break

# Se o usuário digitar uma opção que não corresponde a nenhuma das opções válidas (d, s, e ou q), 
# o programa exibirá uma mensagem informando que a operação é inválida 
# e pedindo que o usuário selecione uma opção válida.

    else:
        print("Operação inválida, por favor selecione a opção desejada:")