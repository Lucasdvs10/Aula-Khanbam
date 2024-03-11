import soma
import Subtracao
import multiplicacao
import Divisao

print("Olá, boas vindas à nossa incrível calculadora")

opcao = 's'

while opcao != 'n':
    print("Digite qual operação deseja realizar a seguir:")
    opcao = input("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\nn - para parar o programa\n")

    if(opcao == 'n'):
        break

    resultado = None

    inputA = float(input("Digite o primeiro numero da operacao: "))
    inputB = float(input("Digite o segundo numero da operacao: "))
    match opcao:

        case '1':
            resultado = soma.soma(inputA, inputB)
        case '2':
            resultado = Subtracao.funcaoSubtracao(inputA, inputB)
        case '3':
            resultado = multiplicacao.multiplicacao(inputA, inputB)
        case '4':
            resultado = Divisao.funcaoDivisao(inputA, inputB)
        case _:
            print("Operacao inválida!")

    if(resultado is not None):
        print("-----------------------------")
        print(f"O resultado é: {resultado}")
    