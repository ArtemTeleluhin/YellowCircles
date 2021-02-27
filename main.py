import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QPoint
from random import randint
from UI import Ui_Form

N = 5


class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

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
        for _ in range(N):
            qp.setPen(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
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
