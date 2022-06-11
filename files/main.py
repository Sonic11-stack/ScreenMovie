import sys

from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets

import Loading
import Movie
import Result


class MainWindow(QtWidgets.QStackedWidget):
    def __init__(self):
        super().__init__()

        # window size
        self.setFixedWidth(800)
        self.setFixedHeight(600)

        # class instances
        self.movie_screen = Movie.MovieScreen()
        self.loading_screen = Loading.LoadingScreen()
        self.result_screen = Result.ResultScreen()

        # adding widgets
        self.addWidget(self.movie_screen)
        self.addWidget(self.loading_screen)
        self.addWidget(self.result_screen)

        # connect buttons with methods for changing indexes
        self.goto_movie()

        self.movie_screen.pushButton.clicked.connect(self.goto_loading)
        self.result_screen.pushButton.clicked.connect(self.goto_movie)

        # window switching methods

    def goto_movie(self):
        self.setCurrentIndex(self.indexOf(self.movie_screen))

        # show object
        self.movie_screen.pushButton_2.show()

        # hide object
        self.movie_screen.label_3.clear()

    def goto_loading(self):
        self.setCurrentIndex(self.indexOf(self.loading_screen))
        self.repaint()

        # def start
        self.loading_screen.process(self.movie_screen.path_to_img)
        self.goto_result()

    def goto_result(self):
        self.setCurrentIndex(self.indexOf(self.result_screen))

        # hide object
        self.result_screen.textBrowser.clear()
        self.result_screen.textBrowser_2.clear()

        # def start
        self.result_screen.populating_data(self.loading_screen.answer_name, self.loading_screen.answer_data)


def main():
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    try:
        app.exec_()
        # sys.exit(app_exec())
    except Exception as ex:
        print(ex)
        print("ERROR")


if __name__ == '__main__':
    main()
