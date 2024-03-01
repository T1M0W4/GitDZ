class AbcView:
    def show(self, message):
        """
        Отображает любой текст.
        """
        print(message)

    def show_word(self, word):
        """
        Отображает слово, названное оппонентом.
        """
        print(f"Opponent's word: {word}")

    def show_win(self):
        """
        Отображает сообщение о выигрыше.
        """
        print("You win!")

    def show_loose(self):
        """
        Отображает сообщение о проигрыше.
        """
        print("You lose!")

    def show_mistake(self, last_letter, attempts_left):
        """
        Отображает сообщение о том, что слово не подходит,
        и оно должно начинаться на другую букву.
        """
        print(f"Invalid word. Should start with '{last_letter}'. Attempts left: {attempts_left}")

    def show_used(self, attempts_left):
        """
        Отображает сообщение о том, что слово уже использовалось.
        """
        print(f"Word has already been used. Attempts left: {attempts_left}")

    def show_unknown(self):
        """
        Отображает сообщение о том, что такого слова не существует.
        """
        print("Unknown word.")

    def ask_word(self):
        """
        Запрашивает слово у пользователя.
        """
        return input("Enter a word: ")
