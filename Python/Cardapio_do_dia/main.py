import requests as re
import tkinter as tk
from tkinter import ttk
from datetime import datetime

# Restaurant options
restaurants = [
    {"id": 1, "nome": "RU Setorial II"},
    {"id": 6, "nome": "RU Setorial I"}
]

# Initialize Tkinter window
root = tk.Tk()
root.title("Pedir Cardápio")

# Dropdown menu for restaurants
selected_restaurant = tk.StringVar()
restaurant_menu = ttk.Combobox(root, textvariable=selected_restaurant, state="readonly")
restaurant_menu["values"] = [restaurant["nome"] for restaurant in restaurants]
restaurant_menu.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
restaurant_menu.set("Selecione o restaurante")

# Option selection for meal type using Radiobuttons
selected_meal = tk.StringVar(value="Almoço")
almoco_radio = ttk.Radiobutton(root, text="Almoço", variable=selected_meal, value="Almoço")
almoco_radio.grid(row=1, column=0, padx=10, pady=5)
jantar_radio = ttk.Radiobutton(root, text="Jantar", variable=selected_meal, value="Jantar")
jantar_radio.grid(row=1, column=1, padx=10, pady=5)

# Read-only text area to display the menu
menu_display = tk.Text(root, width=60, height=20, state="disabled", wrap="word")
menu_display.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
menu_display.tag_configure("bold", font=("Helvetica", 12, "bold"))
menu_display.config(font=("Helvetica", 12))

# Function to get selected restaurant ID and meal type
def pedir_cardapio():
    restaurant_name = selected_restaurant.get()
    restaurant_id = next((restaurant["id"] for restaurant in restaurants if restaurant["nome"] == restaurant_name), None)
    meal = selected_meal.get()
    
    # Check for valid restaurant and meal availability
    if restaurant_id == 1 and meal == "Jantar":
        update_menu_display("Jantar apenas disponível para o RU Setorial I\nPedir cardápio para o almoço")
        return

    if restaurant_id:
        start_date = datetime.today().strftime('%Y-%m-%d')
        end_date = start_date
        full_url = f"https://fump.ufmg.br:3003/cardapios/cardapio?id={restaurant_id}&dataInicio={start_date}&dataFim={end_date}"

        try:
            json_response = re.get(full_url).json()
        except re.exceptions.ConnectionError:
            update_menu_display("Couldn't connect to FUMP server and retrieve the menu")
            return

        # Extract and format the menu
        menu = {}
        for cardapio in json_response['cardapios']:
            for refeicao in cardapio['refeicoes']:
                if refeicao['tipoRefeicao'] == meal:
                    for prato in refeicao['pratos']:
                        tipo = prato['tipoPrato']
                        descricao = prato['descricaoPrato']
                        menu[tipo] = descricao

        # Rename keys for readability
        menu['Bebida'] = menu.pop('(um copo)', 'N/A')
        menu['Molho'] = menu.pop('Tipo de item não cadastrado', 'N/A')
        
        # Format menu text with bold labels
        menu_display.config(state="normal")
        menu_display.delete(1.0, tk.END)  # Clear previous content
        for tipo, descricao in menu.items():
            # Insert label in bold
            menu_display.insert(tk.END, f"{tipo}: ", "bold")
            # Insert description in regular font
            menu_display.insert(tk.END, f"{descricao}\n")
        menu_display.config(state="disabled")
    else:
        update_menu_display("Please select a valid restaurant")

# Helper function to update the read-only text area
def update_menu_display(text):
    menu_display.config(state="normal")
    menu_display.delete(1.0, tk.END)
    menu_display.insert(tk.END, text)
    menu_display.config(state="disabled")

# Final button to request the menu
request_button = ttk.Button(root, text="Pedir cardápio", command=pedir_cardapio)
request_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
