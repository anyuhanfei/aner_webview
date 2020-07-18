'''
窗口控件
'''

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.Qt import QUrl
from PyQt5.QtNetwork import QNetworkCookie

import __init__ as init


class Browser(QWebEngineView):
    '''自定义web控件
    '''
    def __init__(self, *argv, **kwargv):
        super().__init__(*argv, **kwargv)

    def SetCookie(self, cookie_dict, url):
        '''将Cookie设置到站点中
        '''
        self.my_cookie = QNetworkCookie()

        for key, value in cookie_dict.items():
            self.my_cookie.setName(key.encode())
            self.my_cookie.setValue(value.encode())
            self.my_cookie.setDomain(url)
            self.page().profile().cookieStore().setCookie(self.my_cookie)


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
        self.setWindowTitle('{title_name}--{url}'.format(title_name=self.title_name, url=self.url))
        self.move(self.width * 0.05, self.height * 0.03)
        self.resize(self.width * 0.9, self.height * 0.87)
        self.setMinimumSize(init.最小宽度, init.最小高度)

        # 设置web控件
        self.web = Browser(self)
        self.web.SetCookie({'SameSite': 'None'}, self.url)
        self.web.resize(self.width * 0.9, self.height * 0.87)
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
