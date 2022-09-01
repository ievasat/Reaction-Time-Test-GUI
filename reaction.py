from frontend import Ui_Form
from PyQt5 import QtCore, QtWidgets, QtTest
import sys
import random
import time

# Scaling Code
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
QtWidgets.QApplication.setHighDpiScaleFactorRoundingPolicy(QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)


class MyWin(QtWidgets.QMainWindow, Ui_Form):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.dragPos = QtCore.QPoint()
        self.records = dict()
        self.ui.labelInstruction.hide()
        self.ui.labelResult.hide()
        self.ui.labelResults.hide()
        self.ui.buttonBack.hide()
        self.ui.button1.clicked.connect(lambda: self.setting(1))
        self.ui.button3.clicked.connect(lambda: self.setting(3))
        self.ui.button5.clicked.connect(lambda: self.setting(5))
        self.ui.buttonTimer.clicked.connect(self.on_press)
        self.ui.buttonTimer.setEnabled(False)
        self.ui.buttonTimer.setDefault(True)
        self.ui.buttonBack.clicked.connect(self.back_home)

    def center(self):
        frameGm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def back_home(self):
        self.ui.labelResult.hide()
        self.ui.labelResults.hide()
        self.ui.buttonBack.hide()
        self.ui.button1.show()
        self.ui.button3.show()
        self.ui.button5.show()
        self.ui.labelTitle.show()

    def setting(self, num):
        self.times = 0
        self.records.clear()
        self.ui.button1.hide()
        self.ui.button3.hide()
        self.ui.button5.hide()
        self.ui.labelTitle.hide()
        self.repeats = num
        self.animate_start()

    def animate_start(self):
        self.anim = QtCore.QPropertyAnimation(self.ui.buttonTimer, b'geometry')
        self.anim.setDuration(1000)
        self.anim.setEndValue(QtCore.QRect(330, 200, 100, 145))
        self.anim.start()
        self.ui.labelInstruction.show()
        self.ui.buttonTimer.setEnabled(True)
        self.ui.buttonTimer.setFocus()

    def animate_end(self):
        self.anim = QtCore.QPropertyAnimation(self.ui.buttonTimer, b'geometry')
        self.anim.setDuration(1000)
        self.anim.setEndValue(QtCore.QRect(640, 0, 100, 145))
        self.anim.start()
        self.ui.labelResult.show()
        self.display_results()
        self.ui.buttonBack.show()

    def display_results(self):
        text = ''
        if self.repeats > 1:
            for k, v in self.records.items():
                text += str(k) + '. ' + str(round(v*1000)) + '\n'
            text += '\nAverage: ' + str(round(sum(self.records.values())*1000/self.repeats)) + ' milliseconds'
        else:
            t = self.records.get(1)
            text = f'{round(t*1000)} milliseconds'
        self.ui.labelResults.setText(text)
        self.ui.labelResults.show()

    def on_press(self):
        if self.times == 0:
            self.ui.labelInstruction.hide()
            self.hide_show()
        elif self.times < self.repeats:
            self.end = time.time()
            self.records[self.times] = self.end-self.start
            self.hide_show()
        else:
            self.end = time.time()
            self.records[self.times] = self.end - self.start
            self.ui.buttonTimer.setEnabled(False)
            self.animate_end()

    def hide_show(self):
        self.ui.buttonTimer.hide()
        self.ui.buttonTimer.setEnabled(False)
        QtTest.QTest.qWait(random.randint(1000, 10000))
        self.ui.buttonTimer.setGeometry(QtCore.QRect(random.randint(0, 660), random.randint(0, 410), 100, 145))
        self.ui.buttonTimer.show()
        self.ui.buttonTimer.setEnabled(True)
        self.ui.buttonTimer.setFocus()
        self.start = time.time()
        self.times += 1


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MyWin()
    screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
    centerPts = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
    y = (w.ui.widget.size().height() // 2)
    x = w.ui.widget.size().width() // 2
    w.showMaximized()
    w.move(centerPts.x() - x, centerPts.y() - int(y * 1.1))
    sys.exit(app.exec_())
