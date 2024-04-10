
menu='''
       Depósito [ d ]
       Sacar    [ s ]
       Extrato  [ e ]
       Sair     [ q ]
    '''


limite_Saques = 3
numero_Saques = 0
limite_Saque = 500
extrato = ''
saldo = 0

while True:
    opcao=input(menu)

    if opcao == 'd':
        Valor = float(input("Digite o valor de Depósito ? " ))

        if Valor > 0:
            saldo += Valor
            extrato += f"Saldo: R$ {saldo}"
    
    
    
    elif opcao ==  "s" :
        Valor = float(input("Qual valor do Saque ?"))

        numero_Saques += 1
        if Valor > limite_Saque:
            print('valor limite excedido')
            continue
        
        if numero_Saques > limite_Saques:
            print('limite diario de saques excedido')




        elif Valor > 0 :
             saldo -= Valor
             print (f" Saque no valor de R$ {Valor} realizado")
             
             extrato += f" Saldo R$ {saldo}"
        elif numero_Saques > limite_Saques :
            print ( " numero de saques excedisdo ")
    


    elif opcao == "e":
        print("================== EXTRATO ====================")
       
        print(f"Saldo: R$ {saldo:.2f}")
        

    elif opcao == "q":
        break


    else :
        print("Opção invalida")




    
    
    


        
            
        
   
