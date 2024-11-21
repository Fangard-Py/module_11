from PIL import Image, ImageFilter

'''
Библиотеки: request, pandas, pillow
'''

'''
Pillow 
1)Импортируем необходимые модули: Image для работы с изображениями и ImageFilter для применения эффектов.
2)Открываем изображение: Замените 'photo.jpg' на путь к Вашему изображению.
3)Изменение размера: Метод resize изменяет размер изображения на новый указанный.
4)Применение эффекта: Метод filter применяет эффект размытия.
5)Сохранение в другом формате: Сохраняем обработанное изображение в формате PNG.

'''

image_path = 'photo.jpg'
image = Image.open(image_path)
# Изменяем размер
new_size = (360, 360)
resized_image = image.resize(new_size)
# Применяем эффект
blurred_image = resized_image.filter(ImageFilter.BLUR)
# Сохраняем в другом формате
output_path = 'photo.png'
blurred_image.save(output_path, format='PNG')
print('Изображение успешно обработано!')

'''
Pandas
'''
import pandas as pd

# Считываем данные из файла
df = pd.read_csv('data.txt')

# Выполняем простой анализ
mean_value = df['Value'].mean()
sum_value = df['Value'].sum()

# Выводим результаты в консоль
print("Анализ данных:")
print(f"Среднее значение: {mean_value}")
print(f"Сумма значений: {sum_value}")

'''
Request
'''
import requests

# URL, с которого мы хотим получить данные
url = 'https://genius.com'

# Отправляем GET-запрос
response = requests.get(url)

# Проверяем код ответа
if response.status_code == 200:
    # Выводим текстовую часть ответа
    print(response.text)
else:
    print(f'Ошибка при запросе: {response.status_code}')
