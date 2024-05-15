import random

ASCII_ART = """
Welcome to the game Hangman
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
"""
MAX_TRIES = 6  

Dictionery = {
    1: """
         -----
        |     |
        |
        |
        |
        |
      -------""",
    2: """
         -----
        |     |
        |     O
        |
        |
        |
      -------""",
    3: """
         -----
        |     |
        |     O
        |     |
        |
        |
      -------""",
    4: """
         -----
        |     |
        |     O
        |    /|\\
        |
        |
      -------""",
    5: """
         -----
        |     |
        |     O
        |    /|\\
        |    /
        |
      -------""",
    6: """
         -----
        |     |
        |     O
        |    /|\\
        |    / \\
        |
      -------"""
}


def choose_word(file_path, index):

    with open(file_path, 'r') as file:
        word_list = file.read().split()
        unique_words = set(word_list)
        total_unique_words = len(unique_words)
        chosen_index = index % total_unique_words
        chosen_word = list(unique_words)[chosen_index]
        return total_unique_words, chosen_word


def print_hangman(num_of_tries):

    if num_of_tries in Dictionery:
        print(Dictionery[num_of_tries])
    else:
        print("Game over! You have reached the maximum number of attempts.")


def check_valid_input(letter_guessed):
    
    if len(letter_guessed) != 1 or not letter_guessed.isalpha():
        print("X")
        print("Invalid input! Please enter a single alphabetical character.")
        return False
    return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    
    if not check_valid_input(letter_guessed):
        return False

    if letter_guessed in old_letters_guessed:
        print("You already guessed this letter. Try again.")
        old_letters_guessed = list(set(old_letters_guessed))  # Remove duplicates
        print("X\n" + " -> ".join(sorted(old_letters_guessed)))
        return False
    else:
        old_letters_guessed.append(letter_guessed)
        old_letters_guessed.sort()
        return True


def show_hidden_word(secret_word, old_letters_guessed):
    
    display_word = ""
    for letter in secret_word:
        if letter.lower() in old_letters_guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    return display_word.strip()


def check_win(secret_word, old_letters_guessed):
    
    return all(letter.lower() in old_letters_guessed for letter in secret_word)


def play_hangman():
   
    word = choose_word(r"C:\temp\hangman_game.txt", 1)[1]  # Choose a word from the file
    guessed_letters = []  
    wrong_attempts = 0  

    print("Welcome to Hangman!")
    print(ASCII_ART)  

    # Game loop
    while wrong_attempts < MAX_TRIES:
        print("\nWord:", show_hidden_word(word, guessed_letters))  
        print("\n")

        
        guess = input("Guess a letter: ").lower() 

       
        if not try_update_letter_guessed(guess, guessed_letters):
            continue

       
        if guess in word:
            guessed_letters.append(guess)
            print("Correct guess!")
        else:
            wrong_attempts += 1
            print("Wrong guess!")
            print_hangman(wrong_attempts)

        if check_win(word, guessed_letters):
            print("\nCongratulations! You guessed the word:", word)
            break

    if wrong_attempts == MAX_TRIES:
        print("\nSorry, you ran out of attempts. The word was:", word)


def main():
    play_hangman()


if __name__ == "__main__":
    main()