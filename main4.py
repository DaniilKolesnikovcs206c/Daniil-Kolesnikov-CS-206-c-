import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QTextEdit, QFileDialog, QVBoxLayout, QWidget

class NoteApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Инициализация главного окна
        self.setWindowTitle('Приложение для заметок')
        self.setGeometry(100, 100, 600, 400)
        
        # Создание текста для заметки
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)
        
        # Создание меню
        self.menu_bar = self.menuBar()
        self.file_menu = self.menu_bar.addMenu('Файл')
        
        # Добавляем пункты меню
        new_note_action = QAction('Новая заметка', self)
        new_note_action.triggered.connect(self.create_new_note)
        
        save_note_action = QAction('Сохранить заметку', self)
        save_note_action.triggered.connect(self.save_note)
        
        self.file_menu.addAction(new_note_action)
        self.file_menu.addAction(save_note_action)
        
    def create_new_note(self):
        """Создание нового окна с текстовым редактором для заметки."""
        self.text_edit.clear()  # Очистка текущего текста

    def save_note(self):
        """Сохранение заметки в файл."""
        file_name, _ = QFileDialog.getSaveFileName(self, 'Сохранить заметку', '', 'Text Files (*.txt);;All Files (*)')
        
        if file_name:
            try:
                with open(file_name, 'w', encoding='utf-8') as file:
                    file.write(self.text_edit.toPlainText())  # Сохранение текста из QTextEdit
            except Exception as e:
                print(f"Ошибка при сохранении файла: {e}")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # Создание и отображение главного окна
    main_window = NoteApp()
    main_window.show()
    
    # Запуск приложения
    sys.exit(app.exec_())
