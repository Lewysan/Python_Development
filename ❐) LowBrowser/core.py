#  _                  ____
# | |    _____      _| __ ) _ __ _____      _____  ___ _ __
# | |   / _ \ \ /\ / /  _ \| '__/ _ \ \ /\ / / __|/ _ \ '__|
# | |__| (_) \ V  V /| |_) | | | (_) \ V  V /\__ \  __/ |
# |_____\___/ \_/\_/ |____/|_|  \___/ \_/\_/ |___/\___|_|

import sys
import utilities
# import requests

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

from PyQt5.QtGui import QPixmap

PaginaInicio = "https://google.it"

class browser(QMainWindow):
    def __init__(self):
        super(browser, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(PaginaInicio))
        self.setCentralWidget(self.browser)
        print('------------------------------')
        print(' ')
        print('L O W - B R O W S E R ')
        print('Browser version: '+utilities.LBversion())
        print('Developed by: '+utilities.getDeveloper())
        print(' ')
        print('------------------------------')
        self.show()
        self.showMaximized()

        # BARRA DE NAVERGACION

        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('<-', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('->', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('RELOAD', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('HUB', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://google.com/'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

app = QApplication(sys.argv)

screen = app.primaryScreen()
size = screen.size()
rect = screen.availableGeometry()

QApplication.setApplicationName('LowBrowser')
window = browser()
app.exec_()
#  ____  _       _ _            ____                        _
# / ___|| |_ ___| | | __ _ _ __/ ___|  __ _ _   _  __ _  __| |
# \___ \| __/ _ \ | |/ _` | '__\___ \ / _` | | | |/ _` |/ _` |
#  ___) | ||  __/ | | (_| | |   ___) | (_| | |_| | (_| | (_| |
# |____/ \__\___|_|_|\__,_|_|  |____/ \__, |\__,_|\__,_|\__,_|
#                                        |_|
