# produtos_bar.py

produtos = {
    "cerveja lt": 5.00,
    "cerveja gf": 15.00,
    "refri lt": 6.00,
    "refri ks": 8.00,
    "água": 3.00,
    "copão vd": 25.00,
    "copão wk": 40.00,
    "copão gin": 25.00,
    "caipirinha": 25.00,
    "caipiroska": 30.00,
    "energetico": 12.00
}

def listar_produtos():
    print("\n--- Cardápio ---")
    for nome, preco in produtos.items():
        print(f"{nome.capitalize()} - R$ {preco:.2f}")
    print()
