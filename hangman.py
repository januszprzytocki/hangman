# hangman game

import random

words = [("doctor", "Profession"), ("architect", "Profession"), ("driver", "Profession"), ("surgeon", "Profession"),
         ("Practice makes perfect", "Proverb"), ("A penny saved is a penny earned", "Proverbs"),
         ("Fortune favours the brave", "Proverb"), ("The world is your oyster", "Proverb"),
         ("New York", "City"), ("Warshaw", "City"), ("Tokyo", "City"), ("Copenhagen", "City"),
         ("Footbol", "Sport"), ("artistic gymnastics", "Sport"), ("basketball", "Sport")]

word = ""  # initialization of the variable in which we hold the word
play = "T"

while play == "T":
    given_letters = []
    letter = ""
    gibbet = 0  # state of gibbet
    how_many_words = len(words)

    # a randomly selected category and word from words
    random_word_number = random.randint(0, how_many_words-1)
    word = words[random_word_number][0]
    category = words[random_word_number][1]
    word_len = len(word)

    # delete the randomly selected word and category from the "WORDS" so that it will not be repeated
    word_org = word
    words.pop(random_word_number)

    word = word.upper()
    category = category.upper()

    print("Word category: ", category)
    word_shown = "*"
    word_shown *= word_len

    while word.count(" ") != 0:
        space = word.index(" ")
        word = word[:space] + "_" + word[space + 1:]
        word_shown = word_shown[:space] + " " + word_shown[space + 1:]

    while word.count("_") != word_len:
        print("Guess the word: ", word_shown)
        while not letter.isalpha():
            letter = input("Enter a letter: ")
            letter = letter.capitalize()
            if not letter.isalpha():
                print("It must be a letter")
        how_many_letters = word.count(letter)

        if how_many_letters == 0 or word_shown.count(letter) > 0:
            if word_shown.count(letter) > 0:
                print("\nOOh, this letter is already revealed. Be careful.")  # letter is already revealed
            elif given_letters.count(letter) != 0:
                print("\nYou have already entered that letter. Be careful.")  # there is no such letter in the word, but it was already given
            else:
                print("\nSorry. There is no such letter in the word", letter)

            given_letters.append(letter)
            gibbet += 1
            if gibbet == 1:
                print("\nI'm starting the construction of the gibbet, the foundation is already there\n")
                print("\n----------")
            elif gibbet == 2:
                print("\nI add a vertical beam\n")
                print("     |")
                print("     |")
                print("     |")
                print("     |")
                print("     |")
                print("     |")
                print("     |")
                print("\n----------")
            elif gibbet == 3:
                print("\nz\n")
                print("      -----")
                print("     |")
                print("     |")
                print("     |")
                print("     |")
                print("     |")
                print("     |")
                print("     |")
                print("\n----------")
            elif gibbet == 4:
                print("\nI'm hooking the rope now\n")
                print("      -----")
                print("     |     |")
                print("     |")
                print("     |")
                print("     |")
                print("     |")
                print("     |")
                print("     |")
                print("\n----------")
            elif gibbet == 5:
                print("\nThe head appears\n")
                print("      -----")
                print("     |     |")
                print("     |     O")
                print("     |")
                print("     |")
                print("     |")
                print("     |")
                print("     |")
                print("\n----------")
            elif gibbet == 6:
                print("\nNow the tummy\n")
                print("      -----")
                print("     |     |")
                print("     |     O")
                print("     |     |")
                print("     |     |")
                print("     |")
                print("     |")
                print("     |")
                print("\n----------")
            elif gibbet == 7:
                print("\nNow the left hand\n")
                print("      -----")
                print("     |     |")
                print("     |     O")
                print("     |    /|")
                print("     |     |")
                print("     |")
                print("     |")
                print("     |")
                print("\n----------")
            elif gibbet == 8:
                print("\nNow the right hand\n")
                print("      -----")
                print("     |     |")
                print("     |     O")
                print("     |    /|\\")
                print("     |     |")
                print("     |")
                print("     |")
                print("     |")
                print("\n----------")
                print("Oh, it's close")
            elif gibbet == 9:
                print("\nNow the right leg\n")
                print("      -----")
                print("     |     |")
                print("     |     O")
                print("     |    /|\\")
                print("     |     |")
                print("     |      \\")
                print("     |")
                print("     |")
                print("\n----------")
                print("Oh, not much anymore")
            else:
                print("\nUpsss..\n")
                print("      -----")
                print("     |     |")
                print("     |     O")
                print("     |    /|\\")
                print("     |     |")
                print("     |    / \\")
                print("     |")
                print("     |")
                print("\n----------")
                
                break
        else:
            for i in range(how_many_letters):
                which_letter = word.index(letter)
                word = word[:which_letter] + "_" + word[which_letter+1:]
                word_shown = word_shown[:which_letter] + letter + word_shown[which_letter+1:]
        letter = ""
    if gibbet == 10:
        print("You are dead, the word is:", word_org)
    else:    
        print("You guessed, the word is: ", word_shown)

    play = "z"
    while play != "T" and play != "N":
        play = input("Do you play again? T/N ").capitalize()

        if play != "T" and play != "N":
            print("Only letter T or  N")

    if how_many_words == 1:
        print("\nYou have already guessed all the words")
        break
               
print("Thanks for the game!!!")
