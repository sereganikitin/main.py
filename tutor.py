try:
    raise IndexError
except IndexError:
    print('Получаем исключение')
else:
    print('Лови его')