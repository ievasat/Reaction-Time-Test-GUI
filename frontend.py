# Created by: PyQt5 UI code generator 5.15.6
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(10, 33, 760, 560)
        self.widget.setStyleSheet("QWidget#widget{\n"
                                  "border: 10px solid;\n"
                                  "background-color:qlineargradient(spread:pad, x1:0, y1:0.523, x2:0.77, " +
                                  "y2:0.517, stop:0 rgba(16, 68, 124, 255), stop:1 rgba(184, 255, 245, 255));\n"
                                  "border-radius: 50px;}")
        self.widget.setObjectName("widget")
        self.labelTitle = QtWidgets.QLabel(self.widget)
        self.labelTitle.setGeometry(0, 210, 760, 80)
        self.labelTitle.setObjectName("labelTitle")
        self.labelResult = QtWidgets.QLabel(self.widget)
        self.labelResult.setGeometry(QtCore.QRect(0, 110, 760, 80))
        self.labelResult.setObjectName("labelResult")
        self.labelResults = QtWidgets.QLabel(self.widget)
        self.labelResults.setGeometry(QtCore.QRect(0, 190, 760, 230))
        self.labelResults.setObjectName("labelResults")
        self.labelInstruction = QtWidgets.QLabel(self.widget)
        self.labelInstruction.setGeometry(QtCore.QRect(0, 510, 760, 50))
        self.labelInstruction.setObjectName("labelInstruction")
        self.label_list = [self.labelResult, self.labelInstruction, self.labelResults, self.labelTitle]
        for label in self.label_list:
            label.setStyleSheet("color:rgb(39, 39, 39);\n"
                                "border-radius: 50px;\n"
                                "background-color: rgba(255, 255, 255, 0);")
            label.setAlignment(QtCore.Qt.AlignCenter)
            label.setWordWrap(True)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPixelSize(55)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        font.setPixelSize(40)
        self.labelResult.setFont(font)
        font.setPixelSize(26)
        self.labelResults.setFont(font)
        font.setPixelSize(22)
        self.labelInstruction.setFont(font)
        self.buttonTimer = QtWidgets.QPushButton(self.widget)
        self.buttonTimer.setGeometry(QtCore.QRect(640, 0, 100, 145))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPixelSize(160)
        font.setBold(True)
        font.setWeight(75)
        self.buttonTimer.setFont(font)
        self.buttonTimer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonTimer.setStyleSheet("background-color: rgba(0,0,0,0);\n"
                                       "color:rgb(255, 191, 0);\n"
                                       "border-radius: 50px;")
        self.buttonTimer.setObjectName("buttonTimer")
        self.buttonBack = QtWidgets.QPushButton(self.widget)
        self.buttonBack.setGeometry(QtCore.QRect(305, 460, 150, 60))
        self.buttonBack.setObjectName("buttonBack")
        self.button1 = QtWidgets.QPushButton(self.widget)
        self.button1.setGeometry(QtCore.QRect(170, 310, 100, 60))
        self.button1.setObjectName("button1")
        self.button3 = QtWidgets.QPushButton(self.widget)
        self.button3.setGeometry(QtCore.QRect(330, 310, 100, 60))
        self.button3.setObjectName("button3")
        self.button5 = QtWidgets.QPushButton(self.widget)
        self.button5.setGeometry(QtCore.QRect(490, 310, 100, 60))
        self.button5.setObjectName("button5")
        font = QtGui.QFont()
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        button_list = [self.button1, self.button5, self.button3, self.buttonBack]
        for button in button_list:
            button.setFont(font)
            button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            name = button.objectName()
            button.setStyleSheet(f"QPushButton#{name}" +
                                 "{border-radius: 20px;\n"
                                 "border: 5px solid;\n"
                                 "border-color: rgb(39, 39, 39);\n"
                                 "background-color:rgb(39, 39, 39);\n"
                                 "color: rgb(184, 255, 245);}"
                                 f"QPushButton#{name}:hover"
                                 "{background-color:rgba(0,0, 0, 0);\n"
                                 "color: rgb(39, 39, 39);}"
                                 f"QPushButton#{name}:pressed"
                                 "{padding-top:5px;\n"
                                 "padding-left:5px;}")
        self.buttonClose = QtWidgets.QPushButton(Form)
        self.buttonClose.setGeometry(QtCore.QRect(660, 3, 27, 27))
        self.buttonClose.setObjectName("buttonClose")
        self.buttonMinimize = QtWidgets.QPushButton(Form)
        self.buttonMinimize.setGeometry(QtCore.QRect(700, 3, 27, 27))
        self.buttonMinimize.setObjectName("buttonMinimize")
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPixelSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.buttonClose.setFont(font)
        font.setPixelSize(20)
        self.buttonMinimize.setFont(font)
        self.top_buttons = [self.buttonClose, self.buttonMinimize]
        for button in self.top_buttons:
            button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            name = button.objectName()
            button.setStyleSheet(f"QPushButton#{name}"
                                 "{border-radius: 10px;\n"
                                 "border: 3px solid;\n"
                                 "border-color: rgb(39, 39, 39);\n"
                                 "background-color:rgb(39, 39, 39);\n"
                                 "color: rgb(184, 255, 245);\n"
                                 "padding-bottom:3px;}"
                                 f"QPushButton#{name}:hover"
                                 "{background-color:rgb(184, 255, 245);\n"
                                 "color: rgb(39, 39, 39);}"
                                 f"QPushButton#{name}:pressed"
                                 "{padding-top:5px;\n"
                                 "padding-left:5px;\n}")
        self.buttonClose.clicked.connect(Form.close)
        self.buttonMinimize.clicked.connect(Form.showMinimized)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labelTitle.setText(_translate("Form", "Reaction Time Test"))
        self.labelResult.setText(_translate("Form", "Your reaction time:"))
        self.labelResults.setText(_translate("Form", ""))
        self.buttonTimer.setText(_translate("Form", "⚡"))
        self.labelInstruction.setText(
            _translate("Form", "Press Enter to start and when lightning reappears on screen"))
        self.button1.setText(_translate("Form", "1x Test"))
        self.button3.setText(_translate("Form", "Repeat 3x"))
        self.button5.setText(_translate("Form", "Repeat 5x"))
        self.buttonBack.setText(_translate('Form', 'Test again'))
        self.buttonClose.setText(_translate("Form", "x"))
        self.buttonMinimize.setText(_translate("Form", "-"))


# if __name__ == "__main__":
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())
