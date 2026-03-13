import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        # Загружаем дизайн из файла
        uic.loadUi('UI.ui', self)

        # Список для хранения данных о кругах (x, y, диаметр)
        self.circles = []

        # Подключаем кнопку
        self.pushButton.clicked.connect(self.add_circle)

    def add_circle(self):
        # Генерируем случайный диаметр и координаты
        d = random.randint(20, 100)
        x = random.randint(0, self.width() - d)
        y = random.randint(50, self.height() - d)  # Начинаем чуть ниже кнопки

        # Сохраняем и обновляем окно
        self.circles.append((x, y, d))
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_circles(qp)
        qp.end()

    def draw_circles(self, qp):
        # Устанавливаем желтый цвет заливки
        qp.setBrush(QColor(255, 255, 0))
        for x, y, d in self.circles:
            qp.drawEllipse(x, y, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())