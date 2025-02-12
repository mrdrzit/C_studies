from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QComboBox, QRadioButton,
    QButtonGroup, QTextEdit, QPushButton, QCalendarWidget, QWidget, QLabel, QHBoxLayout
)
from PySide6.QtCore import Qt, QDate, QThread, Signal
from PySide6.QtGui import QIcon
import requests as re
import sys
import os 

# Restaurant options
restaurants = [
    {"id": 1, "nome": "RU Setorial II"},
    {"id": 6, "nome": "RU Setorial I"}
]

class MenuRequestThread(QThread):
    menu_fetched = Signal(dict)
    error_occurred = Signal(str)

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        try:
            response = re.get(self.url).json()
            if response.get("cardapios"):
                self.menu_fetched.emit(response)
            else:
                self.error_occurred.emit("Não há cardápio disponível para a data selecionada")
        except re.exceptions.ConnectionError:
            self.error_occurred.emit("Não foi possível conectar ao servidor da FUMP e obter o cardápio")

class MenuApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bandeco")
        self.is_recess = False

        # Main widget and layout
        main_widget = QWidget()

        # Set maximum and minimum size for the window
        self.setMinimumSize(380, 750)
        self.setMaximumSize(380, 750)

        main_layout = QVBoxLayout()
        
        # Add title for the restaurant name
        title_label = QLabel("Restaurante Universitário")
        title_label.setAlignment(Qt.AlignCenter)  # Center the title
        title_label.setStyleSheet("font-weight: bold; font-size: 15px; color: white;")
        main_layout.addWidget(title_label)
        
        # Dropdown menu for restaurants
        self.restaurant_menu = QComboBox()
        for restaurant in restaurants:
            self.restaurant_menu.addItem(restaurant["nome"])
        self.restaurant_menu.setCurrentIndex(0)
        main_layout.addWidget(self.restaurant_menu)
        
        # Add some space between restaurant and meal type
        main_layout.addSpacing(10)

        # Radio buttons for meal type
        self.selected_meal = "Almoço"
        self.meal_button_group = QButtonGroup()
        
        almoco_radio = QRadioButton("Almoço")
        almoco_radio.setChecked(True)
        almoco_radio.toggled.connect(lambda: self.set_meal_type("Almoço"))
        self.meal_button_group.addButton(almoco_radio)
        
        jantar_radio = QRadioButton("Jantar")
        jantar_radio.toggled.connect(lambda: self.set_meal_type("Jantar"))
        self.meal_button_group.addButton(jantar_radio)

        main_layout.addWidget(almoco_radio)
        main_layout.addWidget(jantar_radio)
        
        # Add space after meal type
        main_layout.addSpacing(10)

        # Get current date
        current_date = QDate.currentDate()

        # Calculate the last Sunday (previous Sunday or today if today is Sunday)
        days_since_sunday = (current_date.dayOfWeek() % 7)  # Sunday is day 7, so we use mod 7
        last_sunday = current_date.addDays(-days_since_sunday)

        # Calculate the next Sunday
        next_sunday = last_sunday.addDays(13)

        # Calendar widget for date selection
        self.calendar = QCalendarWidget()
        self.calendar.setMinimumDate(last_sunday)
        self.calendar.setMaximumDate(next_sunday)
        self.calendar.setSelectedDate(current_date)
        self.calendar.setNavigationBarVisible(False)
        self.calendar.setGridVisible(False)

        main_layout.addWidget(self.calendar)

        # Read-only text area to display the menu
        self.menu_display = QTextEdit()
        self.menu_display.setReadOnly(True)
        main_layout.addWidget(self.menu_display)

        # Button to request the menu
        request_button = QPushButton("Pedir cardápio")
        request_button.setFixedSize(140, 30)  # Square button
        request_button.setStyleSheet("""
            QPushButton {
                background-color: #555555;
                color: white;
                font-weight: bold;
                border-radius: 10px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #666666;
            }
            QPushButton:disabled {
                background-color: #777777;
            }
        """)
        request_button.clicked.connect(self.pedir_cardapio)

        # Create a horizontal layout to center the button
        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(request_button)
        button_layout.addStretch(1)
        
        # Create checkbox to toggle recess mode below the button
        recess_checkbox = QRadioButton("Se for recesso, marque aqui para ver o cardápio do RU Setorial I")
        recess_checkbox.setStyleSheet("color: white;")
        recess_checkbox.toggled.connect(lambda: self.toggle_recess_mode())
        main_layout.addWidget(recess_checkbox)

        # Add the button layout to the main layout
        main_layout.addLayout(button_layout)

        # Set the main layout and widget
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # Apply dark theme and set Helvetica font
        self.setStyleSheet(
        """
            QCalendarWidget {
                background-color: #2b2b2b;
                color: #d3d3d3;
                border: none;
            }

            /* Style the month/year navigation bar */
            QCalendarWidget QToolButton {
                background-color: #3a3a3a;
                color: #d3d3d3;
                border: none;
                margin: 5px;
                padding: 5px;
            }

            /* Weekday header (Mon, Tue, ...) */
            QCalendarWidget QHeaderView::section {
                background-color: #2b2b2b;
                color: #d3d3d3;
                padding: 5px;
                font-weight: bold;
            }

            /* Calendar grid */
            QCalendarWidget QTableView {
                font-size: 14px;
                outline: 0;
                background-color: #2b2b2b;
                selection-background-color: #4c4c4c;
                alternate-background-color: #3a3a3a;
            }

            /* Disabled days */
            QCalendarWidget QTableView::item:disabled {
                color: #707070;
            }

            /* Selected day */
            QCalendarWidget QTableView::item:selected {
                background-color: #5a5a5a;
                color: #ffffff;
            }

            /* Style for weekends (Saturday and Sunday) */
            QCalendarWidget QTableView::item:nth-child(7),  /* Sábado */
            QCalendarWidget QTableView::item:nth-child(1) { /* Domingo */
                color: red;
                font-weight: bold;
            }
        """
        )
        self.set_icons_and_logo()

    def set_icons_and_logo(self):
        window_icon = os.path.abspath(os.path.join(os.path.dirname(__file__), "logo", "charmander.ico"))

        # Set the window icon
        if os.path.exists(window_icon):
            self.setWindowIcon(QIcon(window_icon))


    def set_meal_type(self, meal_type):
        self.selected_meal = meal_type

    def pedir_cardapio(self):
        request_button = self.findChild(QPushButton)
        request_button.setDisabled(True)

        restaurant_name = self.restaurant_menu.currentText()
        restaurant_id = next((r["id"] for r in restaurants if r["nome"] == restaurant_name), None)
        meal = self.selected_meal
        selected_day = self.calendar.selectedDate().toString("yyyy-MM-dd")

        if restaurant_id == 1 and meal == "Jantar" and not self.is_recess:
            self.update_menu_display("Jantar apenas disponível para o RU Setorial I\nPedir cardápio para o almoço")
            request_button.setDisabled(False)
            return

        if restaurant_id and selected_day:
            full_url = f"https://fump.ufmg.br:3003/cardapios/cardapio?id={restaurant_id}&dataInicio={selected_day}&dataFim={selected_day}"
            self.menu_thread = MenuRequestThread(full_url)

            self.menu_thread.menu_fetched.connect(self.process_menu_response)
            self.menu_thread.error_occurred.connect(self.display_error)

            self.menu_thread.start()

    def process_menu_response(self, json_response):
        menu = {}
        for cardapio in json_response['cardapios']:
            for refeicao in cardapio['refeicoes']:
                if refeicao['tipoRefeicao'] == self.selected_meal:
                    for prato in refeicao['pratos']:
                        tipo = prato['tipoPrato']
                        descricao = prato['descricaoPrato']
                        if tipo not in menu:
                            menu[tipo] = []
                        menu[tipo].append(descricao)

        menu['Bebida'] = menu.pop('(um copo)', ['N/A'])
        menu['Molho'] = menu.pop('Tipo de item não cadastrado', ['N/A'])
        menu['Sobremesa'] = menu.pop('Sobremesa 1 (uma porção)', ['N/A'])

        meal_order = {
            'Entrada': ['Entrada 1', 'Entrada 2'],
            'Prato Principal': ['Acompanhamento 1', 'Acompanhamento 2', 'Prato protéico 1', 'Prato protéico 3', 'Guarnição', 'Molho'],
            'Sobremesa': ['Sobremesa', 'Bebida']
        }

        display_text = ""
        for section, items in meal_order.items():
            display_text += f"<b>{self.selected_meal} - {section}</b><br>"
            for item in items:
                if item in menu:
                    for desc in menu[item]:
                        display_text += f"- {desc}<br>"
            display_text += "<br>"

        self.update_menu_display(display_text)
        self.findChild(QPushButton).setDisabled(False)

    def display_error(self, message):
        self.update_menu_display(message)
        self.findChild(QPushButton).setDisabled(False)

    def update_menu_display(self, text):
        self.menu_display.setText(text)

    def toggle_recess_mode(self):
        self.is_recess = not self.is_recess

app = QApplication(sys.argv)
window = MenuApp()
window.show()
sys.exit(app.exec())