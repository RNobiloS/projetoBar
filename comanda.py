import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from produtos_bar import produtos

comandas = {}

def salvar_comandas():
    with open("comandas.txt", "w", encoding="utf-8") as f:
        for cliente, itens in comandas.items():
            for produto, qtd, preco in itens:
                f.write(f"{cliente};{produto};{qtd};{preco}\n")

def carregar_comandas():
    if not os.path.exists("comandas.txt"):
        return
    with open("comandas.txt", "r", encoding="utf-8") as f:
        for linha in f:
            partes = linha.strip().split(";")
            if len(partes) == 4:
                cliente, produto, qtd, preco = partes
                qtd = int(qtd)
                preco = float(preco)
                if cliente not in comandas:
                    comandas[cliente] = []
                # Soma quantidades se já existir o produto
                for idx, (prod, q, p) in enumerate(comandas[cliente]):
                    if prod == produto and p == preco:
                        comandas[cliente][idx] = (prod, q + qtd, p)
                        break
                else:
                    comandas[cliente].append((produto, qtd, preco))

def adicionar_item(cliente, produto, qtd):
    produto = produto.lower()
    if produto not in produtos:
        raise ValueError(f"Produto '{produto}' não encontrado.")
    preco = produtos[produto]
    if cliente not in comandas:
        comandas[cliente] = []
    for idx, (prod, q, p) in enumerate(comandas[cliente]):
        if prod == produto and p == preco:
            comandas[cliente][idx] = (prod, q + qtd, p)
            break
    else:
        comandas[cliente].append((produto, qtd, preco))
    salvar_comandas()

def calcular_total(cliente):
    if cliente not in comandas:
        return 0
    return sum(qtd * preco for produto, qtd, preco in comandas[cliente])

def listar_itens(cliente):
    if cliente not in comandas:
        return []
    return comandas[cliente]

def listar_clientes():
    return list(comandas.keys())

carregar_comandas()