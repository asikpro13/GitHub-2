from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
import sys
import random


class yellow_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.paint()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(Qt.yellow)
            self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        self.do_paint = False
        for i in range(100):
            x = random.randint(0, self.width())
            y = random.randint(0, self.height())
            r = random.randint(0, 150)
            qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = yellow_Window()
    ex.show()
    sys.exit(app.exec_())
