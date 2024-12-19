import sys
from PyQt5.QtCore import Qt, QUrl, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QSlider, QLabel, QVBoxLayout, QWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget

class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Минималистичный видеоплеер")
        self.setGeometry(100, 100, 800, 600)

        # Инициализация медиаплеера
        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        
        # Виджет для отображения видео
        self.video_widget = QVideoWidget()

        # Настройка вывода видео
        self.media_player.setVideoOutput(self.video_widget)

        # Кнопки управления
        self.play_button = QPushButton("Воспроизвести")
        self.pause_button = QPushButton("Пауза")
        self.stop_button = QPushButton("Остановить")
        self.volume_slider = QSlider(Qt.Horizontal)
        self.time_slider = QSlider(Qt.Horizontal)
        self.file_path_label = QLabel("Путь к файлу: ")

        # Соединение кнопок с функциями
        self.play_button.clicked.connect(self.play_video)
        self.pause_button.clicked.connect(self.pause_video)
        self.stop_button.clicked.connect(self.stop_video)
        self.volume_slider.valueChanged.connect(self.change_volume)
        self.time_slider.sliderMoved.connect(self.seek_video)

        # Кнопка для открытия файла
        self.open_file_button = QPushButton("Открыть файл")
        self.open_file_button.clicked.connect(self.open_file)

        # Подключение сигналов для обновления позиции и длительности видео
        self.media_player.positionChanged.connect(self.update_position)
        self.media_player.durationChanged.connect(self.update_duration)

        # Подключение сигнала изменения состояния медиаплеера
        self.media_player.mediaStatusChanged.connect(self.handle_media_status)

        # Создание макета
        layout = QVBoxLayout()
        layout.addWidget(self.open_file_button)
        layout.addWidget(self.file_path_label)
        layout.addWidget(self.video_widget)
        layout.addWidget(self.play_button)
        layout.addWidget(self.pause_button)
        layout.addWidget(self.stop_button)
        layout.addWidget(self.volume_slider)
        layout.addWidget(self.time_slider)

        # Контейнер для виджетов
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Таймер для обновления времени
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_position)
        self.timer.start(100)

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Выберите видеофайл", "", "Видео файлы (*.mp4 *.avi *.mov *.mkv)")
        if file_name:
            self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_name)))
            self.file_path_label.setText(f"Путь к файлу: {file_name}")
            self.play_button.setEnabled(True)

    def play_video(self):
        self.media_player.play()
        self.play_button.setEnabled(False)
        self.pause_button.setEnabled(True)
        self.stop_button.setEnabled(True)

    def pause_video(self):
        self.media_player.pause()
        self.play_button.setEnabled(True)
        self.pause_button.setEnabled(False)
        self.stop_button.setEnabled(True)

    def stop_video(self):
        self.media_player.stop()
        self.play_button.setEnabled(True)
        self.pause_button.setEnabled(False)
        self.stop_button.setEnabled(False)

    def change_volume(self):
        volume = self.volume_slider.value()
        self.media_player.setVolume(volume)

    def seek_video(self):
        position = self.time_slider.value()
        self.media_player.setPosition(position)

    def update_position(self):
        position = self.media_player.position()
        self.time_slider.setValue(position)

    def update_duration(self):
        duration = self.media_player.duration()
        self.time_slider.setRange(0, duration)

    def handle_media_status(self, status):
        if status == QMediaPlayer.InvalidMedia:
            print("Ошибка: Неверный или неподдерживаемый формат файла.")
        elif status == QMediaPlayer.NoMedia:
            print("Ошибка: Нет медиа.")
        elif status == QMediaPlayer.LoadingMedia:
            print("Загрузка файла...")
        elif status == QMediaPlayer.PlayingMedia:
            print("Воспроизведение...")
        elif status == QMediaPlayer.PausedMedia:
            print("Пауза.")
        elif status == QMediaPlayer.StoppedMedia:
            print("Остановлено.")
        
        # Можно также проверить строку ошибки
        error_string = self.media_player.errorString()
        if error_string:
            print(f"Ошибка воспроизведения: {error_string}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.show()
    sys.exit(app.exec_())
