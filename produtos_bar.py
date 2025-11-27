import openpyxl
import os

# Caminho do arquivo Excel
CAMINHO_EXCEL = os.path.join(os.path.dirname(__file__), "produtos.xlsx")

produtos = {}

# Carrega os produtos do Excel
wb = openpyxl.load_workbook(CAMINHO_EXCEL)
ws = wb.active

for row in ws.iter_rows(min_row=2, values_only=True):  # Pula o cabeçalho
    if row and len(row) >= 2:
        nome, preco = row[:2]
        # Só adiciona se nome for string e preco for número
        if isinstance(nome, str) and nome and isinstance(preco, (int, float)):
            produtos[nome.lower()] = float(preco)