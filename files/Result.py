from PyQt5.QtWidgets import QWidget, QTextBrowser
from PyQt5 import uic


class ResultScreen(QWidget):
    def __init__(self):
        super(ResultScreen, self).__init__()
        uic.loadUi('qt designer//Result.ui', self)

        # QTextBrowser
        self.tb_name = self.findChild(QTextBrowser, 'textBrowser')
        self.tb_shelf_life = self.findChild(QTextBrowser, 'textBrowser_2')

    def populating_data(self, name, shelf_life):
        self.tb_name.setText(name)
        self.tb_shelf_life.setText(shelf_life)
