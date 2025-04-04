class Produto:
    def __init__(self):
        self.produtos = [
            {
                "nome": "Pão",
                "preco": 5,
            },
            {
                "nome": "Queijo",
                "preco": 5,
            }
        ]

    def removerRepetido(self, atributo: str):
        valoresPesquisados = []
        produtosFiltrados = []

        for produto in self.produtos:
            if produto[atributo] not in valoresPesquisados:
                produtosFiltrados.append(produto)
                valoresPesquisados.append(produto[atributo])

        return produtosFiltrados
    
    def ordenar(self, atributo: str):
        return sorted(self.produtos, key=lambda produto: produto[atributo])
    
produto = Produto()
print(produto.removerRepetido("nome"))   # deixa todos os itens por terem nomes diferentes
print(produto.removerRepetido("preco"))  # remove preco por ter o mesmo valor
print(produto.removerRepetido("preco"))  # remove preco por ter o mesmo valor

print(produto.ordenar("preco")) 