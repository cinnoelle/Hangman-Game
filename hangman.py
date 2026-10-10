# Created by: Sara
# Purpose: HW7 , reading from a file and using decision and repetition to solve a problem
# Created at: 11/17/25, 9:11am
# Last modified: 11/17/25, 11:29pm

import random
from graphics import *

#accepts file, returns list of words from file
def read_words(file):
    #open the file and read it
    open_file = open(file, "r")
    #create empty list to put words in
    words = []

    for line in open_file:
        #strip line 
        line = line.strip()
        #append to list and make the words auto lower-cased in the file
        words.append(line.lower())
    #print(file)
    return words

#returns a random word from the list
def random_words(words):
    rand_word = random.choice(words)
    #print(rand_word)
    return rand_word


#ask player to choose a letter, 
#if choice longer than 1 letter or alrd guessed, should ask player for input again
#letter should be added to list if guessed
def get_guess(guessed_letters):

    while True:
        #ask user to guess a letter, make it lowercased
        guess = input("Guess a letter: ").strip().lower()

        #if guess is longer than 1 letter or not part of alphabet
        if len(guess) != 1 or not guess.isalpha():
            print("Enter one letter (a-z)")
        #if letter is already guessed
        elif guess in guessed_letters:
            print(f"You already guessed '{guess}', guess again")
        else:
            guessed_letters.append(guess)
            return guess

#uses secret word and guesses to build and return players current guess
def blanks(word, guessed_letters):
    #create list
    hangman = []
    #find each letter in the word
    for ch in word:
        #append letter if it is guessed to show as a guessed letter instead of blank
        if ch in guessed_letters:
            hangman.append(ch)
            #else keep underscore
        else:
            hangman.append("_")
    
    #make list into a string
    spaces = ""
    #add spaces to the word
    for ch in hangman:
        spaces += ch + ""
    #strip for anything extra and then return
    return spaces.strip()


def game_won(blanks):
    #if there are no blanks, return True for game being won
    if "_" not in blanks:
        return True
    else:
        return False


def play_game():

    #set read_words to variable for use in random_words
    data = read_words("hangmanwords.txt")
    #get the list of words from read_words and pick a random one, set to word variable
    word = random_words(data)
    #list to track characters guessed
    guessed_letters = []
    #list to track wrong guesses
    wrong_guesses = []
    #max num of incorrect guesses allowed
    max_incorrect = 7

    #game loop
    while True:
        #get current word displayed
        current = blanks(word, guessed_letters)
        print(f"Word: {current}")
        print(f"Incorrect Guesses: {wrong_guesses}")
        print(f"Guesses left: {max_incorrect - len(wrong_guesses)}")

        #get the players guess
        guess = get_guess(guessed_letters)

        #if guess is not in word add it to wrong guess list
        if guess not in word:
            wrong_guesses.append(guess)

        #if player runs out of guesses (goes over max incorrect), they lose and break to end game
        if len(wrong_guesses) >= max_incorrect:
            print(f"You lost. The word was: {word}")
            break
        
        #check if player guessed the whole word w/ no blanks left
        current_blanks = blanks(word, guessed_letters)
        if game_won(current_blanks):
            print(f"You won! The word was: {word}")
            break

#hashtag this out to play just graphics version
#play_game()


"""
EXTRA CREDIT
"""
def graphics_hangman(word):
    #window: name, width, height 
    win = GraphWin("Hangman", 800, 500)
    win.setBackground("pink")

    #create list for guessed letters
    guessed_letters = []

    #pre drawn lines for gallows - part 1
    line1 = Line(Point(100,100), Point(100, 400))
    line1.draw(win)
    line2 = Line(Point(40,400), Point(160, 400))
    line2.draw(win)
    line3 = Line(Point(100,100), Point(200, 100))
    line3.draw(win)
    line4 = Line(Point(200,100), Point(200, 170))
    line4.draw(win)


    #all parts of hang man in a list
    parts = []

    #head - part 2
    head = Circle(Point(200,180), 35)
    head.setFill("white")
    parts.append(head)

    #body - part 3
    body = Line(Point(200, 215), Point(200, 300))
    parts.append(body)

    #right arm - part 3
    right_arm = Line(Point(200, 240), Point(250, 250))
    parts.append(right_arm)

    #left arm - part 4
    left_arm = Line(Point(200, 240), Point(150, 250))
    parts.append(left_arm)

    #right leg - part 5
    right_leg = Line(Point(200, 300), Point(150, 350))
    parts.append(right_leg)

    #left leg - part 6
    left_leg = Line(Point(200, 300), Point(250, 350))
    parts.append(left_leg)

    #mouth - part 7
    mouth = Line(Point(190, 200), Point(210, 200))
    parts.append(mouth)


    #face if lost 
    lose_face = [
    Line(Point(175, 175), Point(190, 175)),
    Line(Point(210, 175), Point(225, 175))
    ]

    #face if won
    win_face = [
    Circle(Point(180, 175), 10),
    Circle(Point(220, 175), 10)
    ]
    #filling in eyes because it doesn't work in list
    for eye in win_face:
        eye.setFill("black")

    #undraw the parts
    for part in parts:
        part.undraw()
    for part in lose_face:
        part.undraw()
    for part in win_face:
        part.undraw()

    #make list for guessed letters
    guessed_letters = []
    #set mistakes to 0 to start
    mistakes = 0
    #max mistakes is the length of the parts (should be 7 parts)
    max_mistakes = len(parts)


    # TEXT
    # concatenate word display 
    word_display = ""
    for ch in word:
        word_display += "_ "

    #strip word display
    word_display = word_display.strip()
    #set a text for the word display (the underscores on the screen)
    underscores = Text(Point(500, 120), word_display)
    underscores.setSize(18)
    underscores.draw(win)

    #guesses left displayed as text
    guess_display = Text(Point(500, 160), f"Guesses left: {max_mistakes - mistakes}")
    guess_display.draw(win)

    #used letters displayed as text
    used_display = Text(Point(500, 200), "Used letters: ")
    used_display.draw(win)


    # ENTRY BOX
    #entry box created to make guesses in
    entry = Entry(Point(500, 260), 5)
    entry.draw(win)
    
    #submit icon made into a rectangle w/ text saying submit
    submit_rectangle = Rectangle(Point(450, 285), Point(550, 315))
    submit_rectangle.draw(win)
    submit_text = Text(Point(500, 300), "SUBMIT")
    submit_text.draw(win)


    # LOOP
    #while true - 
    while True:

        #set get mouse to click variable to call
        click = win.getMouse()
        #get x and y of click
        x = click.getX()
        y = click.getY()

        #if user isn't clicking inside submit button, continue the loop
        if not (450 <= x <= 550 and 285 <= y <= 315):
            continue

        #get text of entry, lowercase it, strip it
        guess = entry.getText().lower().strip()

        #set entry text
        entry.setText("")

        # if  guess length is not equal to one or guess is not in the alphabet, continue
        if len(guess) != 1 or not guess.isalpha():
            continue

        # if guess is in guessed_letters, continue
        if guess in guessed_letters:
            continue

        #append guess into guessed letters
        guessed_letters.append(guess)

        #concatenate letters
        letters = ""
        for i in range(len(guessed_letters)):
            letters += guessed_letters[i]
            #if i is not last letter in list, add a comma to separate the letters
            if i != len(guessed_letters) - 1:   
                letters += ", "

        #update display to show all letters guessed
        used_display.setText("Used letters: " + letters)


        #start w/ empty string
        updated = ""
        for cha in word:
            if cha in guessed_letters:
                updated += cha #if the letter is guessed show it on screen
            else:
                updated += "_"  #if not keep underscore
            updated += " " #add space after each character
            
        #remove extra spaces at end and update text on screen
        updated = updated.strip()
        underscores.setText(updated)

        #check if player has whole word guessed
        if "_" not in updated:
            #draw eyes for winning face + display win msg
            for eye in win_face:
                eye.draw(win) 
            message = Text(Point(500, 350), "YOU WON! Play Again?")
            message.setSize(18)
            message.draw(win)
            break   #exit if game is won

        #if guessed letter not in word, update hangman guy
        if guess not in word:
            if mistakes < max_mistakes:
                parts[mistakes].draw(win)   #draw next part of hangman
            mistakes += 1   #add to mistake counter
            #update guesses left
            guess_display.setText("Guesses left: " + str(max_mistakes - mistakes))

        #check if player reached max mistakes
        if mistakes == max_mistakes:
            #draw eyes for losing face + draw losing msg
            for eye in lose_face:
                eye.draw(win)
            message = Text(Point(500, 350), f"YOU LOST! Word was: {word}\nPlay Again?")
            message.setSize(18)
            message.draw(win)
            break #get out of loop if game lost
        
    #yes and no text boxes created + drawn + set size to 18
    yes_box = Rectangle(Point(430, 380), Point(490, 420))
    yes_text = Text(Point(460, 400), "YES")
    yes_text.setSize(18)
    no_box = Rectangle(Point(510, 380), Point(570, 420))
    no_text = Text(Point(540, 400), "NO")
    no_text.setSize(18)
    yes_box.draw(win)
    no_box.draw(win)
    yes_text.draw(win)
    no_text.draw(win)

    
    while True:
        click = win.getMouse()
        #get x and y of click
        x = click.getX()
        y = click.getY()

        #if yes is clicked, set to True
        if 430 <= x <= 490 and 380 <= y <= 420:
            win.close()
            return True
        
        #if no is clicked, set to False
        if 510 <= x <= 570 and 380 <= y <= 420:
            win.close()
            return False
        

while True:
    #set read_words to variable for use in random_words
    data = read_words("hangmanwords.txt")
    #get the list of words from read_words and pick a random one, set to word variable
    word = random_words(data)

    #reopen window if playing again
    play_again = graphics_hangman(word)
    #end if not playing again
    if not play_again:
        break
