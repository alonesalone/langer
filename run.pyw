import sys
from PyQt5 import QtWidgets
from langer import LangerProgram

def RUN_APP():
    app = QtWidgets.QApplication(sys.argv)
    run = LangerProgram()
    run.show()
    sys.exit(app.exec_())

RUN_APP()
