def saudacao(nome):
    return f"Seja bem-vindo {nome}"

def soma(numero1, numero2):
    resultado = numero1 + numero2
    return f"A soma entre {numero1} + {numero2} = {resultado}"

nome = input("Digite o seu nome: ")
numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
nome = saudacao(nome)
resultado = soma(numero1, numero2)
print(nome)
print(resultado)