import sys
import random
import time
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow


class PrettyFox(QMainWindow):
    def __init__(self):
        super(PrettyFox, self).__init__()
        self.button = QtWidgets.QPushButton(self)
        self.label = QtWidgets.QLabel(self)
        self.input_ans = QtWidgets.QInputDialog(self)
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Pretty Fox")
        self.initUI()

    def initUI(self):
        self.label.move(100, 0)
        self.input_ans.move(100, 100)
        self.button.move(100, 150)
        a = self.__generate_equation()
        self.label.setText(a[0])

    @staticmethod
    def __generate_equation():
        equation = f"{random.randint(1, 10)} * {random.randint(1, 10)} + {random.randint(1, 10)}"
        return f"{equation} = ?", eval(equation)


def Pretty_Fox():
    app = QApplication(sys.argv)
    win = PrettyFox()
    win.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    Pretty_Fox()
