import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from PySide6.QtGui import QIcon
from info import Info
from variables import WINDOW_ICON_PATH
from components.display import Display
from styles import setupTheme
from buttons import ButtonsGrid

if __name__ == '__main__':
    # Cria aplicação
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()
    
    # Define o ícone da aplicação
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info 
    info = Info('Sua conta')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()