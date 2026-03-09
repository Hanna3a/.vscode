 #calculadora de raiz quadrada
 #09/02/26
while True:
    numero = int(input("Digite um número para ver sua raiz quadrada (ou 0 para sair):"))
    if numero == 0:
        break
    if numero < 0:
        print("Não é possível calcular a raiz quadrada de um número negativo.")
    else:
        raiz_quadrada = numero ** 0.5
    print(f"A raiz quadrada de {numero} é {raiz_quadrada}")
