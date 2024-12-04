import sys
import random
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt6.QtGui import QPainter, QColor


class Interface:
    def setup_ui(window):
        window.setGeometry(300, 300, 400, 400)
        window.setWindowTitle('Случайные круги')
        window.btn = QPushButton('Нарисовать круг', window)
        window.btn.move(150, 10)
        window.btn.clicked.connect(window.make_circle)


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        Interface.setup_ui(self)
        self.circle_params = None

    def make_circle(self):
        self.circle_params = {
            'size': random.randint(10, 100),
            'color': QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        }
        self.update()

    def paintEvent(self, event):
        if self.circle_params:
            painter = QPainter(self)
            painter.setBrush(self.circle_params['color'])
            size = self.circle_params['size']
            center_x = self.width() // 2
            center_y = self.height() // 2
            painter.drawEllipse(center_x - size // 2, center_y - size // 2, size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
