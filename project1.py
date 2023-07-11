import csv
import random

# Function to choose a random word from a CSV file
def choose_word_from_csv(file_path):
    with open(file_path) as f:
        reader = csv.reader(f)
        words = [word.strip() for row in reader for word in row]
    return random.choice(words)

# Function to update the display word with correctly guessed letters
def update_display_word(word, display_word, letter):
    for i in range(len(word)):
        if word[i] == letter:
            display_word[i] = letter
    return display_word

# Function to check if the game has been won
def check_win(display_word):
    return '_' not in display_word

# Function to play the game
def play_hangman():
    file_path = 'proj1.csv'
    word = choose_word_from_csv(file_path)
    display_word = ['_' for i in range(len(word))]
    incorrect_guesses = 0
    max_incorrect_guesses = 10 
    guessed_letters = []
    
    print('Welcome to Hangman! You have 10 chances to guess the word.')
    print('The word has', len(word), 'letters.')
    
    while incorrect_guesses < max_incorrect_guesses:
        print(' '.join(display_word))
        letter = input('Guess a letter: ').lower()
        
        if letter in guessed_letters:
            print('You have already guessed that letter.')
            continue
        
        guessed_letters.append(letter)
        
        if letter in word:
            display_word = update_display_word(word, display_word, letter)
            print('Correct!')
            
            if check_win(display_word):
                print('Congratulations, you won!')
                return
        
        else:
            incorrect_guesses += 1
            print('Incorrect guess. You have', max_incorrect_guesses - incorrect_guesses, 'guesses left.')
    
    print('Sorry, you lost. The word was', word)

play_hangman()
