import os
import sys
from PIL import Image


def optimize_images():
    # Запрашиваем у пользователя путь к папке с изображениями
    input_dir = input("Введите путь к папке с изображениями: ")
    
    # Запрашиваем у пользователя максимальную ширину изображений
    max_width = int(input("Введите максимальную ширину изображений: "))
    
    # Запрашиваем у пользователя степень сжатия (качество)
    quality = int(input("Введите степень сжатия (от 1 до 95): "))
    
    # Создаем папку для оптимизированных изображений
    output_dir = os.path.join(input_dir, 'optimized')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Обрабатываем каждое изображение в папке
    for filename in os.listdir(input_dir):
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
            # Получаем путь к файлу
            filepath = os.path.join(input_dir, filename)
            
            # Открываем изображение с помощью библиотеки PIL
            with Image.open(filepath) as image:
                # Получаем размеры изображения
                width, height = image.size
                
                # Определяем новые размеры с сохранением пропорций
                new_width = max_width
                new_height = int(height * max_width / width)
                
                # Масштабируем изображение
                resized_image = image.resize((new_width, new_height))
                
                # Если у изображения есть альфа-канал, сохраняем с сохранением альфа-канала
                if image.mode == 'RGBA':
                    resized_image.save(os.path.join(output_dir, filename), format='PNG', quality=quality, optimize=True)
                else:
                    # Если альфа-канала нет, сохраняем в формате JPEG
                    resized_image.save(os.path.join(output_dir, filename), format='JPEG', quality=quality, optimize=True)

    print("Оптимизация изображений завершена!")


# Вызываем функцию для оптимизации изображений
optimize_images()
