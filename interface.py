# interface.py
import sys
import os
import tkinter as tk

# Adiciona a pasta do projeto no path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from comanda import adicionar_item, calcular_total, listar_itens
from produtos_bar import produtos

def adicionar():
    cliente = entry_cliente.get()
    produto = entry_produto.get().lower()
    try:
        qtd = int(entry_qtd.get())
    except ValueError:
        label_msg.config(text="Quantidade inválida!", fg="red")
        return

    if produto in produtos:
        adicionar_item(cliente, produto, qtd)
        label_msg.config(text=f"{qtd}x {produto} adicionado para {cliente}", fg="green")
        atualizar_lista(cliente)
    else:
        label_msg.config(text="Produto não encontrado!", fg="red")

def mostrar_total():
    cliente = entry_cliente.get()
    total = calcular_total(cliente)
    label_msg.config(text=f"Total de {cliente}: R$ {total:.2f}", fg="blue")

def atualizar_lista(cliente):
    lista_itens.delete(0, tk.END)
    for produto, qtd, preco in listar_itens(cliente):
        lista_itens.insert(tk.END, f"{qtd}x {produto} - R$ {preco:.2f}")

# Janela principal
root = tk.Tk()
root.title("Comanda do Bar")
root.geometry("500x500")
root.resizable(False, False)

font_label = ("Helvetica", 12, "bold")
font_entry = ("Helvetica", 12)

tk.Label(root, text="Cliente", font=font_label).pack(pady=5)
entry_cliente = tk.Entry(root, font=font_entry)
entry_cliente.pack(pady=5)

tk.Label(root, text="Produto", font=font_label).pack(pady=5)
entry_produto = tk.Entry(root, font=font_entry)
entry_produto.pack(pady=5)

tk.Label(root, text="Quantidade", font=font_label).pack(pady=5)
entry_qtd = tk.Entry(root, font=font_entry)
entry_qtd.pack(pady=5)

btn_add = tk.Button(root, text="Adicionar Item", bg="#4CAF50", fg="white",
                    font=("Helvetica", 12, "bold"), width=20, command=adicionar)
btn_add.pack(pady=5)

btn_total = tk.Button(root, text="Mostrar Total", bg="#2196F3", fg="white",
                      font=("Helvetica", 12, "bold"), width=20, command=mostrar_total)
btn_total.pack(pady=5)

tk.Label(root, text="Itens do Cliente", font=font_label).pack(pady=5)
lista_itens = tk.Listbox(root, width=50)
lista_itens.pack(pady=5)

label_msg = tk.Label(root, text="", font=("Helvetica", 12, "italic"))
label_msg.pack(pady=10)

if __name__ == "__main__":
    print("Interface iniciada!")
    root.mainloop()
