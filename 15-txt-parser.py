# Разработка парсера файла task.txt для сборки маршрута для Jetbot_MIREA
# Используем Python для создания простого и гибкого парсера

def parse_task_file(file_path):
    try:
        with open(file_path, 'r') as file:
            # Чтение всех строк из файла
            lines = file.readlines()
            
            # Список для хранения значений кодов, которые необходимо искать на полигоне
            target_codes = []
            
            for line in lines:
                # Пропускаем пустые строки и строки с комментариями (начинающиеся с #)
                if line.strip() and not line.startswith('#'):
                    try:
                        # Разделение строки на номер и название товара
                        parts = line.strip().split('. ', 1)
                        if len(parts) == 2:
                            target_codes.append(parts[1].strip())
                    except ValueError:
                        print(f"Неверный формат строки: {line.strip()} - пропускается")
            
            return target_codes
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return []

if __name__ == "__main__":
    # Путь к файлу task.txt
    file_path = "tasks.txt"
    
    # Парсинг файла и получение списка значений кодов
    target_codes = parse_task_file(file_path)
    
    # Вывод значений кодов в правильном порядке
    if target_codes:
        print("Целевые коды для поиска на полигоне:")
        for code in target_codes:
            print(code)
    else:
        print("Не удалось найти целевые коды.")
