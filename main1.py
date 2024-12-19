import os

def ensure_directory_exists(directory_path):
    # Проверяем, существует ли каталог
    if not os.path.exists(directory_path):
        # Если не существует, создаем каталог
        os.makedirs(directory_path)
        print(f"Каталог '{directory_path}' был успешно создан.")
    else:
        print(f"Каталог '{directory_path}' уже существует.")

# Пример использования с путем 'D:\Пример'
directory_path = r'D:\Пример2\Пример'  # Путь к каталогу
ensure_directory_exists(directory_path)
