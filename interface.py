import sys
import os
import tkinter as tk
import tkinter.messagebox as msgbox

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from comanda import adicionar_item, calcular_total, listar_itens
from produtos_bar import produtos

def listar_clientes():
    try:
        from comanda import listar_clientes as lc
        return lc()
    except ImportError:
        return []

def atualizar_clientes():
    lista_clientes.delete(0, tk.END)
    for cliente in listar_clientes():
        lista_clientes.insert(tk.END, cliente)

def ao_selecionar_cliente(event):
    selecionado = lista_clientes.curselection()
    if selecionado:
        cliente = lista_clientes.get(selecionado[0])
        entry_cliente.delete(0, tk.END)
        entry_cliente.insert(0, cliente)
        atualizar_lista(cliente)

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
        atualizar_clientes()
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

def resetar_comandas():
    resposta = msgbox.askyesno("Confirmação", "Tem certeza que deseja resetar TODAS as comandas?")
    if resposta:
        from comanda import comandas, salvar_comandas
        comandas.clear()
        salvar_comandas()
        if os.path.exists("comandas.txt"):
            os.remove("comandas.txt")
        atualizar_clientes()
        lista_itens.delete(0, tk.END)
        label_msg.config(text="Comandas resetadas!", fg="red")

root = tk.Tk()
root.title("Comanda do Bar")
root.geometry("520x700")
root.resizable(False, False)

font_label = ("Helvetica", 12, "bold")
font_entry = ("Helvetica", 12)

canvas = tk.Canvas(root, borderwidth=0, width=500, height=680)
frame_principal = tk.Frame(canvas)
scrollbar_pagina = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar_pagina.set)

scrollbar_pagina.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((0, 0), window=frame_principal, anchor="nw")

def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame_principal.bind("<Configure>", on_frame_configure)

def _on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

canvas.bind_all("<MouseWheel>", _on_mousewheel)

tk.Label(frame_principal, text="Produtos Disponíveis", font=font_label).pack(pady=5)
lista_produtos = tk.Listbox(frame_principal, width=50, height=8)
for produto, preco in produtos.items():
    lista_produtos.insert(tk.END, f"{produto} - R$ {preco:.2f}")
lista_produtos.config(state=tk.DISABLED)
lista_produtos.pack(pady=5)

tk.Label(frame_principal, text="Clientes", font=font_label).pack(pady=5)
lista_clientes = tk.Listbox(frame_principal, width=30, height=5)
lista_clientes.pack(pady=5)
lista_clientes.bind("<<ListboxSelect>>", ao_selecionar_cliente)

tk.Label(frame_principal, text="Cliente", font=font_label).pack(pady=5)
entry_cliente = tk.Entry(frame_principal, font=font_entry)
entry_cliente.pack(pady=5)

tk.Label(frame_principal, text="Produto", font=font_label).pack(pady=5)
entry_produto = tk.Entry(frame_principal, font=font_entry)
entry_produto.pack(pady=5)

tk.Label(frame_principal, text="Quantidade", font=font_label).pack(pady=5)
entry_qtd = tk.Entry(frame_principal, font=font_entry)
entry_qtd.pack(pady=5)

btn_add = tk.Button(frame_principal, text="Adicionar Item", bg="#4CAF50", fg="white",
                    font=("Helvetica", 12, "bold"), width=20, command=adicionar)
btn_add.pack(pady=5)

btn_total = tk.Button(frame_principal, text="Mostrar Total", bg="#2196F3", fg="white",
                      font=("Helvetica", 12, "bold"), width=20, command=mostrar_total)
btn_total.pack(pady=5)

btn_reset = tk.Button(frame_principal, text="Resetar Comandas", bg="#F44336", fg="white",
                      font=("Helvetica", 12, "bold"), width=20, command=resetar_comandas)
btn_reset.pack(pady=5)

tk.Label(frame_principal, text="Itens do Cliente", font=font_label).pack(pady=5)

frame_lista = tk.Frame(frame_principal)
frame_lista.pack(pady=5)

scrollbar = tk.Scrollbar(frame_lista, orient=tk.VERTICAL)
lista_itens = tk.Listbox(frame_lista, width=50, yscrollcommand=scrollbar.set)
scrollbar.config(command=lista_itens.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
lista_itens.pack(side=tk.LEFT, fill=tk.BOTH)

label_msg = tk.Label(frame_principal, text="", font=("Helvetica", 12, "italic"))
label_msg.pack(pady=10)

# ...código anterior...

tk.Label(frame_principal, text="Produtos Disponíveis", font=font_label).pack(pady=5)

frame_produtos = tk.Frame(frame_principal)
frame_produtos.pack(pady=5)

scrollbar_produtos = tk.Scrollbar(frame_produtos, orient=tk.VERTICAL)
lista_produtos = tk.Listbox(frame_produtos, width=50, height=8, yscrollcommand=scrollbar_produtos.set)
scrollbar_produtos.config(command=lista_produtos.yview)
scrollbar_produtos.pack(side=tk.RIGHT, fill=tk.Y)
lista_produtos.pack(side=tk.LEFT, fill=tk.BOTH)

for produto, preco in produtos.items():
    lista_produtos.insert(tk.END, f"{produto} - R$ {preco:.2f}")
lista_produtos.config(state=tk.DISABLED)

# ...código posterior...

if __name__ == "__main__":
    atualizar_clientes()
    print("Interface iniciada!")
    root.mainloop()