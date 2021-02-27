import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QPoint
from random import randint

N = 5


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.paint = False
        self.pushButton.clicked.connect(self.button_draw)

    def button_draw(self):
        self.paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_squares(qp)
            qp.end()
            self.paint = False

    def draw_squares(self, qp):
        wight = self.size().width()
        height = self.size().height()
        qp.setPen(QColor(220, 220, 0))
        for _ in range(N):
            r = randint(0, min(wight, height) // 2)
            x = randint(0, wight)
            y = randint(0, height)
            qp.drawEllipse(QPoint(x, y), r, r)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
