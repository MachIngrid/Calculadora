import math
import time
def retorno_operacao():#Para realizar outra operação
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

def inicio_calculadora():#para usar a calculadora

 oper = input("""bem vindo a calculadora da ingrid kk ,me ajude a matar o tédio e escolha que operaçao deseja realizar:\n
 | Soma 
 | Divisão 
 | Multiplicação 
 | Subtração 
 | Potenciação
 | Raiz
 | Porcentagem\n 
 Digite o Nome da operação desejada exatamente como está apresentada (considere letras maiusculas e minúsculas)->""")

 

 if oper == "Soma" :

    v1 = float(input(" \nessa é uma soma de dois valores, qual o primeiro valor da soma?"))
    time.sleep(1)
    v2 = float(input("\nqual o segundo?"))
    soma = v1+v2
    print ("\no resultado da soma é: ",soma) 

 elif oper == "Divisão" :

    d1 = float(input("\nessa é uma divisão de dois valores inteiros, qual o primeiro valor?"))
    time.sleep(1)
    d2 =float(input("\nqual o segundo valor?"))
    div = d1/d2
    time.sleep (2)
    print ("\no resultado da divisão é:" , div)

 elif oper == "Multiplicação" :

    m1 = float(input("\nessa é uma multiplicação de dois valores inteiros, qual o primeiro valor?"))
    time.sleep(1)
    m2 = float(input("\nqual o segundo valor?"))
    mult = m1*m2
    time.sleep(2)
    print (" \n --> o resultado da multiplicação é:", mult)

 elif oper == "Subtração":

    s1 = float(input("\nessa é uma subtração de 2 valores, qual o primeiro valor?"))
    time.sleep(1)
    s2 = float(input("\nqual o segundo valor?")) 
    sub = s1-s2
    time.sleep(2)
    print("\n --> o resultado da subtração é:" ,sub)

 elif oper == "Potenciação":

    base = float(input("\n Essa é uma potenciação, qual o valor da base da sua operação? "))
    time.sleep(1)
    potencia = float(input("\n e qual o valor da potencia? "))
    pot = base ** potencia
    time.sleep(1)
    print("\n --> O resultado da potenciação é:", pot ,"\n")

 elif oper == "Raiz":

    grau = float(input("\nqual o grau da raiz que deseja calcular?"))  
    time.sleep(1)
    r1 = float(input("qual o valor deseja calcular a raiz?"))
    raiz = r1 ** (1/grau)
    time.sleep(1)
    print("\no valor da raiz calculada é:",raiz)   

 elif oper == "Porcentagem":

    valor = float(input("\nqual o valor inicial?"))  
    percent = float(input("\n que porcentagem deseja saber desse valor?"))
    porcentagem = valor * (percent/100)
    time.sleep(1)
    print("\n ",{percent}," por cento de ",{valor},"é:",porcentagem)

 else:
    print("\nesta não é uma operação válida.") 
    retorno_operacao()
    
inicio_calculadora()
retorno_operacao()


      
    
      
      
      