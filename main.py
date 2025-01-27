from PySide6.QtWidgets import QApplication, QLabel
from main_window import MainWindow
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    label1 = QLabel('O meu texto')
    label1.setStyleSheet('font-size: 50px;')
    window.vlayout.addWidget(label1)
    window.adjustFixedSize()

    window.show()
    app.exec()