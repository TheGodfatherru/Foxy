from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
import os


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.b1 = QtWidgets.QPushButton(self)
        self.label = QtWidgets.QLabel(self)
        self.initUI()
        self.i = 0

    def button_clicked(self):
        print("clicked")
        self.label.setText(f"{self.i}")
        self.i += 1

    def initUI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Foxy")

        self.label.setText("my first label!")
        self.label.move(50, 50)

        self.b1.setText("click me!")
        self.b1.clicked.connect(self.button_clicked)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
