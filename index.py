'''
简易的浏览器GUI
'''


import sys

from PyQt5.QtWidgets import QApplication

from Window import Window


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec_())
