import main
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

def aaaa():
    print('aaa')
class MainWindow(object):
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = main.Ui_Form()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
    MainWindow()
    