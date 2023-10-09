# Função que compara as variáveis e exibe uma mensagem
def f_n_comp(a, b, c):
    if a == b == c:
        return "Todos os valores são iguais"
    elif a == b or b == c or a == c:
        return "Existem dois valores iguais e um diferente"
    elif a != b != c:
        return "Todos os valores são diferentes"


def main():
    # Entrada de Dados
    a = input("").strip()
    b = input("").strip()
    c = input("").strip()

    # Saída de Dados
    print(f_n_comp(a, b, c))


if __name__ == '__main__':
    main()
