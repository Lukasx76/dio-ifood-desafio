balance = 0
limit_to_withdraw = 500
number_of_withdraws = 0
WITHDRAW_LIMIT = 3
operations_in_progress = True

while operations_in_progress:
    option = input("D(depósito) S(saque) E(extrato) Q(sair)\n")

    if option == "D":
        value_to_deposit = float(input("Digite o valor a ser depositado:\n"))
        if value_to_deposit < 0:
            print("Número negativo, operação cancelada")
        balance += value_to_deposit
        print(f"Depósito realizado. O saldo atual é R${balance:.2f}") 

    elif option == "S":
        value_to_withdraw = float(input("Digite o valor a ser sacado:\n"))
        if value_to_withdraw > balance:
            print("Valor a sacar maior que saldo\n")
        elif value_to_withdraw > limit_to_withdraw:
            print("Limite de saque excedido\n")
        elif number_of_withdraws >= WITHDRAW_LIMIT:
            print("Cota de saques já atingiu o limite\n")
        else:
            balance -= value_to_withdraw
            number_of_withdraws += 1
            print(f"Saque realizado. O saldo atual é R${balance:.2f}") 

    elif option == "E":
        print(f"O saldo atual é R${balance:.2f}") 
    else:
        operations_in_progress = False