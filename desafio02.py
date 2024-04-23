


def menu():
    menu = """
    MENU
    [d]Depositar
    [s]Sacar
    [e]Extrato
    [nc]Nova conta
    [l]Listar contas
    [n]Novo usuário
    [q]Sair
    """
    return input(menu)




def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saques = numero_saques >= limite_saques

    excedeu_limite = valor > limite
    excedeu_saldo = valor > saldo
   
   
   
   
    
    if excedeu_saldo:
        print(" Operação falhou! Você não tem saldo suficiente. ")

    elif excedeu_limite:
        print(" Operação falhou! O valor do saque excede o limite. ")

    elif excedeu_saques:
        print(" Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:R$ {valor}"
        numero_saques += 1
        print("Saque realizado com sucesso! ")

    else:
        print(" Operação falhou! O valor informado é inválido. ")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print(" EXTRATO ")
    print("Não foram realizadas movimentações.")
    print(f"Saldo:R$ {saldo}")
    





def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(" Conta criada com sucesso! ")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print(" Usuário não encontrado, fluxo de criação de conta encerrado! ")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:{conta['agencia']}
            C/C:{conta['numero_conta']}
            Titular:{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)


def criar_usuario(usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(" Já existe usuário com esse CPF! ")
        return

    nome = input("Informe o nome: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereço : ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print(" Usuário criado com sucesso!")


def depositar(saldo, valor, extrato, ):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor}"
        print(" Depósito realizado com sucesso ")
    else:
        print("Operação falhou! O valor informado é inválido. ")

    return saldo, extrato

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nc":
            criar_usuario(usuarios)

        elif opcao == "n":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "l":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()