```python
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
            },
	    {
                "nome": "Abacate",
                "preco": 2,
            }
        ]

    # passa como parametro o atributo que sera comparado para remover repetidos
    def removerRepetido(self, atributo: str):
        valoresPesquisados = []
        produtosFiltrados = []

        for produto in self.produtos:
            if produto[atributo] not in valoresPesquisados:
                produtosFiltrados.append(produto)
                valoresPesquisados.append(produto[atributo])

        return produtosFiltrados
    
    # passa como parametro o atributo que sera comparado para ordenar
    def ordenar(self, atributo: str):
        return sorted(self.produtos, key=lambda produto: produto[atributo])
    
produto = Produto()
print("##REMOVER ITENS REPETIDOS PELO ATRIBUTO")
print("Remove nomes repetidos")
print(produto.removerRepetido("nome"))   # deixa todos os itens por terem nomes diferentes


print("\nRemove nomes repetidos")
print(produto.removerRepetido("preco"))  # remove preco por ter o mesmo valor

#ordenar itens
print("\n\n##ORDENAR")
print("Ordenar por nome")
print(produto.ordenar("nome"))  # ordena por nome


print("\nOrdenar por menor preco")
print(produto.ordenar("preco")) # ordena por preco
```

# Saida
```python
##REMOVER ITENS REPETIDOS PELO ATRIBUTO
Remove nomes repetidos
[{'nome': 'Pão', 'preco': 5}, {'nome': 'Queijo', 'preco': 5}, {'nome': 'Abacate', 'preco': 2}]

Remove nomes repetidos
[{'nome': 'Pão', 'preco': 5}, {'nome': 'Abacate', 'preco': 2}]


##ORDENAR
Ordenar por nome
[{'nome': 'Abacate', 'preco': 2}, {'nome': 'Pão', 'preco': 5}, {'nome': 'Queijo', 'preco': 5}]

Ordenar por menor preco
[{'nome': 'Abacate', 'preco': 2}, {'nome': 'Pão', 'preco': 5}, {'nome': 'Queijo', 'preco': 5}]
