import random
from colorama import Fore

def word_pick():
    word_bank = ['dog','cat','king','food', 'party','person', 'balloon', 'below','sorry', 'dragon','face', 'afternoon', 'favorite', 'although', 'usually', 'special', 'planet' ]
    return random.choice(word_bank)

def hangman_drawing (num_of_mistakes):
    if num_of_mistakes == 0:
        pass
    elif num_of_mistakes == 1:
        print("Mistakes: 1/9   ")
        print("                ")
        print("                ")
        print("                ")
        print("                ")
        print("                   ")
        print("           --------")
    elif num_of_mistakes == 2:
        print("Mistakes: 2/9   ")
        print("                ")
        print("                ")
        print("               |")
        print("               |")
        print("               |   ")
        print("           --------")
    elif num_of_mistakes == 3:
        print("Mistakes: 3/9   ")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |   ")
        print("           --------")
    elif num_of_mistakes == 4:
        print("Mistakes: 4/9   ___")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |   ")
        print("           --------")
    elif num_of_mistakes == 5:
        print("Mistakes: 5/9   ___")
        print("               |   |")
        print("               |")
        print("               |")
        print("               |")
        print("               |   ")
        print("           --------")
    elif num_of_mistakes == 6:
        print("Mistakes: 6/9   ___")
        print("               |   |")
        print("               |   o")
        print("               |")
        print("               |")
        print("               |   ")
        print("           --------")
    elif num_of_mistakes == 7:
        print("Mistakes: 7/9   ___")
        print("               |   |")
        print("               |   o")
        print("               |   |")
        print("               |")
        print("               |   ")
        print("           --------")
    elif num_of_mistakes == 8:
        print("Mistakes: 8/9   ___")
        print("               |   |")
        print("               |   o")
        print("               |  /|\ ")
        print("               |")
        print("               |   ")
        print("           --------")
    elif num_of_mistakes == 9:
        print("Mistakes: 9/9   ___")
        print("               |   |")
        print("               |   o")
        print("               |  /|\ ")
        print("               |  /\ ")
        print("               |   ")
        print("           --------")


def word_display(picked_word,guessed_letters):
    word = list(len(picked_word)*'*')

    for letter in guessed_letters:
        if letter in picked_word:
            word_index = picked_word.index(letter)

            word[word_index] = letter
    print(''.join(word))

def check_win(letter_attempts,letter_of_picked_word):
    return all(letter in letter_attempts for letter in letter_of_picked_word)

picked_word = word_pick()
letter_of_picked_word = list(picked_word)
letter_attempts = []
win = False
num_of_mistakes = 0


print (Fore.BLUE +'Welcome to the HangMan game')
print (len(picked_word )*'*')

while (win == False) and (num_of_mistakes < 9):
    attempt = input('Guess a letter from the hidden word').lower()
    print('\n' * 100)
    if attempt[0] in letter_attempts:
        print (f'You\'e already guessed the  letter {attempt[0]}')
        continue
    else:
        letter_attempts.append(attempt)
        if attempt in letter_of_picked_word:
            print(Fore.GREEN +f'correct! the letter {attempt[0]} is one of the letters in the hidden word')
            word_display(picked_word,letter_attempts)
            win = check_win(letter_attempts, letter_of_picked_word)
        else:
            num_of_mistakes = num_of_mistakes + 1
            print(Fore.RED + f'Wrong! the letter {attempt[0]} is not one of the letters in the hidden word')
            word_display(picked_word, letter_attempts)
            hangman_drawing(num_of_mistakes)

if win == True:
    print(Fore.YELLOW +'Congratulations, you won! \n The man will live to hang on another day')
else:
    print(Fore.RED +'Game over! \n The man is dead and it\'s on your conscience')