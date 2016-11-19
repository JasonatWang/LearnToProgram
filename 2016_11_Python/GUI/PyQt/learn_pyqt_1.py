from PyQt5 import QtWidgets


class FirstApplication(QtWidgets.QWidget):
    def __init__(self):
        super(FirstApplication, self).__init__()

import sys
app = QtWidgets.QApplication(sys.argv)
window = FirstApplication()
label = QtWidgets.QLabel(window)
label.setText("Hello!")

window.show()
sys.exit(app.exec_())