while True:

   #Escolha de tipo de conta
   print ("Qual tipo de conta você quer fazer?")
   print("1 - Soma")
   print("2 - Subtração")
   print("3 - Divisão")
   print("4 - Multiplicação")
   print("Digite 'sair' para sair do programa")

   opcao = input ("Sua escolha: ")

   num1 = float (input("Digite o Primeiro número: "))
   num2 = float (input("Digite o Segundo número: "))

   #Variaveis das contas
   soma = (float(num1 + num2))
   subtracao = (float(num1 - num2))
   divisao = (float(num1 / num2))
   multiplicacao = (float(num1 * num2))

   #Calculos
   if opcao == "1":
      print ("")
      print (num1 + num2)

   elif opcao == "2":
      print ("")
      print (num1 - num2) 

   elif opcao == "3":
      print ("")
      print (num1 / num2)

   elif opcao == "4":
      print ("")
      print (num1 * num2)

   else:
      print ("")
      print("ESCOLHA INVALIDA")

   print ("")
