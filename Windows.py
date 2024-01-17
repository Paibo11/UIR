from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import datetime

class Ui_Form2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(625, 508)
        font = QtGui.QFont()
        font.setPointSize(16)
        Form.setFont(font)
        self.widget = PlotWidget(Form)
        self.widget.setGeometry(QtCore.QRect(80, 209, 411, 211))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 90, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(260, 100, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(320, 40, 291, 141))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        months = []
        imt = []
        with open("date.txt") as f:
            for line in f:
                months.append(int(line))
        with open("IMT.txt") as f:
            for line in f:
                imt.append(float(line))

        pen = pg.mkPen(color=(255, 0, 0))
        month_labels = [
            (m, datetime.date(2023, m, 1).strftime('%B'))
            for m in months
        ]
        self.widget.plot(months, imt, pen=pen, labels=month_labels)
        ax = self.widget.getAxis('bottom')
        ax.setTicks([month_labels])
        x = float(imt[len(imt)-1])
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.label.setText(str(x))
        if x < 18.5:
            self.label_3.setText('Недостаточный вес')
        elif 18.5 < x < 24.9:
            self.label_3.setText('Нормальный вес')
        elif 24.9 < x < 29.9:
            self.label_3.setText('Избыточный вес')
        elif x > 29.9:
            self.label_3.setText('Ожирение')

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.label_2.setText(_translate("Form", "-"))
        self.label_3.setText(_translate("Form", "TextLabel"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form2()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
