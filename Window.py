'''
窗口控件
'''

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.Qt import QUrl

import __init__ as init


class Window(QWidget):
    title_name = init.窗口标题
    url = init.url地址

    def __init__(self):
        super().__init__()

        # 获取屏幕分辩率
        self.desktop = QApplication.desktop()
        self.width = self.desktop.screenGeometry().width()
        self.height = self.desktop.screenGeometry().height()

        # 设置窗口
        self.setWindowTitle(self.title_name)
        self.resize(self.width, self.height)
        self.setMinimumSize(init.最小宽度, init.最小高度)

        # 设置web控件
        self.web = QWebEngineView(self)
        self.web.resize(self.width, self.height)
        self.web.load(QUrl(self.url))

    def resizeEvent(self, event):
        '''监听窗口尺寸
        当窗口尺寸变化时, 就会触发此方法
        Agrs:
            event: PyQt5.QtGui.QResizeEvent object
        '''
        self.width = event.size().width()
        self.height = event.size().height()

        self.web.resize(self.width, self.height)
