from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QWidget, QLineEdit
from PyQt5 import uic


class MovieScreen(QWidget):
    def __init__(self):
        super(MovieScreen, self).__init__()
        uic.loadUi('qt designer//Movie.ui', self)

        self.path_to_img = str

        # Button clicked
        self.pushButton_2.clicked.connect(self.getting_data)

        # QLineEdit
        self.le = self.findChild(QLineEdit, 'lineEdit')

    def getting_data(self):
        try:
            image_file = QFileDialog.getOpenFileName(self, 'Open file', 'D:\\',
                                                     'Image files (*.jpg *.gif *.png *.jpeg)')
            self.path_to_img = image_file[0]
            self.label_3.setText(image_file[0])
            # self.pushButton_2.setObjectName()
            self.pushButton_2.hide()
        except:
            pass
