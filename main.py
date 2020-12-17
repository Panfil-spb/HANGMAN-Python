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
                   0    |
                   |    |
                        |
                       ===""",
               """
                   +---+
                   0    |
                  /|    |
                        |
                       ===""",
               """
                   +---+
                   0    |
                  /|\   |
                        |
                       ===""",
               """
                   +---+
                   0    |
                  /|\   |
                  /     |
                       ===""",
               """
                   +---+
                   0    |
                  /|\   |
                  / \   |
                       ==="""]
    print(hangman[i])


def main():
    hello()
    word = choiseWord()
    for i in range(7):
        hangmanView(i)



main()