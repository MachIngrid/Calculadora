import math
import time

def inicio_calculadora():

 oper = int(input("bem vindo a calculadora da ingrid kk ,me ajude a matar o tédio e escolha que operaçao deseja realizar:\n 1 - soma \n| 2- divisão \n| 3- multiplicação \n| 4 - subtração \n| 5- potenciação\n" ))

 match oper:

     case 1:#soma

          v1 = int(input(" essa é uma soma de dois valores, qual o primeiro valor da soma?"))
          time.sleep(1)
          v2 = int(input("qual o segundo?"))
          soma = v1+v2
          print ("o resultado da soma é: ",soma)


     case 2:#divisão

         d1 = int(input("essa é uma divisão de dois valores inteiros, qual o primeiro valor?"))
         time.sleep(1)
         d2 = int(input("qual o segundo valor?"))
         div = d1/d2
         time.sleep (2)
         print ("o resultado da divisão é:soma" , div)


     case 3:#multiplicação
         
         m1 = int(input("essa é uma multiplicação de dois valores inteiros, qual o primeiro valor?"))
         time.sleep(1)
         m2 = int(input("\nqual o segundo valor?"))
         mult = m1*m2
         time.sleep(2)
         print (" \n --> o resultado da multiplicação é:", mult)


     case 4:#subtração

         s1 = int(input("essa é uma subtração de 2 valores, qual o primeiro valor?"))
         time.sleep(1)
         s2 = int(input("qual o segundo valor?")) 
         sub = s1-s2
         time.sleep(2)
         print("\n --> o resultado da subtraçao é:" ,sub)

     case 5:#potenciação
         base = int(input("\n Essa é uma potenciação, qual o valor da base da sua operação? "))
         time.sleep(1)
         potencia = int(input("\n e qual o valor da potencia? "))
         pot = base ** potencia
         time.sleep(1)
         print("\n --> O resultado da potenciação é:", pot ,"\n")

     case 6 :    




        

    
         
             

inicio_calculadora()

ret = True
while ret:

     opçao = int(input("deseja realizar outra operação? 1-Sim 2-Não"))
     if opçao == 2:
      ret = False
      print("obrigada por usar a calculadora!")    
     elif opçao == 1:
         inicio_calculadora()
     else:
         print("digite uma opção válida") 


      
    
      
      
      