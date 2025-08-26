# comanda.py
import sys
import os

# Adiciona a pasta do projeto no path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from produtos_bar import produtos, listar_produtos

comandas = {}

def adicionar_item(cliente, produto, qtd):
    produto = produto.lower()
    if produto not in produtos:
        raise ValueError(f"Produto '{produto}' não encontrado.")
    if cliente not in comandas:
        comandas[cliente] = []
    comandas[cliente].append((produto, qtd, produtos[produto]))

def calcular_total(cliente):
    if cliente not in comandas:
        return 0
    return sum(qtd * preco for produto, qtd, preco in comandas[cliente])

def listar_itens(cliente):
    if cliente not in comandas:
        return []
    return comandas[cliente]
