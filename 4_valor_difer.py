#Usa a função 'valor absoluto' para comparar "b" e "c"
def f_diferenca(a, b, c):
    if abs(b - a) < abs(c - a):
        return abs(b - a)
    else:
        return abs(c - a)


def main():

    #Entrada de Dados
    a = int(input(""))
    b = int(input(""))
    c = int(input(""))

    #Saída de Dados
    print(f_diferenca(a, b, c))
    

if __name__ == '__main__':
    main()
