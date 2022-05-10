# Программа будет конвертировать строки в морзе-код, а затем проверять ответы пользователя. Все
# это с помощью функций.
from random import choice

# Вводные данные
answers = []
morse_dict = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.",
    "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
    "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
    "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
    "y": "-.--", "z": "--.."
}
eng_words = ['code', 'bit', 'list', 'soul', 'next']
count = 1


def get_word():  # Функция, которая получает случайное слово из списка
    random_word = choice(eng_words)
    eng_words.remove(random_word)
    return random_word


def morse_encode(encode_word):  # Перевод слова в последовательность морзе
    morse_code = ''
    for letter in encode_word:
        if letter in morse_dict:
            morse_code += morse_dict[letter]

    return morse_code


def print_statistics():
    print(f'\nВсего задачек: {count}')
    print(f'Отвечено верно: {answers.count(True)}')
    print(f'Отвечено неверно: {answers.count(False)}')


# Основная программа
print('Сегодня мы потренируемся расшифровывать морзянку. \nНажмите Enter и начнем')
input()

for word in range(0, len(eng_words)):
    word = get_word()
    print(f'Слово {count} >>> {morse_encode(word)}')
    user_input = input('Ваша расшифровка: ')
    if user_input == word:
        print(f'Верно, {word}!')
        count += 1
        answers.append(True)
    else:
        print(f'Неверно, {word}!')
        count += 1
        answers.append(False)

print_statistics()
