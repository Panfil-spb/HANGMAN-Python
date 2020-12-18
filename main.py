import random

def hello():
    print("""
                        Привет, это игра Висилица.
            Суть игры - это отгадывать слово по буква, количевство попыток ограничено.
              С каждым неверным выбором буквы, появляется новый рисунок повешенного.
                                Приятной игры!
    ______________________________________________________________________________________________
                        Hello, this is Hangman game.
        The essence of the game is to guess a word letter by letter, the number of attempts is limited.
                With each wrong letter choice, a new drawing of the hanged man appears.
                            Have a nice game!""")

def choiseWord():
    words = ["висилица", "постамент", "веревка", "человек"]
    return random.choice(words)

def hangmanView(i):
    hangman = [""" 
                   +---+
                       |
                       |
                       |
                      ===""",
               """
                   +---+
                   0   |
                       |
                       |
                      ===""",
               """
                    +---+
                    0   |
                    |   |
                        |
                       ===""",
               """
                   +---+
                   0   |
                  /|   |
                       |
                      ===""",
               """
                    +---+
                    0   |
                   /|\  |
                        |
                       ===""",
               """
                    +---+
                    0   |
                   /|\  |
                   /    |
                       ===""",
               """
                   +---+
                   0   |
                  /|\  |
                  / \  |
                      ==="""]
    print(hangman[i])

def showWord(used, word):
    wordGame = ""
    for i in range(len(word)):
        if word[i] in used:
            wordGame += word[i]
        else:
            wordGame += "-"
    return wordGame

def checkWon(used, word):
    if '-' not in showWord(used, word):
        return 1
    else:
        return 0

def game(word):
    wrong = 0
    used = []
    alphabet = "йцукенгшщзхъфывапролджэячсмитьбю"
    while wrong != 6:
        hangmanView(wrong)
        gameWord = showWord(used, word)

        print(gameWord)
        while 1:
            userLitter = input("Введите букву которую хотите проверить: ")
            if userLitter.lower() in used:
                print("Введите букву которую вы ещё не вводили!")
            elif userLitter.lower() not in alphabet:
                print("Введите букву русскаого алфавита!")
            else:
                used.append(userLitter.lower())
                if userLitter.lower() not in word:
                    wrong += 1
                break
        check = checkWon(used, word)
        if check == 1:
            break
    if check == 1:
        print("Поздравляю, вы победили!"
              "\nВы отгадали слово '" + word + "'!")
    if wrong == 6:
        hangmanView(wrong)
        print("К сожалению, вы проиграли!"
              "\nСлово, которое вы не отгадали '" + word + "'!")

def main():
    hello()
    word = choiseWord()
    game(word)

main()