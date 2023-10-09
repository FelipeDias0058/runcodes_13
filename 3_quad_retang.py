#Função calcula a área
def f_area_retangulo(x, y):
    return x * y

#Função calcula o perímetro
def f_peri_retangulo(x, y):
    return (x * 2) + (y * 2)


def main():

    #Entrada de Dados
    x = int(input("Base: "))
    y = int(input("Altura: "))

    perimetro = f_peri_retangulo(x, y)
    area = f_area_retangulo(x, y)

    #Saída de Dados
    if x != y:
        print(perimetro, "-", area)
    elif x == y:
        print("QUADRADO")
    else:
        print("Digite dois números válidos.")

if __name__ == '__main__':
    main()
