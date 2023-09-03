# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(405, 184)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 361, 91))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.slider_pan = QtWidgets.QSlider(self.gridLayoutWidget)
        self.slider_pan.setMaximum(2000)
        self.slider_pan.setProperty("value", 1000)
        self.slider_pan.setOrientation(QtCore.Qt.Horizontal)
        self.slider_pan.setObjectName("slider_pan")
        self.gridLayout.addWidget(self.slider_pan, 1, 2, 1, 1)
        self.tilt_degree = QtWidgets.QLabel(self.gridLayoutWidget)
        self.tilt_degree.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tilt_degree.setAlignment(QtCore.Qt.AlignCenter)
        self.tilt_degree.setObjectName("tilt_degree")
        self.gridLayout.addWidget(self.tilt_degree, 2, 1, 1, 1)
        self.label2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label2")
        self.gridLayout.addWidget(self.label2, 0, 1, 1, 1)
        self.label1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label1")
        self.gridLayout.addWidget(self.label1, 0, 0, 1, 1)
        self.tilt = QtWidgets.QLabel(self.gridLayoutWidget)
        self.tilt.setAlignment(QtCore.Qt.AlignCenter)
        self.tilt.setObjectName("tilt")
        self.gridLayout.addWidget(self.tilt, 2, 0, 1, 1)
        self.pan = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pan.setAlignment(QtCore.Qt.AlignCenter)
        self.pan.setObjectName("pan")
        self.gridLayout.addWidget(self.pan, 1, 0, 1, 1)
        self.pan_degree = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pan_degree.setAlignment(QtCore.Qt.AlignCenter)
        self.pan_degree.setObjectName("pan_degree")
        self.gridLayout.addWidget(self.pan_degree, 1, 1, 1, 1)
        self.slider_tilt = QtWidgets.QSlider(self.gridLayoutWidget)
        self.slider_tilt.setMaximum(2000)
        self.slider_tilt.setProperty("value", 1000)
        self.slider_tilt.setOrientation(QtCore.Qt.Horizontal)
        self.slider_tilt.setObjectName("slider_tilt")
        self.gridLayout.addWidget(self.slider_tilt, 2, 2, 1, 1)
        self.label3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setObjectName("label3")
        self.gridLayout.addWidget(self.label3, 0, 2, 1, 1)
        self.line_tilt = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.line_tilt.setAlignment(QtCore.Qt.AlignCenter)
        self.line_tilt.setObjectName("line_tilt")
        self.gridLayout.addWidget(self.line_tilt, 2, 3, 1, 1)
        self.line_pan = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.line_pan.setEnabled(True)
        self.line_pan.setTabletTracking(False)
        self.line_pan.setMaxLength(32767)
        self.line_pan.setAlignment(QtCore.Qt.AlignCenter)
        self.line_pan.setObjectName("line_pan")
        self.gridLayout.addWidget(self.line_pan, 1, 3, 1, 1)
        self.label4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label4.setAlignment(QtCore.Qt.AlignCenter)
        self.label4.setObjectName("label4")
        self.gridLayout.addWidget(self.label4, 0, 3, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(130, 110, 164, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_reset = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_reset.setObjectName("button_reset")
        self.horizontalLayout.addWidget(self.button_reset)
        self.button_ok = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_ok.setObjectName("button_ok")
        self.horizontalLayout.addWidget(self.button_ok)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 405, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.init_serial()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def rev2degree(self, rev):
        rev = int(rev)
        degree = rev*90/1750
        return degree
    
    def degree2rev(self, degree):
        degree = float(degree)
        rev = round(degree*1750/90)
        return str(rev)

    def l_p(self,p):
        if int(p)>=int(self.p_nx[1]):
            p = int(self.p_nx[1])
        if int(p)<=int(self.p_nx[0]):
            p = int(self.p_nx[0])
        return p
    
    def l_t(self,t):
        if int(t)>=int(self.t_nx[1]):
            t = int(self.t_nx[1])
        if int(t)<=int(self.t_nx[0]):
            t = int(self.t_nx[0])
        return t

    def cmd(self, s, delay_s = 0.1):
        ss = "{} \r\n".format(s)
        ss = ss.encode()
        self.ser.write(ss)
        time.sleep(delay_s)
        return self.ser.readline().decode().strip("\r\n").split(" ")

    def init_serial(self):
        print("Initial serial...")
        self.ser = serial.Serial("/dev/ttyUSB0", 9600)
        self.cmd("ps700")
        self.cmd("ts500")
        print("Done!")
       
        print("Current Position...")
        self.pp = self.cmd("pp")[-1]
        self.tp = self.cmd("tp")[-1]
        self.pp = self.rev2degree(self.pp)
        self.tp = self.rev2degree(self.tp)
        print("Done!")

        print("Get limits of ptu46...") # the limits of pp and tp
        self.p_nx = [self.cmd("pn")[-1], self.cmd("px")[-1]]
        self.t_nx = [self.cmd("tn")[-1], self.cmd("tx")[-1]]
        print("The limits of  pan position: ",self.p_nx)
        print("The limits of tilt position: ",self.t_nx)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pan_degree.setText(_translate("MainWindow", "{:3.2f}".format(self.pp)))
        self.tilt_degree.setText(_translate("MainWindow", "{:3.2f}".format(self.tp)))
        self.label2.setText(_translate("MainWindow", "角度"))
        self.label1.setText(_translate("MainWindow", "方向"))
        self.tilt.setText(_translate("MainWindow", "Tilt"))
        self.pan.setText(_translate("MainWindow", "Pan"))
        
        self.label3.setText(_translate("MainWindow", "控制條"))
        self.line_pan.setText(_translate("MainWindow", "{:3.2f}".format(self.pp)))
        self.line_tilt.setText(_translate("MainWindow", "{:3.2f}".format(self.tp)))
        self.label4.setText(_translate("MainWindow", "指定角度"))
        self.button_reset.setText(_translate("MainWindow", "Reset"))
        self.button_ok.setText(_translate("MainWindow", "OK"))


        self.button_ok.clicked.connect(self.ok)
        self.button_reset.clicked.connect(self.reset)
        self.slider_pan.valueChanged.connect(self.slider_pan_c)
        self.slider_tilt.valueChanged.connect(self.slider_tilt_c)

    def ok(self):
        # self.pan_degree.setText(self.line_pan.text())
        # self.tilt_degree.setText(self.line_tilt.text())

        p = self.line_pan.text()
        t = self.line_tilt.text()

        p = self.degree2rev(p)
        t = self.degree2rev(t)

        p = self.l_p(p)
        t = self.l_t(t)

        self.pan_degree.setText("{:3.2f}".format(self.rev2degree(p)))
        self.tilt_degree.setText("{:3.2f}".format(self.rev2degree(t)))

        self.cmd("pp{}".format(p))
        self.cmd("tp{}".format(t))


    def reset(self):
        # self.ser.write(b"r * \r\n")
        print("Reset...")
        self.pan_degree.setText("{:3.2f}".format(0))
        self.tilt_degree.setText("{:3.2f}".format(0))
        self.line_pan.setText("{:3.2f}".format(0))
        self.line_tilt.setText("{:3.2f}".format(0))
        self.cmd("r")
        print("Done!")

    def slider_pan_c(self):
        pass

    def slider_tilt_c(self):
        pass



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
