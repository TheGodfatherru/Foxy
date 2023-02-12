import sys
import random
from PyQt5 import QtCore, QtGui

from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QWidget, QLabel, QPushButton, QLineEdit


class Ui_PrettyFox(object):
    def __init__(self, id, device_type, name):
        self.failed_btn = None
        self.filed_widget = None
        self.success_widget = None
        self.device_type_label = None
        self.equation = None
        self.oauth_label = None
        self.device_name_label = None
        self.lineEdit = None
        self.pushButton = None
        self.new_device_label = None
        self.answer_label = None
        self.centralwidget = None
        self.wrong_answers = 3
        self.type = device_type
        self.name = name
        self.id = id

    def setupUi(self, PrettyFox):
        PrettyFox.setObjectName("PrettyFox")
        PrettyFox.setWindowModality(QtCore.Qt.WindowModal)
        PrettyFox.resize(400, 400)
        PrettyFox.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.centralwidget = QWidget(PrettyFox)
        self.centralwidget.setObjectName("centralwidget")
        self.new_device_label = QLabel(self.centralwidget)
        self.new_device_label.setGeometry(QtCore.QRect(50, 0, 300, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.new_device_label.setFont(font)
        self.new_device_label.setAlignment(QtCore.Qt.AlignCenter)
        self.new_device_label.setObjectName("new_device_label")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 300, 140, 30))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 260, 160, 27))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(12)
        self.lineEdit.setObjectName("lineEdit")
        self.device_name_label = QLabel(self.centralwidget)
        self.device_name_label.setGeometry(QtCore.QRect(0, 50, 391, 21))
        self.device_name_label.setText(f"Тип: {self.type}")
        self.device_name_label.setTextFormat(QtCore.Qt.AutoText)
        self.device_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.device_name_label.setObjectName("device_name_label")
        self.device_type_label = QLabel(self.centralwidget)
        self.device_type_label.setGeometry(QtCore.QRect(0, 80, 391, 21))
        self.device_type_label.setText(f"Модель: {self.name}")
        self.device_type_label.setTextFormat(QtCore.Qt.AutoText)
        self.device_type_label.setAlignment(QtCore.Qt.AlignCenter)
        self.device_type_label.setObjectName("device_type_label")
        self.oauth_label = QLabel(self.centralwidget)
        self.oauth_label.setGeometry(QtCore.QRect(0, 130, 400, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.oauth_label.setFont(font)
        self.oauth_label.setAlignment(QtCore.Qt.AlignCenter)
        self.oauth_label.setObjectName("oauth_label")
        self.answer_label = QLabel(self.centralwidget)
        self.answer_label.setEnabled(True)
        self.answer_label.setGeometry(QtCore.QRect(80, 190, 231, 51))
        font = QtGui.QFont()
        font.setItalic(False)
        self.answer_label.setFont(font)
        self.answer_label.setTabletTracking(False)
        self.answer_label.setText("")
        self.answer_label.setAlignment(QtCore.Qt.AlignCenter)
        self.answer_label.setObjectName("answer_label")
        PrettyFox.setCentralWidget(self.centralwidget)

        self.retranslateUi(PrettyFox)
        QtCore.QMetaObject.connectSlotsByName(PrettyFox)

    def success(self):
        self.success_widget = QMessageBox()
        self.success_widget.setWindowTitle("PrettyFox")
        self.success_widget.setText("Успешная авторизация")
        self.success_widget.setStandardButtons(QMessageBox.Ok)
        self.success_widget.exec_()
        QApplication.quit()

    def fail(self):
        self.filed_widget = QMessageBox()
        self.filed_widget.setWindowTitle('PrettyFox')
        self.filed_widget.setText('Неправильный ответ')

        try_again = self.filed_widget.addButton("Поробовать снова", QMessageBox.YesRole)
        try_again.adjustSize()

        self.filed_widget.exec_()

        if self.filed_widget.clickedButton() == try_again:
            self.filed_widget.close()

    def generate_equation(self):
        equation = f"{random.randint(1, 10)} * {random.randint(1, 10)} + {random.randint(1, 10)}"
        self.answer_label.setText(equation)
        self.equation = [f"{equation} = ?", eval(equation)]

    def oauth(self):
        self.generate_equation()
        self.answer_label.setText(self.equation[0])
        self.pushButton.clicked.connect(self.check)

    def check(self):
        try:
            if int(self.lineEdit.text()) == self.equation[1]:
                with open('ids.txt', 'a') as ids:
                    ids.write(f";{self.id}")
                self.success()
            else:
                self.fail()
                self.lineEdit.setText('')
                self.oauth()
        except ValueError:
            return False

    def retranslateUi(self, PrettyFox):
        _translate = QtCore.QCoreApplication.translate
        PrettyFox.setWindowTitle(_translate("PrettyFox", "PrettyFox"))
        self.new_device_label.setText(_translate("PrettyFox", "Подключенно новое устройство"))
        self.pushButton.setText(_translate("PrettyFox", "Авторизовать "))
        self.lineEdit.setPlaceholderText(_translate("PrettyFox", "Введите ответ: "))
        self.oauth_label.setText(_translate("PrettyFox", "Для авторизации нового устройства, решите уравнение"))


def application(device_id, device_type='Keyboard', device_name='Undefined'):
    app = QApplication(sys.argv)
    PrettyFox = QMainWindow()
    ui = Ui_PrettyFox(device_id, device_type, device_name)
    ui.setupUi(PrettyFox)
    ui.oauth()
    PrettyFox.show()
    app.exec_()
