class Produto:
    def __init__(self, nome: str, preco: float, estoque: int = 0):
        if preco < 0:
            raise ValueError("O preço não pode ser negativo.")
        if estoque < 0:
            raise ValueError("O estoque não pode ser negativo.")

        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def adicionar_estoque(self, qtd: int):
        if qtd <= 0:
            raise ValueError("A quantidade deve ser positiva.")
        self.estoque += qtd

    def remover_estoque(self, qtd: int):
        if qtd <= 0:
            raise ValueError("A quantidade deve ser positiva.")
        if qtd > self.estoque:
            raise ValueError("Estoque insuficiente.")
        self.estoque -= qtd

    def aplicar_desconto(self, porcentagem: float):
        if porcentagem < 0 or porcentagem > 100:
            raise ValueError("A porcentagem deve estar entre 0 e 100.")
        desconto = self.preco * (porcentagem / 100)
        self.preco -= desconto

    def __str__(self):
        return f"{self.nome} | Preço: R${self.preco:.2f} | Estoque: {self.estoque}"
