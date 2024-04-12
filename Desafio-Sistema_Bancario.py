# DESAFIO: Python AI Backend Developer Bootcamp DIO
# Criando um Sistema Bancário simples com Python

# Criando o menu principal
def menu():
    print("\n")
    print("======== Bem-vindo ao Banco WIL ========")
    print("Escolha uma opção (Digite o número):")
    print("1 - Efetuar depósito")
    print("2 - Efetuar saque")
    print("3 - Ver Extrato")
    print("4 - Sair")

# Variáveis
saldo = 0
limite = 500
extrato = "======== Extrato ========\n"
numero_saques = 0
LIMITE_SAQUES = 3

# Criando a lógica do sistema

while True:

    menu()
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        valor_deposito = float(input("Digite o valor do depósito: "))
        saldo += valor_deposito
        extrato += f"Depósito de R$ {valor_deposito:.2f}\n"
        print("Depósito efetuado com sucesso!")

    elif opcao == 2:
        if numero_saques < LIMITE_SAQUES:
            valor_saque = float(input("Digite o valor do saque: "))
            if saldo >= valor_saque:
                saldo -= valor_saque
                extrato += f"Saque de R$ {valor_saque:.2f}\n"
                numero_saques += 1
                print("Saque efetuado com sucesso!")
            else:
                print("Saldo insuficiente!")
        else:
            print("Limite de saques diários atingido!")

    elif opcao == 3:
        print(f"Saldo: R$ {saldo}")
        print(f"Limite: R$ {limite}")
        print("Extrato:")
        print(extrato)

    elif opcao == 4:
        print("Obrigado por utilizar o Banco WIL!")
        break

    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")

