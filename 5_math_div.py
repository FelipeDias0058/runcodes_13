def f_matematica(x, y):
    #Calcula a divisão inteira
    def f_div_resto(x, y):
        return x % 5

    #Determina par ou ímpar
    def f_par(x):
        if x % 2 == 0:
            return "par"
        else:
            return "ímpar"

    n = f_div_resto(x, y)

    #Condicionais para 'n'
    if n == 0:
        return (9 * x) + 7
    elif n == 1:
        return f_par(x)
    elif n == 2:
        return (5 * (x ** 2)) - (3 * x) + 42
    elif n == 3:
        return x // 10
    elif n == 4:
        return x ** 2
    else:
        raise ValueError(f'Erro.')   


def main():

    #Entrada de Dados
    x = int(input(""))

    #Saída de Dados
    print(f_matematica(x, 5))


if __name__ == '__main__':
    main()

   
