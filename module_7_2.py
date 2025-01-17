def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for index, string in enumerate(strings, start=1):
            position = file.tell()  # Получаем текущую позицию байта перед записью строки
            file.write(string + '\n')  # Записываем строку и перенос строки
            strings_positions[(index, position)] = string  # Заполняем словарь

    return strings_positions


# Пример использования функции
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
