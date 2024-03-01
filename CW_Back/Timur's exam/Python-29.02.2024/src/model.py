from wiktionary import Wiktionary

class AbcModel:
    def __init__(self):
        self.used_words = set()
        self.wiktionary = Wiktionary('ru')  # Предположим, что используется русский язык

    def is_used(self, word):
        """
        Проверяет, использовалось ли слово ранее.
        """
        return word in self.used_words

    def add(self, word):
        """
        Добавляет слово в список использованных.
        """
        self.used_words.add(word)

    def is_word_valid(self, word):
        """
        Проверяет, является ли слово допустимым.
        """
        return self.wiktionary.is_exists(word)
