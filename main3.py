import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Пример сигналов и слотов")
        self.setGeometry(100, 100, 300, 200)

        # Создаем метку и кнопку
        self.label = QLabel("Нажмите кнопку", self)
        self.button = QPushButton("Нажать меня", self)

        # Добавляем стиль с помощью CSS
        self.label.setStyleSheet("font-size: 20px; color: blue;")
        self.button.setStyleSheet("background-color: lightgreen; font-size: 15px;")

        # Создаем вертикальный layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        # Устанавливаем layout для окна
        self.setLayout(layout)

        # Связываем сигнал clicked с функцией обновления метки
        self.button.clicked.connect(self.update_label_text)
        self.button.clicked.connect(self.change_styles)

    def update_label_text(self):
        """Функция для изменения текста метки при нажатии на кнопку"""
        self.label.setText("Кнопка нажата!")

    def change_styles(self):
        """Функция для динамического изменения стилей кнопки и метки"""
        # Изменяем стиль метки
        self.label.setStyleSheet("font-size: 20px; color: red; font-weight: bold;")
        # Изменяем стиль кнопки
        self.button.setStyleSheet("background-color: lightblue; font-size: 18px; color: darkblue;")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Создаем окно
    window = MyWindow()
    window.show()

    # Запускаем приложение
    sys.exit(app.exec_())
