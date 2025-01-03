import random


def hangman():
    words_list = ['cat', 'dog', 'bear', 'fox', 'rabbit', 'crocodile']
    word = words_list[random.randint(0, len(words_list))]

    wrong_guesses = 0

    stages = ["",
              "________      ",
              "|      |      ",
              "|      0      ",
              "|     /|\\     ",
              "|     / \\     ",
              "|"]

    remaining_letters = list(word)
    letter_board = ["_"] * len(word)
    win = False

    print('Welcome to Hangman')

    while wrong_guesses < len(stages) - 1:
        print()
        guess = input("Guess a letter\n")

        if guess in remaining_letters:
            character_index = remaining_letters.index(guess)
            letter_board[character_index] = guess
            remaining_letters[character_index] = '$'
        else:
            wrong_guesses += 1
            print('\n'.join(stages[0: wrong_guesses + 1]))

        print((' '.join(letter_board)))

        if '_' not in letter_board:
            print('You win! The word was:')
            print(''.join(letter_board))
            win = True
            break

    if not win:
        print('\n'.join(stages[0: wrong_guesses]))
        print(f'You lose! The words was {word}')


hangman()
