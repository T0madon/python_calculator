import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH
from components.display import Display

if __name__ == '__main__':
    # Cria aplicação
    app = QApplication(sys.argv)
    window = MainWindow()
    
    # Define o ícone da aplicação
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)

    # Display
    display = Display()
    
    window.addToVLayout(display)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()