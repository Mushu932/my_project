import random

MENU = """
1. Начать игру
2. Добавить слова
3. Редактировать слова
4. Удалить слова
5. Вывести слова
6. Выход
"""

def play_game(words):
    """Запускает игровой режим. Принимает словарь words."""
    if not words:
        print("Словарь пуст. Сначала добавьте слова (пункт 2).")
        return

    score = 0
    stop = False
    print('Для выхода введите "/меню"')

    while not stop:
        attempts = 3
        word = random.choice(list(words))
        translation = words[word]

        while attempts != 0:
            answer = input(f"Введите перевод {word}: ")
            if answer == "/меню":
                print(f"Ваш счёт: {score}")
                stop = True
                break
            if answer == translation:
                score += 1
                print("Верно!")
                break
            else:
                attempts -= 1
                print("Неверно, попробуй снова")

        if attempts == 0:
            print(f"Правильный ответ: {translation}")

def add_words(words):
    """Добавляет слова. Принимает и возвращает словарь words."""
    print('Для выхода введите "/меню"')
    while True:
        word = input("Введите слово: ")
        if word == "/меню":
            break
        if word in words:
            print("Такое слово уже есть в словаре.")
            continue
        translation = input("Введите перевод: ")
        if translation == "/меню":
            break
        words[word] = translation
        print(f"Слово '{word}' добавлено.")
    return words

def edit_words(words):
    """Редактирует слова. Принимает и возвращает словарь words."""
    if not words:
        print("Словарь пуст. Сначала добавьте слова.")
        return words

    word = input("Введите слово, которое хотите изменить: ")
    if word not in words:
        print("Такого слова нет в словаре.")
        return words

    print(f"Текущее слово: {word} -> {words[word]}")
    new_word = input("Введите новое слово (или нажмите Enter, чтобы оставить прежним): ").strip()
    new_translation = input("Введите новый перевод (или нажмите Enter, чтобы оставить прежним): ").strip()

    final_word = new_word if new_word else word
    final_translation = new_translation if new_translation else words[word]

    # Удаляем старое слово и добавляем новое (с поддержкой смены самого слова)
    if final_word != word:
        del words[word]
    words[final_word] = final_translation
    print("Изменения сохранены.")
    return words

def delete_words(words):
    """Удаляет слова. Принимает и возвращает словарь words."""
    if not words:
        print("Словарь пуст. Сначала добавьте слова.")
        return words

    word = input("Введите слово, которое хотите удалить: ")
    if word in words:
        del words[word]
        print(f"Слово '{word}' удалено.")
    else:
        print("Такого слова нет в словаре.")
    return words

def show_words(words):
    """Выводит все слова в формате слово -> перевод."""
    if not words:
        print("Сохранённых слов пока нет.")
        return
    for word, translation in words.items():
        print(f"{word} -> {translation}")

def main():
    """Основной цикл программы — меню и вызов функций."""
    words = {}
    while True:
        print("Приветствуем в игре Anki! Что хотите сделать?")
        print(MENU)
        action = input("Выберите пункт меню: ")

        if action == "1":
            play_game(words)
        elif action == "2":
            words = add_words(words)
        elif action == "3":
            words = edit_words(words)
        elif action == "4":
            words = delete_words(words)
        elif action == "5":
            show_words(words)
        elif action == "6":
            print("До свидания!")
            break
        else:
            print("Неизвестный пункт меню")

if __name__ == "__main__":
    main()