menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[cu] Criar Usuário
[cc] Criar Conta
[q] Sair

=>
"""


# Função para realizar o saque
def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques < limite_saques:
        if 0 < valor <= saldo and valor <= limite:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R${valor:.2f} bem sucedido. Retire o seu dinheiro. Você tem R${saldo:.2f} em conta.")
        else:
            print("Saque inválido. Verifique o saldo ou limite de saques diários.")
    else:
        print("Limite diário de saques atingido. Aguarde até amanhã para fazer mais saques.")
    return saldo, extrato

# Função para realizar o depósito
def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"
        print(f"Depósito de R${valor:.2f} bem sucedido.")
    else:
        print("Valor inválido para depósito. O valor deve ser positivo.")
    return saldo, extrato

# Função para visualizar o extrato
def visualizar_extrato(saldo, *, extrato):
    print("Extrato")
    if extrato:
        print(extrato)
        print(f"Saldo atual: R${saldo:.2f}")
    else:
        print(f"Nenhuma operação registrada no extrato ainda. Seu saldo atual é R${saldo:.2f}")


# Lista para armazenar os usuários (clientes do banco)
usuarios = []

# Função para criar um novo usuário (cliente)
def criar_usuario(nome, data_nascimento, cpf, endereco):
    # Verificar se o usuário já existe pelo CPF
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Já existe um usuário com esse CPF.")
            return None

    usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }
    usuarios.append(usuario)
    print("Usuário criado com sucesso.")
    return usuario

# Lista para armazenar as contas correntes
contas = []

# Função para criar uma nova conta corrente e vincular a um usuário existente
def criar_conta_corrente(cpf_usuario):
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario['cpf'] == cpf_usuario:
            usuario_encontrado = usuario
            break

    if usuario_encontrado is not None:
        numero_conta = len(contas) + 1
        conta = {
            'agencia': '0001',
            'numero_conta': numero_conta,
            'usuario': usuario_encontrado
        }
        contas.append(conta)
        print(f"Conta corrente {numero_conta} criada e vinculada ao usuário {usuario_encontrado['nome']}.")
    else:
        print("Usuário não encontrado.")

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        print("Depósito")
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        saldo, extrato = deposito(saldo, valor_deposito, extrato)

    elif opcao == "s":
        print("Saque")
        valor_saque = float(input("Digite o valor a ser sacado: "))
        saldo, extrato = saque(saldo=saldo, valor=valor_saque, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

    elif opcao == "e":
        visualizar_extrato(saldo, extrato=extrato)

    elif opcao == "cu":
        print("Criar Usuário")
        # Coletar informações para criar usuário (nome, data_nascimento, cpf, endereco)
        nome = input("Digite o nome do usuário: ")
        data_nascimento = input("Digite a data de nascimento do usuário: ")
        cpf = input("Digite o CPF do usuário: ")
        endereco = input("Digite o endereço do usuário: ")
        criar_usuario(nome, data_nascimento, cpf, endereco)

    elif opcao == "cc":
        print("Criar Conta")
        # Coletar o CPF do usuário para vincular à conta corrente
        cpf_usuario = input("Digite o CPF do usuário para vincular à conta corrente: ")
        criar_conta_corrente(cpf_usuario)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione a opção desejada:")