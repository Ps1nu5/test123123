# file_size = int(input('Введите размер файла: '))
# speed = int(input('Введите скорость загрузки(бит/c): '))
#
# file_size_bit = file_size * 1024 * 1024 * 1024 * 8
#
# download_time = file_size_bit / speed
#
# choice = input('Выберите единицу измерения [с / м / ч]: ')
#
# if choice == 'с':
#     print(f'Время скачивания файла: {download_time}c')
# elif choice == 'м':
#     print(f'Время скачивания файла: {download_time//60}м')
# elif choice == 'ч':
#     print(f'Время скачивания файла: {download_time // 3600}ч')
# else:
#     print('Некорректный выбор!')

# points = 0
# print('Кто создатель ЯП Python?')
# answer = input('Ваш ответ: ')
#
# if answer.lower() == 'гвидо ван россум':
#     print('Верно!')
#     points += 10
# else:
#     print('Неверно!')
#     points -= 5
#
# if points >= 45:
#     print('Отлично!')
# elif 35 <= points < 45:
#     print('Хорошо')


hour = int(input('Введите часы: '))
minute = int(input('Введите минуты: '))
difference = int(input('Введите разницу: '))

new_hour = hour + difference

if new_hour > 24:
    new_hour -= 24
if new_hour < 0:
    new_hour += 24

print(f'{new_hour}:{minute}')






