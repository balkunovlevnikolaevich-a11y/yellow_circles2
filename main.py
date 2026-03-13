# main.py
import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from UI import Ui_MainWindow  # Импортируем наш новый класс интерфейса


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Инициализируем интерфейс из класса

        # Теперь храним (x, y, d, color)
        self.circles = []
        self.pushButton.clicked.connect(self.add_circle)

    def add_circle(self):
        d = random.randint(20, 100)
        x = random.randint(0, self.width() - d)
        y = random.randint(50, self.height() - d)

        # Генерируем случайный цвет
        color = QColor(random.randint(0, 255),
                       random.randint(0, 255),
                       random.randint(0, 255))

        self.circles.append((x, y, d, color))
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_circles(qp)
        qp.end()

    def draw_circles(self, qp):
        for x, y, d, color in self.circles:
            qp.setBrush(color)
            qp.drawEllipse(x, y, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())