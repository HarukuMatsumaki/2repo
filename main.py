import sys
from random import randint

from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor


UIC_FILE_PATH = 'UI.ui'
CIRCLE_COLOR = 'yellow'
MIN_RADIUS = 10
MAX_RADIUS = 100
MIN_CIRCLES_QUANTITY = 2
MAX_CIRCLES_QUANTITY = 10


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(UIC_FILE_PATH, self)
        self.initUi()

    def initUi(self):
        self.do_paint = False
        self.drawCircleBtn.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.drawCircle(qp)
            qp.end()

    def drawCircle(self, qp: QPainter):
        qp.setPen(QColor(CIRCLE_COLOR))
        qp.setBrush(QColor(CIRCLE_COLOR))

        for i in range(
                randint(MIN_CIRCLES_QUANTITY, MAX_CIRCLES_QUANTITY)):
            x, y = self.canvas.width(), self.canvas.height()
            radius = randint(MIN_RADIUS, MAX_RADIUS)
            qp.drawEllipse(randint(0, x - radius), randint(0, y - radius),
                           radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
