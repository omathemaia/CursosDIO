menu = """
[D] -> Depositar
[S] -> Sacar
[E] -> Extrato
[X] -> SAIR 
=> """

saldo = 0
LIMITE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

  opcao = input(menu)

  if opcao == "D":
    print("Deposito")
    deposito = float(input("Digite o valor que deseja depositar:"))
    
    if deposito > 0:
      saldo = saldo + deposito
      extrato += f'O valor depositado foi R${deposito:.2f}\n'
    
    else:
      print ("Operacao Invalida")

  elif opcao == "S":
    print("Sacar")
    saque = float(input("Digite o valor que deseja sacar:"))

    if saque > LIMITE:
      print("Nao e possivel fazer o saque! Seu limite maximo por saque e R$500,00!")
    
    elif saque > saldo:
      print("Nao e possivel sacar um valor maior que o saldo!")

    elif numero_saques >= LIMITE_SAQUES:
      print ("Voce ja atingiu o limite maximo de saque diario")
    
    elif saque > 0:
      saldo -= saque
      extrato += f'O valor sacado foi R${saque:.2f}\n'
      numero_saques = numero_saques + 1
      print(f'Atencao, voce ja sacou:{numero_saques} vez\n')
    
    else:
      print("Operacao invalida")

  elif opcao == "E":
    print(extrato)
    
  
  elif opcao == "X":
    break
    
  else:
    print("Opcao invalida, digite uma opcao valida por favor")