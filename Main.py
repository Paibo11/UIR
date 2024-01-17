from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import datetime
from Windows import Ui_Form2
import re

class Ui_Form(object):

    def openWindow(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form2()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(416, 273)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 150, 391, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 220, 391, 28))
        self.pushButton_2.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, 120, 121, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(150, 50, 111, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 371, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 80, 371, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.result()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.lineEdit, self.lineEdit_2)
        Form.setTabOrder(self.lineEdit_2, self.pushButton)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Рассчитать ИМТ"))
        self.pushButton_2.setText(_translate("Form", "Показать прогресс"))
        self.label.setText(_translate("Form", "Введите свой рост"))
        self.label_2.setText(_translate("Form", "Введите свой вес"))

    def result(self):
        self.pushButton.clicked.connect(lambda: self.IMT())
        self.pushButton_2.clicked.connect(lambda: self.openWindow())

    def IMT(self):
        n1 = self.lineEdit.text()
        n2 = self.lineEdit_2.text()
        if n1.isdigit() == False and (re.match("^\d+?\.\d+?$", n2) is None or n2.isdigit() == False):
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Вы ввели неверные данные")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec()
        else:
            mt = int(n1) / (float(n2) * float(n2))
            with open("IMT.txt", 'a') as f1:
                f1.write(str(mt) + '\n')
            current_date = datetime.datetime.now().strftime('%m')
            print(current_date)
            with open("date.txt", 'a') as f2:
                if current_date[0] == '0':
                    f2.write(current_date[1] + '\n')
                else:
                    f2.write(current_date + '\n')
            self.openWindow()



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
