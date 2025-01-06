def main():
    saldo = 2000.0

    while True:
        print("\nBem-vindo ao Banco TESTE, por favor digite a operação desejada:")
        print("1 - Verificar saldo")
        print("2 - Realizar saque")
        print("3 - Realizar depósito")
        print("4 - Sair")
        
        try:
            opcao = int(input("Digite sua opção: "))
        except ValueError:
            print("Ops, opção inválida!")
            continue

        if opcao == 1:
            print(f"O seu saldo é de {saldo:.2f}")
        elif opcao == 2:
            try:
                saque = float(input("Digite o valor a ser sacado: "))
            except ValueError:
                print("Valor inválido para saque.")
                continue
            
            if saque > saldo:
                print("O valor não poderá ser sacado, saldo insuficiente.")
            else:
                saldo -= saque
                print(f"Saque realizado com sucesso, o seu saldo restante é: {saldo:.2f}")
        elif opcao == 3:
            try:
                deposito = float(input("Digite o valor a ser depositado: "))
            except ValueError:
                print("Valor inválido para depósito.")
                continue
            
            saldo += deposito
            print(f"Depósito realizado com sucesso, o seu saldo é de: {saldo:.2f}")
        elif opcao == 4:
            print("Obrigado por usar o Banco TESTE. Até logo!")
            break
        else:
            print("Ops, opção inválida!")

if __name__ == "__main__":
    main()

