sucesso=True
print("|| Calculadora Básica ||")
print("Por questão de regra matemática. Para esta calculadora é inviável usar 0(zeros)")
numero1=int(input("Digite o primeiro número:\n"))
sinal=str(input("Operador(+,-,/,*):\n"))
numero2=int(input("Digite o segundo número:\n"))
while numero1 !=0 and numero2 !=0:
    if sinal=="+":
        operacao=numero1+numero2
    elif sinal=="-":
        operacao=numero1-numero2
    elif sinal=="/":
        operacao=numero1/numero2
    elif sinal=="*":
        operacao=numero1*numero2
    else:
        sucesso=False
    print("Resultado: ",operacao)
    sequencia=str(input("Digite 'R' de Reiniciar ou 'F' de Finalizar."))
    if sequencia=='R':
        print("Reiniciando...")
        numero1=int(input("Digite o primeiro número:\n"))
        sinal=str(input("Operador(+,-,/,*):\n"))
        numero2=int(input("Digite o segundo número:\n"))
    else:
        sucesso=False
    if sucesso==False:
        numero1=0
print("FIM")