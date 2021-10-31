from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    num = ""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(408, 602)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it('1'))
        self.pushButton_1.setGeometry(QtCore.QRect(20, 190, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Pahnto")
        font.setPointSize(24)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet("color:rgb(98, 4, 153);\n"
"background-color: rgb(242, 193, 255);\n"
"")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it('4'))
        self.pushButton_4.setGeometry(QtCore.QRect(20, 280, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Pahnto")
        font.setPointSize(24)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("color:rgb(98, 4, 153);\n"
"background-color: rgb(242, 193, 255);\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it('7'))
        self.pushButton_7.setGeometry(QtCore.QRect(20, 370, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Pahnto")
        font.setPointSize(24)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("color:rgb(98, 4, 153);\n"
"background-color: rgb(242, 193, 255);\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it('8'))
        self.pushButton_8.setGeometry(QtCore.QRect(120, 370, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Pahnto")
        font.setPointSize(24)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("color:rgb(98, 4, 153);\n"
"background-color: rgb(242, 193, 255);\n"
"")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it('2'))
        self.pushButton_2.setGeometry(QtCore.QRect(120, 190, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Pahnto")
        font.setPointSize(24)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color:rgb(98, 4, 153);\n"
"background-color: rgb(242, 193, 255);\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it('5'))
        self.pushButton_5.setGeometry(QtCore.QRect(120, 280, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Pahnto")
        font.setPointSize(24)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("color:rgb(98, 4, 153);\n"
"background-color: rgb(242, 193, 255);\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it('3'))
        self.pushButton_3.setGeometry(QtCore.QRect(220, 190, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Pahnto")
        font.setPointSize(24)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color:rgb(98, 4, 153);\n"
"background-color: rgb(242, 193, 255);\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it('6'))
        self.pushButton_6.setGeometry(QtCore.QRect(220, 280, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Pahnto")
        font.setPointSize(24)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("color:rgb(98, 4, 153);\n"
"background-color: rgb(242, 193, 255);\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_minus = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.collect_num("-"))
        self.pushButton_minus.setGeometry(QtCore.QRect(320, 370, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Pahnto")
        font.setPointSize(24)
        self.pushButton_minus.setFont(font)
        self.pushButton_minus.setStyleSheet("color: rgb(3, 12, 184);\n"
"background-color: rgb(170, 170, 255);\n"
"")
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it('9'))
        self.pushButton_9.setGeometry(QtCore.QRect(220, 370, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Pahnto")
        font.setPointSize(24)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("color:rgb(98, 4, 153);\n"
"background-color: rgb(242, 193, 255);\n"
"")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_x = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.collect_num("*"))
        self.pushButton_x.setGeometry(QtCore.QRect(320, 280, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Pahnto")
        font.setPointSize(24)
        self.pushButton_x.setFont(font)
        self.pushButton_x.setStyleSheet("color: rgb(3, 12, 184);\n"
"background-color: rgb(170, 170, 255);\n"
"")
        self.pushButton_x.setObjectName("pushButton_x")
        self.pushButton_divide = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.collect_num("/"))
        self.pushButton_divide.setGeometry(QtCore.QRect(320, 190, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Pahnto")
        font.setPointSize(24)
        self.pushButton_divide.setFont(font)
        self.pushButton_divide.setStyleSheet("color: rgb(3, 12, 184);\n"
"background-color: rgb(170, 170, 255);\n"
"")
        self.pushButton_divide.setObjectName("pushButton_divide")
        self.pushButton_plus = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.collect_num("+"))
        self.pushButton_plus.setGeometry(QtCore.QRect(320, 460, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Pahnto")
        font.setPointSize(24)
        self.pushButton_plus.setFont(font)
        self.pushButton_plus.setStyleSheet("color: rgb(3, 12, 184);\n"
"background-color: rgb(170, 170, 255);\n"
"\n"
"")
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_dot = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.dot_it())
        self.pushButton_dot.setGeometry(QtCore.QRect(220, 460, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Pahnto")
        font.setPointSize(24)
        self.pushButton_dot.setFont(font)
        self.pushButton_dot.setStyleSheet("color: rgb(3, 12, 184);\n"
"background-color: rgb(170, 170, 255);\n"
"\n"
"")
        self.pushButton_dot.setObjectName("pushButton_dot")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it('0'))
        self.pushButton_0.setGeometry(QtCore.QRect(120, 460, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Pahnto")
        font.setPointSize(24)
        self.pushButton_0.setFont(font)
        self.pushButton_0.setStyleSheet("color:rgb(98, 4, 153);\n"
"background-color: rgb(242, 193, 255);\n"
"")
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_is = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.calculate())
        self.pushButton_is.setGeometry(QtCore.QRect(20, 460, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Pahnto")
        font.setPointSize(24)
        self.pushButton_is.setFont(font)
        self.pushButton_is.setStyleSheet("color: rgb(3, 12, 184);\n"
"background-color: rgb(170, 170, 255);\n"
"")
        self.pushButton_is.setObjectName("pushButton_is")
        self.pushButton_ce = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.pressed_ce())
        self.pushButton_ce.setGeometry(QtCore.QRect(320, 140, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Pahnto")
        font.setPointSize(24)
        self.pushButton_ce.setFont(font)
        self.pushButton_ce.setStyleSheet("color:rgb(0, 151, 226);\n"
"background-color: rgb(184, 238, 244);")
        self.pushButton_ce.setObjectName("pushButton_ce")
        self.pushButton_c = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.pressed_c())
        self.pushButton_c.setGeometry(QtCore.QRect(220, 140, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Pahnto")
        font.setPointSize(24)
        self.pushButton_c.setFont(font)
        self.pushButton_c.setStyleSheet("color:rgb(0, 151, 226);\n"
"background-color: rgb(184, 238, 244);")
        self.pushButton_c.setObjectName("pushButton_c")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 140, 141, 31))
        self.label.setObjectName("label")
        self.valueDisplay = QtWidgets.QLabel(self.centralwidget)
        self.valueDisplay.setGeometry(QtCore.QRect(30, 30, 351, 81))
        font = QtGui.QFont()
        font.setFamily("Pahnto")
        font.setPointSize(28)
        self.valueDisplay.setFont(font)
        self.valueDisplay.setStyleSheet("background-color: rgb(213, 229, 255);")
        self.valueDisplay.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.valueDisplay.setObjectName("valueDisplay")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 408, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
  
    def collect_num(self, symbol):
        self.num += self.valueDisplay.text() + symbol
        self.valueDisplay.setText('0')
        
    def calculate(self):
        self.num += self.valueDisplay.text()
        ans = eval(self.num)
        self.valueDisplay.setText(str(ans))
        self.num = ''

    def pressed_c(self):
        self.valueDisplay.setText('0')
        num = "0"

    def pressed_ce(self):
        self.valueDisplay.setText('0')

    def dot_it(self):
        screen = self.valueDisplay.text()
        if '.' in screen:
                pass
        else:
                self.valueDisplay.setText(f'{screen}.')
 
    def press_it(self,pressed):
        if pressed == 'c':
                self.valueDisplay.setText('0')
        else:
                #Check to see if starts with 0 and delete 0
                if self.valueDisplay.text() == '0':
                        self.valueDisplay.setText('')
                #
                self.valueDisplay.setText(f'{self.valueDisplay.text()}{pressed}')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_minus.setText(_translate("MainWindow", "-"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_x.setText(_translate("MainWindow", "x"))
        self.pushButton_divide.setText(_translate("MainWindow", "/"))
        self.pushButton_plus.setText(_translate("MainWindow", "+"))
        self.pushButton_dot.setText(_translate("MainWindow", "."))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_is.setText(_translate("MainWindow", "="))
        self.pushButton_ce.setText(_translate("MainWindow", "CE"))
        self.pushButton_c.setText(_translate("MainWindow", "C"))
        self.label.setText(_translate("MainWindow", "CALCULATOR"))
        self.valueDisplay.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
