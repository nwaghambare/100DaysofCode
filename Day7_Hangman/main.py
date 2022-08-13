import random


def print_hangman(hangman_level=0):
    hangman = [["    __________",
                "    |         |",
                "    |         |",
                "              |",
                "              |",
                "              |",
                "              |",
                "              |",
                "              |",
                "      ________|"],
               ["    __________",
                "    |         |",
                "    |         |",
                "    0         |",
                "              |",
                "              |",
                "              |",
                "              |",
                "              |",
                "      ________|"],
               ["    __________",
                "    |         |",
                "    |         |",
                "    0         |",
                "    |         |",
                "              |",
                "              |",
                "              |",
                "              |",
                "      ________|"],
               ["    __________",
                "    |         |",
                "    |         |",
                "    0         |",
                "   /|         |",
                "              |",
                "              |",
                "              |",
                "              |",
                "      ________|"],
               ["    __________",
                "    |         |",
                "    |         |",
                "    0         |",
                "   /|\\        |",
                "              |",
                "              |",
                "              |",
                "              |",
                "      ________|"],
               ["    __________",
                "    |         |",
                "    |         |",
                "    0         |",
                "   /|\\        |",
                "   /          |",
                "              |",
                "              |",
                "              |",
                "      ________|"],
               ["    __________",
                "    |         |",
                "    |         |",
                "    0         |",
                "   /|\\        |",
                "   / \\        |",
                "              |",
                "              |",
                "              |",
                "      ________|"]
               ]
    print("\n".join(hangman[hangman_level]))


# random words list
words = ['hangman', 'elephant', 'facebook', 'instagram', 'whatsapp', 'smartphone', 'bottle', 'garbage', 'bungalow',
         'computer']

# select word from list randomly
selected_word = random.choice(words)
empty_spaces = wordlen = len(selected_word)
hangman_count = 0
match_count = 0
print('Can you guess this word?')
while empty_spaces:
    print("_ ", end='')
    empty_spaces -= 1
print("\n")
output = ["_ "] * wordlen
while match_count < wordlen:
    print_hangman(hangman_count)
    # ask user for letter
    user_input = ''
    while not user_input and len(user_input) != 1:
        user_input = input("\nGuess a letter from the word: ")
        if len(user_input) != 1:
            print('Invalid Input. Try Again.')

    # check letter in the selected word

    if user_input in selected_word:
        for i in range(len(selected_word)):
            if user_input == selected_word[i]:
                output[i] = user_input
                match_count += 1
        print("\n" * 100)
        print("".join(output))
    else:
        print("\n" * 100)
        print("".join(output))
        print(f"{user_input} not in the word.")
        hangman_count += 1
        if hangman_count == 6:
            print("Game Over")
            print_hangman(hangman_count)
            break

if "".join(output) == selected_word:
    print_hangman(hangman_count)
    print("You Won!!")
