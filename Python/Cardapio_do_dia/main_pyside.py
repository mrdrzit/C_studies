from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QComboBox, QRadioButton,
    QButtonGroup, QTextEdit, QPushButton, QCalendarWidget, QWidget, QLabel, QHBoxLayout
)
from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QIcon, QPixmap
import requests as re
import sys
import os 

# Restaurant options
restaurants = [
    {"id": 1, "nome": "RU Setorial II"},
    {"id": 6, "nome": "RU Setorial I"}
]

class MenuApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pedir Cardápio")

        # Main widget and layout
        main_widget = QWidget()

        # Set maximum and minimum size for the window
        self.setMinimumSize(380, 710)
        self.setMaximumSize(380, 710)

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

        main_layout.addWidget(self.calendar)

        # Read-only text area to display the menu
        self.menu_display = QTextEdit()
        self.menu_display.setReadOnly(True)
        main_layout.addWidget(self.menu_display)

        # Button to request the menu
        request_button = QPushButton("Pedir cardápio")
        request_button.setFixedSize(150, 40)  # Square button
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

        # Add the button layout to the main layout
        main_layout.addLayout(button_layout)

        # Set the main layout and widget
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # Apply dark theme and set Helvetica font
        self.setStyleSheet(
        """
            QWidget {
                font-family: Helvetica;
                color: white;
                background-color: #2e2e2e;
            }
            QComboBox, QRadioButton {
                background-color: #444444;
                border: 1px solid #666666;
                padding: 5px;
                font-weight: bold;
            }
            QComboBox::drop-down {
                border-left: 1px solid #666666;
            }
            QTextEdit {
                color: #ffffff;
            }
            QPushButton:hover {
                background-color: #555555;
            }
            QCalendarWidget {
                background-color: #2b2b2b;
                color: #d3d3d3;
                border: none;
            }

            /* Style the month/year navigation bar */
            QCalendarWidget QToolButton {
                background-color: #3a3a3a;
                color: #707070; /* Greyed out to indicate inactive */
                border: none;
                margin: 5px;
                padding: 5px;
            }

            /* Disable interaction with navigation buttons by making them look inactive */
            QCalendarWidget QToolButton:disabled {
                color: #707070;
            }
            
            /* Disable arrow indicators by removing images */
            QCalendarWidget QToolButton::menu-indicator {
                image: none;
            }

            /* Weekday names (top row) style */
            QCalendarWidget QHeaderView::section {
                background-color: #2b2b2b;
                color: #d3d3d3;
                padding: 5px;
            }

            /* Days in the calendar */
            QCalendarWidget QTableView {
                font-size: 14px;
                outline: 0;
                background-color: #2b2b2b;
                selection-background-color: #4c4c4c;
                alternate-background-color: #3a3a3a;
            }

            /* Disabled days styling */
            QCalendarWidget QTableView::item:disabled {
                color: #707070;
            }

            /* Selected day */
            QCalendarWidget QTableView::item:selected {
                background-color: #5a5a5a;
                color: #ffffff;
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
        # Disable the button to prevent multiple requests
        self.findChild(QPushButton).setDisabled(True)
        
        # Get selected restaurant name and meal type
        restaurant_name = self.restaurant_menu.currentText()
        restaurant_id = next((restaurant["id"] for restaurant in restaurants if restaurant["nome"] == restaurant_name), None)
        meal = self.selected_meal
        selected_day = self.calendar.selectedDate().toString("yyyy-MM-dd")
        
        # Check for valid restaurant and meal availability
        if restaurant_id == 1 and meal == "Jantar":
            self.update_menu_display("Jantar apenas disponível para o RU Setorial I\nPedir cardápio para o almoço")
            self.findChild(QPushButton).setDisabled(False)  # Re-enable the button
            return

        if restaurant_id and selected_day:
            full_url = f"https://fump.ufmg.br:3003/cardapios/cardapio?id={restaurant_id}&dataInicio={selected_day}&dataFim={selected_day}"

            try:
                json_response = re.get(full_url).json()
            except re.exceptions.ConnectionError:
                self.update_menu_display("Não foi possível conectar ao servidor da FUMP e obter o cardápio")
                self.findChild(QPushButton).setDisabled(False)  # Re-enable the button
                return

            if json_response['cardapios'] == []:
                self.update_menu_display("Não há cardápio disponível para a data selecionada")
                self.findChild(QPushButton).setDisabled(False)  # Re-enable the button
                return
            
            # Extract and format the menu
            menu = {}
            for cardapio in json_response['cardapios']:
                for refeicao in cardapio['refeicoes']:
                    if refeicao['tipoRefeicao'] == meal:
                        for prato in refeicao['pratos']:
                            tipo = prato['tipoPrato']
                            descricao = prato['descricaoPrato']
                            if tipo not in menu:
                                menu[tipo] = []
                            menu[tipo].append(descricao)

            # Rename keys for readability
            menu['Bebida'] = menu.pop('(um copo)', ['N/A'])
            menu['Molho'] = menu.pop('Tipo de item não cadastrado', ['N/A'])
            menu['Sobremesa'] = menu.pop('Sobremesa 1 (uma porção)', ['N/A'])

            # Set the meal order for display
            meal_order = {
                'Entrada': ['Entrada 1', 'Entrada 2'],
                'Prato Principal': ['Acompanhamento 1', 'Acompanhamento 2', 'Prato protéico 1', 'Prato protéico 3', 'Guarnição', 'Molho'],
                'Sobremesa': ['Sobremesa', 'Bebida']
            }

            # Format the menu text
            display_text = ""
            for section, items in meal_order.items():
                display_text += f"<b>{meal} - {section}</b><br>"
                for item in items:
                    if item in menu:
                        for desc in menu[item]:
                            display_text += f"- {desc}<br>"
                display_text += "<br>"

            self.update_menu_display(display_text)
            self.findChild(QPushButton).setDisabled(False)  # Re-enable the button

    def update_menu_display(self, text):
        self.menu_display.setText(text)

app = QApplication(sys.argv)
window = MenuApp()
window.show()
sys.exit(app.exec())