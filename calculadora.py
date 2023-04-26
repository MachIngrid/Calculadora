# a melhorar: permitir que seja digitado o nome da operação em string;
#
import math
import time

def inicio_calculadora():

 oper = int(input("""bem vindo a calculadora da ingrid kk ,me ajude a matar o tédio e escolha que operaçao deseja realizar:\n
 | 1 | - soma 
 | 2 | - divisão 
 | 3 | - multiplicação 
 | 4 | - subtração 
 | 5 | - potenciação
 | 6 | - Raiz
 | 7 | - porcentagem\n
 Digite o valor da operação desejada->"""))

 match oper:

     case 1:#soma

          v1 = float(input(" essa é uma soma de dois valores, qual o primeiro valor da soma?"))
          time.sleep(1)
          v2 = float(input("qual o segundo?"))
          soma = v1+v2
          print ("o resultado da soma é: ",soma)


     case 2:#divisão

         d1 = float(input("essa é uma divisão de dois valores inteiros, qual o primeiro valor?"))
         time.sleep(1)
         d2 =float(input("qual o segundo valor?"))
         div = d1/d2
         time.sleep (2)
         print ("o resultado da divisão é:soma" , div)


     case 3:#multiplicação
         
         m1 = float(input("essa é uma multiplicação de dois valores inteiros, qual o primeiro valor?"))
         time.sleep(1)
         m2 = float(input("\nqual o segundo valor?"))
         mult = m1*m2
         time.sleep(2)
         print (" \n --> o resultado da multiplicação é:", mult)


     case 4:#subtração

         s1 = float(input("essa é uma subtração de 2 valores, qual o primeiro valor?"))
         time.sleep(1)
         s2 = float(input("qual o segundo valor?")) 
         sub = s1-s2
         time.sleep(2)
         print("\n --> o resultado da subtraçao é:" ,sub)

     case 5:#potenciação
         
         base = float(input("\n Essa é uma potenciação, qual o valor da base da sua operação? "))
         time.sleep(1)
         potencia = float(input("\n e qual o valor da potencia? "))
         pot = base ** potencia
         time.sleep(1)
         print("\n --> O resultado da potenciação é:", pot ,"\n")

     case 6 :  #raiz 
         
         grau = float(input("\nqual o grau da raiz que deseja calcular?"))  
         time.sleep(1)
         r1 = float(input("qual o valor deseja calcular a raiz?"))
         raiz = r1 ** (1/grau)
         time.sleep(1)
         print("\no valor da raiz calculada é:",raiz)

     case 7:#porcentagem
         
         valor = float(input("\nqual o valor inicial?"))  
         percent = float(input("\n que porcentagem deseja saber desse valor?"))
         porcentagem = valor * (percent/100)
         time.sleep(1)
         print("\n ",{percent}," por cento de ",{valor},"é:",porcentagem)


         


        
inicio_calculadora()

ret = True
while ret:

     opçao = int(input("\ndeseja realizar outra operação? 1-Sim 2-Não"))
     if opçao == 2:
      ret = False
      print("\n Obrigada por usar a calculadora!")    
     elif opçao == 1:
         inicio_calculadora()
     else:
         time.sleep(1)
         print("***DIGITE UMA OPERAÇÃO VÁLIDA***") 


      
    
      
      
      