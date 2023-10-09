# Lê os dados digitados e realiza uma operação aritmética
def f_calculadora(a, b, c):
    if c == 1:
        return a + b
    if c == 2:
        return a - b
    if c == 3:
        return a * b
    if c == 4:
        return a / b
    else:
        raise ValueError(f'Digite um número válido.')


def main():
    x = int(input("").strip())
    y = int(input("").strip())
    operacao = int(input("").strip())

    resultado = f_calculadora(x, y, operacao)
    print(resultado)


if __name__ == '__main__':
    main()
