import sys
import random
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt6.QtGui import QPainter, QColor


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.circle_params = None  # Параметры круга

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Рисуем круг')
        self.btn = QPushButton('Сделать круг', self)
        self.btn.move(150, 10)
        self.btn.clicked.connect(self.make_circle)

    def make_circle(self):
        self.circle_params = random.randint(10, 100)
        self.update()

    def paintEvent(self, event):
        if self.circle_params:
            painter = QPainter(self)
            painter.setBrush(QColor(255, 255, 0))
            size = self.circle_params
            center_x = self.width() // 2
            center_y = self.height() // 2
            painter.drawEllipse(center_x - size // 2, center_y - size // 2, size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
