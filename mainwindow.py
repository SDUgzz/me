# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1211, 839)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox1.setGeometry(QtCore.QRect(49, 130, 250, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.comboBox1.setFont(font)
        self.comboBox1.setMouseTracking(False)
        self.comboBox1.setEditable(False)
        self.comboBox1.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox1.setObjectName("comboBox1")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox2.setGeometry(QtCore.QRect(329, 130, 250, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.comboBox2.setFont(font)
        self.comboBox2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox2.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox2.setObjectName("comboBox2")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox4.setGeometry(QtCore.QRect(900, 130, 250, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.comboBox4.setFont(font)
        self.comboBox4.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox4.setObjectName("comboBox4")
        self.comboBox4.addItem("")
        self.comboBox4.addItem("")
        self.comboBox4.addItem("")
        self.comboBox4.addItem("")
        self.comboBox4.addItem("")
        self.comboBox3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox3.setGeometry(QtCore.QRect(620, 130, 250, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.comboBox3.setFont(font)
        self.comboBox3.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox3.setObjectName("comboBox3")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(910, 220, 150, 40))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(910, 280, 150, 40))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(720, 220, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(720, 280, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 90, 191, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(410, 90, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(660, 90, 151, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 730, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 70, 1151, 111))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(2)
        self.frame.setMidLineWidth(1)
        self.frame.setObjectName("frame")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(890, 20, 201, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(16)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 730, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(780, 730, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(18)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.frame3 = QtWidgets.QFrame(self.centralwidget)
        self.frame3.setGeometry(QtCore.QRect(620, 190, 561, 521))
        self.frame3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame3.setLineWidth(2)
        self.frame3.setMidLineWidth(1)
        self.frame3.setObjectName("frame3")
        self.label_14 = QtWidgets.QLabel(self.frame3)
        self.label_14.setGeometry(QtCore.QRect(900, 20, 201, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(16)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.frame4 = QtWidgets.QFrame(self.frame3)
        self.frame4.setGeometry(QtCore.QRect(30, 220, 501, 291))
        self.frame4.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame4.setLineWidth(2)
        self.frame4.setMidLineWidth(1)
        self.frame4.setObjectName("frame4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame4)
        self.lineEdit_5.setGeometry(QtCore.QRect(170, 110, 150, 25))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label = QtWidgets.QLabel(self.frame4)
        self.label.setGeometry(QtCore.QRect(220, 80, 51, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_9 = QtWidgets.QLabel(self.frame4)
        self.label_9.setGeometry(QtCore.QRect(50, 150, 81, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_16 = QtWidgets.QLabel(self.frame4)
        self.label_16.setGeometry(QtCore.QRect(50, 210, 81, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_12 = QtWidgets.QLabel(self.frame4)
        self.label_12.setGeometry(QtCore.QRect(210, 210, 75, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame4)
        self.label_13.setGeometry(QtCore.QRect(380, 150, 75, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame4)
        self.lineEdit_7.setGeometry(QtCore.QRect(180, 180, 150, 25))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_11 = QtWidgets.QLabel(self.frame4)
        self.label_11.setGeometry(QtCore.QRect(380, 210, 75, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_10 = QtWidgets.QLabel(self.frame4)
        self.label_10.setGeometry(QtCore.QRect(210, 147, 75, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame4)
        self.lineEdit_6.setGeometry(QtCore.QRect(10, 180, 150, 25))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_4 = QtWidgets.QLabel(self.frame4)
        self.label_4.setGeometry(QtCore.QRect(170, 20, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_4.setLineWidth(0)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame4)
        self.lineEdit_8.setGeometry(QtCore.QRect(340, 180, 150, 21))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame4)
        self.lineEdit_9.setGeometry(QtCore.QRect(10, 240, 150, 25))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame4)
        self.lineEdit_10.setGeometry(QtCore.QRect(180, 240, 141, 25))
        self.lineEdit_10.setText("")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame4)
        self.lineEdit_11.setGeometry(QtCore.QRect(340, 240, 151, 25))
        self.lineEdit_11.setText("")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_5 = QtWidgets.QLabel(self.frame3)
        self.label_5.setGeometry(QtCore.QRect(100, 150, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame3)
        self.lineEdit_4.setGeometry(QtCore.QRect(290, 150, 150, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.frame4.raise_()
        self.label_14.raise_()
        self.label_5.raise_()
        self.lineEdit_4.raise_()
        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        self.frame1.setGeometry(QtCore.QRect(30, 190, 561, 521))
        self.frame1.setFrameShape(QtWidgets.QFrame.Box)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setLineWidth(1)
        self.frame1.setMidLineWidth(1)
        self.frame1.setObjectName("frame1")
        self.label_17 = QtWidgets.QLabel(self.frame1)
        self.label_17.setGeometry(QtCore.QRect(60, 150, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(16)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.frame1)
        self.label_18.setGeometry(QtCore.QRect(180, 240, 51, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(14)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame1)
        self.label_19.setGeometry(QtCore.QRect(170, 280, 71, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.frame1)
        self.label_20.setGeometry(QtCore.QRect(170, 360, 75, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(14)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.frame1)
        self.label_21.setGeometry(QtCore.QRect(170, 480, 75, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(14)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.frame1)
        self.label_22.setGeometry(QtCore.QRect(170, 320, 71, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(14)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.frame1)
        self.label_23.setGeometry(QtCore.QRect(170, 400, 75, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(14)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_31 = QtWidgets.QLabel(self.frame1)
        self.label_31.setGeometry(QtCore.QRect(170, 440, 75, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(14)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.frame1)
        self.label_32.setGeometry(QtCore.QRect(60, 10, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(16)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.frame1)
        self.label_33.setGeometry(QtCore.QRect(170, 110, 101, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(15)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.frame1)
        self.label_34.setGeometry(QtCore.QRect(170, 70, 121, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(15)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame1)
        self.lineEdit_12.setGeometry(QtCore.QRect(290, 70, 101, 25))
        self.lineEdit_12.setText("")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame1)
        self.lineEdit_13.setGeometry(QtCore.QRect(290, 110, 101, 25))
        self.lineEdit_13.setText("")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_35 = QtWidgets.QLabel(self.frame1)
        self.label_35.setGeometry(QtCore.QRect(310, 30, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.frame1)
        self.lineEdit_14.setGeometry(QtCore.QRect(310, 240, 121, 25))
        self.lineEdit_14.setText("")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.frame1)
        self.lineEdit_15.setGeometry(QtCore.QRect(310, 280, 121, 25))
        self.lineEdit_15.setText("")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.frame1)
        self.lineEdit_16.setGeometry(QtCore.QRect(310, 320, 121, 25))
        self.lineEdit_16.setText("")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.frame1)
        self.lineEdit_17.setGeometry(QtCore.QRect(310, 360, 121, 25))
        self.lineEdit_17.setText("")
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.frame1)
        self.lineEdit_18.setGeometry(QtCore.QRect(310, 400, 121, 25))
        self.lineEdit_18.setText("")
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.frame1)
        self.lineEdit_19.setGeometry(QtCore.QRect(310, 440, 121, 25))
        self.lineEdit_19.setText("")
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.frame1)
        self.lineEdit_20.setGeometry(QtCore.QRect(310, 480, 121, 25))
        self.lineEdit_20.setText("")
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.label_37 = QtWidgets.QLabel(self.frame1)
        self.label_37.setGeometry(QtCore.QRect(170, 200, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.frame2 = QtWidgets.QFrame(self.frame1)
        self.frame2.setGeometry(QtCore.QRect(20, 150, 511, 361))
        self.frame2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame2.setLineWidth(2)
        self.frame2.setMidLineWidth(1)
        self.frame2.setObjectName("frame2")
        self.label_36 = QtWidgets.QLabel(self.frame2)
        self.label_36.setGeometry(QtCore.QRect(310, 50, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.frame2.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.label_31.raise_()
        self.label_32.raise_()
        self.label_33.raise_()
        self.label_34.raise_()
        self.lineEdit_12.raise_()
        self.lineEdit_13.raise_()
        self.label_35.raise_()
        self.lineEdit_14.raise_()
        self.lineEdit_15.raise_()
        self.lineEdit_16.raise_()
        self.lineEdit_17.raise_()
        self.lineEdit_18.raise_()
        self.lineEdit_19.raise_()
        self.lineEdit_20.raise_()
        self.label_37.raise_()
        self.frame.raise_()
        self.frame3.raise_()
        self.comboBox1.raise_()
        self.comboBox2.raise_()
        self.comboBox4.raise_()
        self.comboBox3.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.frame1.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1211, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox1.setCurrentText(_translate("MainWindow", "请点击下拉菜单！"))
        self.comboBox1.setItemText(0, _translate("MainWindow", "请点击下拉菜单！"))
        self.comboBox1.setItemText(1, _translate("MainWindow", "复杂地层分界，无法辨别"))
        self.comboBox1.setItemText(2, _translate("MainWindow", "平缓层：地层倾角<5°"))
        self.comboBox1.setItemText(3, _translate("MainWindow", "缓倾斜层：地层倾角在5~15°"))
        self.comboBox1.setItemText(4, _translate("MainWindow", "中等倾斜层：地层倾角在15~30°"))
        self.comboBox1.setItemText(5, _translate("MainWindow", "陡峭层：地层倾角＞30°"))
        self.comboBox2.setItemText(0, _translate("MainWindow", "请点击下拉菜单！"))
        self.comboBox2.setItemText(1, _translate("MainWindow", "复杂地层特征 无法辨别"))
        self.comboBox2.setItemText(2, _translate("MainWindow", "软硬岩占比1:1（非主要地层类型）"))
        self.comboBox2.setItemText(3, _translate("MainWindow", "软硬岩占比1:2（影响可能较小）"))
        self.comboBox2.setItemText(4, _translate("MainWindow", "软硬岩占比2:1；（影响较明显）"))
        self.comboBox4.setItemText(0, _translate("MainWindow", "请点击下拉菜单！"))
        self.comboBox4.setItemText(1, _translate("MainWindow", "弱孔隙水区：＜1 kPa"))
        self.comboBox4.setItemText(2, _translate("MainWindow", "中等孔隙水区：1~10 kPa"))
        self.comboBox4.setItemText(3, _translate("MainWindow", "强孔隙水区：10~50 kPa"))
        self.comboBox4.setItemText(4, _translate("MainWindow", "强孔隙水区：10~50 kPa"))
        self.comboBox3.setItemText(0, _translate("MainWindow", "请点击下拉菜单！"))
        self.comboBox3.setItemText(1, _translate("MainWindow", "微应力区：地表，＜1 MPa"))
        self.comboBox3.setItemText(2, _translate("MainWindow", "低应力区：1~10 MPa"))
        self.comboBox3.setItemText(3, _translate("MainWindow", "中等应力区：10~100 MPa"))
        self.comboBox3.setItemText(4, _translate("MainWindow", "高应力区：100~1000 MPa"))
        self.label_2.setText(_translate("MainWindow", "平均变形系数"))
        self.label_3.setText(_translate("MainWindow", "非均变形系数"))
        self.label_6.setText(_translate("MainWindow", "地层倾角类型"))
        self.label_7.setText(_translate("MainWindow", "地层占比"))
        self.label_8.setText(_translate("MainWindow", "地应力分区"))
        self.pushButton_2.setText(_translate("MainWindow", "计算"))
        self.label_15.setText(_translate("MainWindow", "孔隙水压力分区"))
        self.pushButton_3.setText(_translate("MainWindow", "清空"))
        self.pushButton_4.setText(_translate("MainWindow", "下一步"))
        self.label_14.setText(_translate("MainWindow", "孔隙水压力分区"))
        self.label.setText(_translate("MainWindow", "拱顶"))
        self.label_9.setText(_translate("MainWindow", "左拱肩"))
        self.label_16.setText(_translate("MainWindow", "右拱肩"))
        self.label_12.setText(_translate("MainWindow", "右拱腰"))
        self.label_13.setText(_translate("MainWindow", "左边墙"))
        self.label_11.setText(_translate("MainWindow", "右边墙"))
        self.label_10.setText(_translate("MainWindow", "左拱腰"))
        self.label_4.setText(_translate("MainWindow", "分段变形系数"))
        self.label_5.setText(_translate("MainWindow", "异常变形系数"))
        self.label_17.setText(_translate("MainWindow", "监控量测数据"))
        self.label_18.setText(_translate("MainWindow", "拱顶"))
        self.label_19.setText(_translate("MainWindow", "左拱肩"))
        self.label_20.setText(_translate("MainWindow", "左拱腰"))
        self.label_21.setText(_translate("MainWindow", "右边墙"))
        self.label_22.setText(_translate("MainWindow", "右拱肩"))
        self.label_23.setText(_translate("MainWindow", "右拱腰"))
        self.label_31.setText(_translate("MainWindow", "左边墙"))
        self.label_32.setText(_translate("MainWindow", "隧道尺寸"))
        self.label_33.setText(_translate("MainWindow", "隧道高度"))
        self.label_34.setText(_translate("MainWindow", "隧道跨度"))
        self.label_35.setText(_translate("MainWindow", "单位/m"))
        self.label_37.setText(_translate("MainWindow", "监测位置"))
        self.label_36.setText(_translate("MainWindow", "单位/cm"))