from produto import Produto

def main():
    p = Produto("Mouse Gamer", 150.00, 10)

    print("Produto inicial:")
    print(p)

    print("\nAdicionando estoque (+5)...")
    p.adicionar_estoque(5)
    print(p)

    print("\nRemovendo estoque (-3)...")
    p.remover_estoque(3)
    print(p)

    print("\nAplicando desconto de 20%...")
    p.aplicar_desconto(20)
    print(p)

if __name__ == "__main__":
    main()
