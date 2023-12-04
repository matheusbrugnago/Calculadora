import funcoes
sucesso=True
print("|| Calculadora Básica ||")
print("Por questão de regra matemática. Para esta calculadora é inviável usar 0(zeros)\n")
while True:
    resultado=str(input("Que operação irá ser feita? Digite a letra...\n(a)Soma\n(b)Subtração\n(c)Divisão\n(d)Multiplicação\n(e)Potência\n(f)Raiz\n:"))
    if resultado =="a" or resultado=="b" or resultado=="c" or resultado=="d" or resultado=="e" or resultado=="f" or resultado=="e":
        if resultado !="f":
            numero1=int(input("Digite o primeiro número:\n"))
            numero2=int(input("Digite o segundo número:\n"))
            if resultado=="a":
                print(funcoes.resultadoSoma(numero1,numero2))
            elif resultado=="b":
                print(funcoes.resultadoSubtracao(numero1,numero2))
            elif resultado=="c":
                print(funcoes.resultadoDivisao(numero1,numero2))
            elif resultado=="d":
                print(funcoes.resultadoVezes(numero1,numero2))
            elif resultado == "e":
                print(funcoes.resultadoPotencia(numero1,numero2))
        else:
            numero=int(input("Digite um número:\n"))            
            print(funcoes.resultadoRaiz(numero))
        sequencia=str(input("Digite 'R' de Reiniciar ou 'F' de Finalizar."))
        if sequencia=='R':
            print("Reiniciando")
        else:
            break
    else:
        print("Valores incorretos.Digite novamente.")
print("FIM")
        
    