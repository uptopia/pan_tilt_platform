from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import time
import sys
import ui2 as ui


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui_test = ui.Ui_MainWindow()
    ui_test.setupUi(MainWindow) #initial
    # ui_test.reset()

    degree_l = -50
    degree_r = 50
    flag = True # -> l->r
    p_l, p_r = degree_l, degree_r
    p_l, p_r = ui_test.degree2rev(p_l), ui_test.degree2rev(p_r)
    p_l, p_r = ui_test.l_p(p_l), ui_test.l_p(p_r)
    while(1):
        if(flag):
            ui_test.cmd("pp{}".format(p_l))
            if(ui_test.cmd("pp")[-1] == p_l):
                time.sleep(0.5)
                flag = False

        else:
            ui_test.cmd("pp{}".format(p_r))
            if(ui_test.cmd("pp")[-1] == p_r):
                time.sleep(0.5)
                flag = True