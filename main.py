import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
from random import randint
from PyQt6.QtGui import QPainter, QColor


class Painting_circles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_btn.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw_circle()
            self.qp.end()

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_circle(self):
        radius = randint(1, 600)
        self.qp.setBrush(QColor(255, 255, 0))
        self.qp.drawEllipse(int(randint(1, 800) - radius / 2), int(randint(1, 600) - radius / 2), radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Painting_circles()
    ex.show()
    sys.exit(app.exec())
