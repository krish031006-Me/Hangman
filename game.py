# to choose a random words from the list
import random
# for emoji
import emoji
# to get fancy text
import pyfiglet
# getting to main()
def main():
    # the list of words to be used to fetch hints and words
    words = [
        {'word': 'banana', 'hint': 'a common fruit'},
        {'word': 'papaya', 'hint': 'a fruit with orange flesh and black seeds'},
        {'word': 'coconut', 'hint': 'lot of electrolytes'},
        {'word': 'chess', 'hint': 'an intellectual game'},
        {'word': 'titanic', 'hint': 'will never sink'},
        {'word': 'violin', 'hint': 'classic music instrument'},
        {'word': 'apple', 'hint': 'related to newton'},
        {'word': 'movies', 'hint': 'combination of multiple art forms—storytelling, music, dialogue'},
        {'word': 'series', 'hint': 'the lengthy new cinema craze'},
        {'word': 'algorithm', 'hint': 'a set of instructions in computing'},
        {'word': 'lighthouse', 'hint': 'guides ships at night'},
        {'word': 'ocean', 'hint': 'through which all life came to exist'},
        {'word': 'music', 'hint': 'it heals everything'},
        {'word': 'python', 'hint': 'a type of snake that is common in corporate'},
        {'word': 'tsunami', 'hint': 'disaster which comes when sea water gets back and recorded first in japan'},
        {'word': 'chatgpt', 'hint': 'replacing professionals'},
        {'word': 'anime', 'hint': 'A style of animation that originated in Japan, known for its vibrant art and storytelling.'},
        {'word': 'echo', 'hint': 'Sound that comes back to you.'}
    ]  
    # length of words to use random choice on it     
    length = len(words)
    # having the index of word that is choosen
    wrd_index = random.choice(range(length))
    # fetching the word from the list
    wrd = words[wrd_index]['word']
    # fetching the hint from the list
    hint = words[wrd_index]['hint']
    # printing the game name
    print_large_text("Welcome to\n Hangman")
    # printing the rules
    print("Rules:\nYou have to guess a word using the hint given to you character by character.\n With every wrong guess you make a structure of a hangman will print as the hangman becomes complete you will lose the game.\n In summary you have 5 chances or 5 lives to correctly guess the word.\n you will get the chance to reveal a word only two times", end = "\n\n")
    print("Start-", end = '\n\n')
    len_wrd, error_count, reveal = len(wrd), 0, 0 # length of word for underscores and an error_count variable
    under = "_"*len_wrd
    while True:
        # to break out of loop when lives have ended
        if error_count == 5: break
        if under == wrd: break
        # printing hangman
        hang_struct(error_count)
        # printing the underscores and hint
        print__(hint, under, error_count)
        #beggining the actual game
        while True:
            # ask for guess
            guess = input("Enter your one character guess- ").strip().lower()
            if guess.isalpha() and len(guess) == 1: # the guess should be an alphabet and a single alphabet specifically
                break
            else:
                print("your guess needs to be a single character")
                continue
        while True:
            # ask for position of the guess
            position =input("Enter the position of your character guess- ").strip()
            if position.isdigit() and 0 <= int(position) <= len_wrd: # the guess should be an alphabet and a single alphabet specifically
                position = int(position) - 1
                if under[int(position)] != '_':
                    print("The position entered is already guessed")
                    continue
                break
            else:
                print("position needs to be a digit and not more than the number of characters in the word")
                continue
        # checking if the guess is same as the character and then changing the under string
        if wrd[position] == guess:
            print()
            print("\033[32mCorrect!!\033[0m") # taken through AI printing in gree as 32m is there
            position = int(position)
            under = under[:position] + guess + under[position + 1:]
            print()
            continue
        else:
            print() 
            print("\033[31mWrong guess\033[0m") # printing in red as 31m is there
            # revealing the correct word at that position
            if reveal < 2:
                under = under[:position] + wrd[position] + under[position + 1:]
                reveal += 1
            error_count += 1
            print()
            continue
    # print_result outside while loop
    print_result(under, error_count, wrd)


def print__(hint, under, error): # printing the dunder
    # printing the hint and lives
    print(f"Hint: {hint}                        Lives: {emoji.emojize('❤️ '*(5 - error))}")
    # print the underscores
    print(f"word: {under}", end = '\n\n')


def print_result(under, error, wrd): # just printing the result
    if all(element != '_' for element in under) and error != 5:
        win_emoji = emoji.emojize("🎉🎊🥳🔥👑")
        print_large_text("Voila")
        print(f"\033[32mCongratulations\033[0m, you won the game and guessed the correct word that is {wrd} {win_emoji}!!!")
        return True # making sure to get out and not let the other conditional run
    elif error == 5:
        print(f"Sorry, you couldn't the guess the correct word, which was {wrd}")
        return True


def print_large_text(text): # taken through AI
    ascii_art = pyfiglet.figlet_format(text, font = 'slant') # figlet_format takes input as a normal text and makes it's ASCII art
    print(ascii_art)


def hang_struct(error): # printing hangman structure using different error values in match case
    print("Hangman:")
    match error:
        case 0:
            print("   +===+")
            print("   |   |")
            print("       |\n"*4)
            print("============")
            print()
        case 1:
            print("   +===+")
            print("   |   |")
            print("   O   |")
            print("       |\n"*3)
            print("============")
            print()
        case 2:
            print("   +===+")
            print("   |   |")
            print("   O   |")
            print("  /|   |")
            print("       |\n"*2)
            print("============")
            print()
        case 3:
            print("   +===+")
            print("   |   |")
            print("   O   |")
            print("  /|\\  |")
            print("       |\n"*2)
            print("============")
            print()
        case 4:
            print("   +===+")
            print("   |   |")
            print("   O   |")
            print("  /|\\  |")
            print("  /    |")
            print("       |\n")
            print("============")
            print()
        case 5:
            print("   +===+")
            print("   |   |")
            print("   O   |")
            print("  /|\\  |")
            print("  / \\  |")
            print("       |\n")
            print("============")
            print()


if __name__ == "__main__":
    main()