# General setup stuff
import turtle

turtle.shape("blank")
turtle.setup(width=1.0, height=1.0, startx=0, starty=0)
turtle.title("Hangman!")
turtle.pensize(4)

# Variable defaults
newNumberCorrect = 0
newNumberIncorrect = 0
firstLetterCorrect = 0
secondLetterCorrect = 0
thirdLetterCorrect = 0
fourthLetterCorrect = 0
fifthLetterCorrect = 0
sixthLetterCorrect = 0
seventhLetterCorrect = 0
eighthLetterCorrect = 0
ninethLetterCorrect = 0
tenthLetterCorrect = 0
spacing = 0
rowHeight = 0
error = 0
wrongLetters = []

# Title
turtle.up()
turtle.setpos(-75, 200)
turtle.write("Hangman!", font=("Arial", 30, "normal"))

# Frame
turtle.setpos(-125, 50)
turtle.pendown()
turtle.setpos(-125, 100)
turtle.setpos(-250, 100)
turtle.setpos(-250, -200)
turtle.up()
turtle.setpos(-300, -200)
turtle.pendown()
turtle.setpos(-150, -200)

# Word setup
word = turtle.textinput("", "Please enter a word that is between 3 and 10 letters long: ")  # Word user input
wordLength = len(word)  # Finds length of the word
letters = list(word)  # Splits the string into separate characters

# Makes sure that the word is between 3 and 10 letters long
if wordLength > 10:
    turtle.clear()
    turtle.up()
    turtle.setpos(-280, 0)
    turtle.write("Sorry, your word must cannot be more than 10 letters long.", font=("Arial", 21, "normal"))
else:
    if wordLength < 3:
        turtle.clear()
        turtle.up()
        turtle.setpos(-230, 0)
        turtle.write("Sorry, your word must be at least 3 letters long.", font=("Arial", 21, "normal"))
    else:

        # 3 letter word
        if wordLength == 3:
            turtle.up()
            turtle.setpos(-100, -200)
            turtle.pendown()
            turtle.setpos(-70, -200)
            turtle.up()
            turtle.setpos(-60, -200)
            turtle.pendown()
            turtle.setpos(-30, -200)
            turtle.up()
            turtle.setpos(-20, -200)
            turtle.pendown()
            turtle.setpos(10, -200)
            firstLetter = letters[0]
            secondLetter = letters[1]
            thirdLetter = letters[2]
            # Guessing program for a 3 letter word (runs if the guess is one letter, the user has not yet guessed the word
            # and there are less than 8 incorrect guesses/the hangman has not been fully drawn)
            while newNumberCorrect < wordLength and newNumberIncorrect < 8:
                guess = turtle.textinput("", "What is your guess?")  # Guess user input
                guessLength = len(guess)  # Finds the number of letters in the guess
                oldNumberCorrect = newNumberCorrect  # The old number of correct letters is set to the current value
                oldNumberIncorrect = newNumberIncorrect  # The old number of incorrect letter is set to the current value
                if guessLength == 1 and not guess == "":  # Runs if the guess is less than one letter
                    # Checks to see if the guess is the first letter of the word
                    if guess == firstLetter and firstLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(-90, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        firstLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the second letter of the word
                    if guess == secondLetter and secondLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(-50, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        secondLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the third letter of the word
                    if guess == thirdLetter and thirdLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(-10, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        thirdLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Runs when you had an incorrect guess (the number of correct letters has not changed)
                    if newNumberCorrect == oldNumberCorrect and not guess in wrongLetters:
                        if guess == firstLetter or guess == secondLetter or guess == thirdLetter:
                            newNumberIncorrect = newNumberIncorrect
                        else:
                            newNumberIncorrect += 1
                            turtle.up()
                            turtle.setpos(spacing, rowHeight)
                            turtle.write(guess, font=("Arial", 25, "normal"))
                            wrongLetters.append(guess)
                            # Changes the spacing between each character for incorrect guesses
                            if spacing < 241:
                                spacing += 30
                            else:
                                spacing = 0
                                rowHeight -= 30
                    # Runs when you had a new incorrect guess
                    if newNumberIncorrect > oldNumberIncorrect:
                        # When the total number of incorrect guesses is 1
                        if newNumberIncorrect == 1:
                            # Draws face
                            turtle.up()
                            turtle.setpos(-125, -10)
                            turtle.pendown()
                            turtle.circle(30)
                        # When the total number of incorrect guesses is 2
                        if newNumberIncorrect == 2:
                            # Draws body
                            turtle.up()
                            turtle.setpos(-125, -10)
                            turtle.pendown()
                            turtle.setpos(-125, -100)
                        # When the total number of incorrect guesses is 3
                        if newNumberIncorrect == 3:
                            # Draws left leg
                            turtle.up()
                            turtle.setpos(-125, -100)
                            turtle.pendown()
                            turtle.setpos(-160, -160)
                        # When the total number of incorrect guesses is 4
                        if newNumberIncorrect == 4:
                            # Draws right leg
                            turtle.up()
                            turtle.setpos(-125, -100)
                            turtle.pendown()
                            turtle.setpos(-90, -160)
                        # When the total number of incorrect guesses is 5
                        if newNumberIncorrect == 5:
                            # Draws left arm
                            turtle.up()
                            turtle.setpos(-125, -35)
                            turtle.pendown()
                            turtle.setpos(-150, -85)
                        # When the total number of incorrect guesses is 6
                        if newNumberIncorrect == 6:
                            # Draws right arm
                            turtle.up()
                            turtle.setpos(-125, -35)
                            turtle.pendown()
                            turtle.setpos(-100, -85)
                        # When the total number of incorrect guesses is 7
                        if newNumberIncorrect == 7:
                            # Draws mouth
                            turtle.up()
                            turtle.setpos(-135, 5)
                            turtle.pendown()
                            turtle.setpos(-115, 5)
            # When the total number of incorrect guesses is 8
            if newNumberIncorrect == 8:
                # Draws left eye
                turtle.up()
                turtle.setpos(-140, 30)
                turtle.pendown()
                turtle.setpos(-130, 20)
                turtle.up()
                turtle.setpos(-130, 30)
                turtle.pendown()
                turtle.setpos(-140, 20)
                # Draws right eye
                turtle.up()
                turtle.setpos(-120, 30)
                turtle.pendown()
                turtle.setpos(-110, 20)
                turtle.up()
                turtle.setpos(-110, 30)
                turtle.pendown()
                turtle.setpos(-120, 20)
                # Fills in the letters
                turtle.up()
                turtle.setpos(-90, -200)
                turtle.write(firstLetter, font=("Arial", 25, "normal"))
                turtle.setpos(-50, -200)
                turtle.write(secondLetter, font=("Arial", 25, "normal"))
                turtle.setpos(-10, -200)
                turtle.write(thirdLetter, font=("Arial", 25, "normal"))
                # Writes "Sorry, you're out of guesses." in the top right corner
                turtle.setpos(-40, 100)
                turtle.pencolor("red")
                turtle.write("Sorry, you're out of guesses.", font=("Arial", 25, "normal"))
            # When you have guessed all the letters
            if newNumberCorrect == wordLength:
                turtle.up()
                turtle.setpos(-20, 100)
                turtle.pencolor("green")
                turtle.write("You guessed correct!!!", font=("Arial", 25, "normal"))

        # 4 letter word
        if wordLength == 4:
            turtle.up()
            turtle.setpos(-100, -200)
            turtle.pendown()
            turtle.setpos(-70, -200)
            turtle.up()
            turtle.setpos(-60, -200)
            turtle.pendown()
            turtle.setpos(-30, -200)
            turtle.up()
            turtle.setpos(-20, -200)
            turtle.pendown()
            turtle.setpos(10, -200)
            turtle.up()
            turtle.setpos(20, -200)
            turtle.pendown()
            turtle.setpos(50, -200)
            firstLetter = letters[0]
            secondLetter = letters[1]
            thirdLetter = letters[2]
            fourthLetter = letters[3]
            # Guessing program for a 4 letter word (runs if the guess is one letter, the user has not yet guessed the word
            # and there are less than 8 incorrect guesses/the hangman has not been fully drawn)
            while newNumberCorrect < wordLength and newNumberIncorrect < 8:
                guess = turtle.textinput("", "What is your guess?")  # Guess user input
                guessLength = len(guess)  # Finds the number of letters in the guess
                oldNumberCorrect = newNumberCorrect  # The old number of correct letters is set to the current value
                oldNumberIncorrect = newNumberIncorrect  # The old number of incorrect letter is set to the current value
                if guessLength == 1 and not guess == "":  # Runs if the guess is more than one letter
                    # Checks to see if the guess is the first letter of the word
                    if guess == firstLetter and firstLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(-90, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        firstLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the second letter of the word
                    if guess == secondLetter and secondLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(-50, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        secondLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the third letter of the word
                    if guess == thirdLetter and thirdLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(-10, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        thirdLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the fourth letter of the word
                    if guess == fourthLetter and fourthLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(30, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        fourthLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Runs when you had an incorrect guess (the number of correct letters has not changed)
                    if newNumberCorrect == oldNumberCorrect and not guess in wrongLetters:
                        if guess == firstLetter or guess == secondLetter or guess == thirdLetter or guess == fourthLetter:
                            newNumberIncorrect = newNumberIncorrect
                        else:
                            newNumberIncorrect += 1
                            turtle.up()
                            turtle.setpos(spacing, rowHeight)
                            turtle.write(guess, font=("Arial", 25, "normal"))
                            wrongLetters.append(guess)
                            # Changes the spacing between each character for incorrect guesses
                            if spacing < 241:
                                spacing += 30
                            else:
                                spacing = 0
                                rowHeight -= 30
                    # Runs when you had a new incorrect guess
                    if newNumberIncorrect > oldNumberIncorrect:
                        # When the total number of incorrect guesses is 1
                        if newNumberIncorrect == 1:
                            # Draws face
                            turtle.up()
                            turtle.setpos(-125, -10)
                            turtle.pendown()
                            turtle.circle(30)
                        # When the total number of incorrect guesses is 2
                        if newNumberIncorrect == 2:
                            # Draws body
                            turtle.up()
                            turtle.setpos(-125, -10)
                            turtle.pendown()
                            turtle.setpos(-125, -100)
                        # When the total number of incorrect guesses is 3
                        if newNumberIncorrect == 3:
                            # Draws left leg
                            turtle.up()
                            turtle.setpos(-125, -100)
                            turtle.pendown()
                            turtle.setpos(-160, -160)
                        # When the total number of incorrect guesses is 4
                        if newNumberIncorrect == 4:
                            # Draws right leg
                            turtle.up()
                            turtle.setpos(-125, -100)
                            turtle.pendown()
                            turtle.setpos(-90, -160)
                        # When the total number of incorrect guesses is 5
                        if newNumberIncorrect == 5:
                            # Draws left arm
                            turtle.up()
                            turtle.setpos(-125, -35)
                            turtle.pendown()
                            turtle.setpos(-150, -85)
                        # When the total number of incorrect guesses is 6
                        if newNumberIncorrect == 6:
                            # Draws right arm
                            turtle.up()
                            turtle.setpos(-125, -35)
                            turtle.pendown()
                            turtle.setpos(-100, -85)
                        # When the total number of incorrect guesses is 7
                        if newNumberIncorrect == 7:
                            # Draws mouth
                            turtle.up()
                            turtle.setpos(-135, 5)
                            turtle.pendown()
                            turtle.setpos(-115, 5)
            # When the total number of incorrect guesses is 8
            if newNumberIncorrect == 8:
                # Draws left eye
                turtle.up()
                turtle.setpos(-140, 30)
                turtle.pendown()
                turtle.setpos(-130, 20)
                turtle.up()
                turtle.setpos(-130, 30)
                turtle.pendown()
                turtle.setpos(-140, 20)
                # Draws right eye
                turtle.up()
                turtle.setpos(-120, 30)
                turtle.pendown()
                turtle.setpos(-110, 20)
                turtle.up()
                turtle.setpos(-110, 30)
                turtle.pendown()
                turtle.setpos(-120, 20)
                # Fills in the letters
                turtle.up()
                turtle.setpos(-90, -200)
                turtle.write(firstLetter, font=("Arial", 25, "normal"))
                turtle.setpos(-50, -200)
                turtle.write(secondLetter, font=("Arial", 25, "normal"))
                turtle.setpos(-10, -200)
                turtle.write(thirdLetter, font=("Arial", 25, "normal"))
                turtle.setpos(30, -200)
                turtle.write(fourthLetter, font=("Arial", 25, "normal"))
                # Writes "Sorry, you're out of guesses." in the top right corner
                turtle.setpos(-40, 100)
                turtle.pencolor("red")
                turtle.write("Sorry, you're out of guesses.", font=("Arial", 25, "normal"))
            # When you have guessed all the letters
            if newNumberCorrect == wordLength:
                turtle.up()
                turtle.setpos(-20, 100)
                turtle.pencolor("green")
                turtle.write("You guessed correct!!!", font=("Arial", 25, "normal"))

        # 5 letter word
        if wordLength == 5:
            turtle.up()
            turtle.setpos(-100, -200)
            turtle.pendown()
            turtle.setpos(-70, -200)
            turtle.up()
            turtle.setpos(-60, -200)
            turtle.pendown()
            turtle.setpos(-30, -200)
            turtle.up()
            turtle.setpos(-20, -200)
            turtle.pendown()
            turtle.setpos(10, -200)
            turtle.up()
            turtle.setpos(20, -200)
            turtle.pendown()
            turtle.setpos(50, -200)
            turtle.up()
            turtle.setpos(60, -200)
            turtle.pendown()
            turtle.setpos(90, -200)
            firstLetter = letters[0]
            secondLetter = letters[1]
            thirdLetter = letters[2]
            fourthLetter = letters[3]
            fifthLetter = letters[4]
            # Guessing program for a 5 letter word (runs if the guess is one letter, the user has not yet guessed the word
            # and there are less than 8 incorrect guesses/the hangman has not been fully drawn)
            while newNumberCorrect < wordLength and newNumberIncorrect < 8:
                guess = turtle.textinput("", "What is your guess?")  # Guess user input
                guessLength = len(guess)  # Finds the number of letters in the guess
                oldNumberCorrect = newNumberCorrect  # The old number of correct letters is set to the current value
                oldNumberIncorrect = newNumberIncorrect  # The old number of incorrect letter is set to the current value
                if guessLength == 1 and not guess == "":  # Runs if the guess is more than one letter
                    # Checks to see if the guess is the first letter of the word
                    if guess == firstLetter and firstLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(-90, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        firstLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the second letter of the word
                    if guess == secondLetter and secondLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(-50, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        secondLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the third letter of the word
                    if guess == thirdLetter and thirdLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(-10, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        thirdLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the fourth letter of the word
                    if guess == fourthLetter and fourthLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(30, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        fourthLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the fifth letter of the word
                    if guess == fifthLetter and fifthLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(70, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        fifthLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Runs when you had an incorrect guess (the number of correct letters has not changed)
                    if newNumberCorrect == oldNumberCorrect and not guess in wrongLetters:
                        if guess == firstLetter or guess == secondLetter or guess == thirdLetter or guess == fourthLetter or guess == fifthLetter:
                            newNumberIncorrect = newNumberIncorrect
                        else:
                            newNumberIncorrect += 1
                            turtle.up()
                            turtle.setpos(spacing, rowHeight)
                            turtle.write(guess, font=("Arial", 25, "normal"))
                            wrongLetters.append(guess)
                            # Changes the spacing between each character for incorrect guesses
                            if spacing < 241:
                                spacing += 30
                            else:
                                spacing = 0
                                rowHeight -= 30
                    # Runs when you had a new incorrect guess
                    if newNumberIncorrect > oldNumberIncorrect:
                        # When the total number of incorrect guesses is 1
                        if newNumberIncorrect == 1:
                            # Draws face
                            turtle.up()
                            turtle.setpos(-125, -10)
                            turtle.pendown()
                            turtle.circle(30)
                        # When the total number of incorrect guesses is 2
                        if newNumberIncorrect == 2:
                            # Draws body
                            turtle.up()
                            turtle.setpos(-125, -10)
                            turtle.pendown()
                            turtle.setpos(-125, -100)
                        # When the total number of incorrect guesses is 3
                        if newNumberIncorrect == 3:
                            # Draws left leg
                            turtle.up()
                            turtle.setpos(-125, -100)
                            turtle.pendown()
                            turtle.setpos(-160, -160)
                        # When the total number of incorrect guesses is 4
                        if newNumberIncorrect == 4:
                            # Draws right leg
                            turtle.up()
                            turtle.setpos(-125, -100)
                            turtle.pendown()
                            turtle.setpos(-90, -160)
                        # When the total number of incorrect guesses is 5
                        if newNumberIncorrect == 5:
                            # Draws left arm
                            turtle.up()
                            turtle.setpos(-125, -35)
                            turtle.pendown()
                            turtle.setpos(-150, -85)
                        # When the total number of incorrect guesses is 6
                        if newNumberIncorrect == 6:
                            # Draws right arm
                            turtle.up()
                            turtle.setpos(-125, -35)
                            turtle.pendown()
                            turtle.setpos(-100, -85)
                        # When the total number of incorrect guesses is 7
                        if newNumberIncorrect == 7:
                            # Draws mouth
                            turtle.up()
                            turtle.setpos(-135, 5)
                            turtle.pendown()
                            turtle.setpos(-115, 5)
            # When the total number of incorrect guesses is 8
            if newNumberIncorrect == 8:
                # Draws left eye
                turtle.up()
                turtle.setpos(-140, 30)
                turtle.pendown()
                turtle.setpos(-130, 20)
                turtle.up()
                turtle.setpos(-130, 30)
                turtle.pendown()
                turtle.setpos(-140, 20)
                # Draws right eye
                turtle.up()
                turtle.setpos(-120, 30)
                turtle.pendown()
                turtle.setpos(-110, 20)
                turtle.up()
                turtle.setpos(-110, 30)
                turtle.pendown()
                turtle.setpos(-120, 20)
                # Fills in the letters
                turtle.up()
                turtle.setpos(-90, -200)
                turtle.write(firstLetter, font=("Arial", 25, "normal"))
                turtle.setpos(-50, -200)
                turtle.write(secondLetter, font=("Arial", 25, "normal"))
                turtle.setpos(-10, -200)
                turtle.write(thirdLetter, font=("Arial", 25, "normal"))
                turtle.setpos(30, -200)
                turtle.write(fourthLetter, font=("Arial", 25, "normal"))
                turtle.setpos(70, -200)
                turtle.write(fifthLetter, font=("Arial", 25, "normal"))
                # Writes "Sorry, you're out of guesses." in the top right corner
                turtle.setpos(-40, 100)
                turtle.pencolor("red")
                turtle.write("Sorry, you're out of guesses.", font=("Arial", 25, "normal"))
            # When you have guessed all the letters
            if newNumberCorrect == wordLength:
                turtle.up()
                turtle.setpos(-20, 100)
                turtle.pencolor("green")
                turtle.write("You guessed correct!!!", font=("Arial", 25, "normal"))

        # 6 letter word
        if wordLength == 6:
            turtle.up()
            turtle.setpos(-100, -200)
            turtle.pendown()
            turtle.setpos(-70, -200)
            turtle.up()
            turtle.setpos(-60, -200)
            turtle.pendown()
            turtle.setpos(-30, -200)
            turtle.up()
            turtle.setpos(-20, -200)
            turtle.pendown()
            turtle.setpos(10, -200)
            turtle.up()
            turtle.setpos(20, -200)
            turtle.pendown()
            turtle.setpos(50, -200)
            turtle.up()
            turtle.setpos(60, -200)
            turtle.pendown()
            turtle.setpos(90, -200)
            turtle.up()
            turtle.setpos(100, -200)
            turtle.pendown()
            turtle.setpos(130, -200)
            firstLetter = letters[0]
            secondLetter = letters[1]
            thirdLetter = letters[2]
            fourthLetter = letters[3]
            fifthLetter = letters[4]
            sixthLetter = letters[5]
            # Guessing program for a 6 letter word (runs if the guess is one letter, the user has not yet guessed the word
            # and there are less than 8 incorrect guesses/the hangman has not been fully drawn)
            while newNumberCorrect < wordLength and newNumberIncorrect < 8:
                guess = turtle.textinput("", "What is your guess?")  # Guess user input
                guessLength = len(guess)  # Finds the number of letters in the guess
                oldNumberCorrect = newNumberCorrect  # The old number of correct letters is set to the current value
                oldNumberIncorrect = newNumberIncorrect  # The old number of incorrect letter is set to the current value
                if guessLength == 1 and not guess == "":  # Runs if the guess is more than one letter
                    # Checks to see if the guess is the first letter of the word
                    if guess == firstLetter and firstLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(-90, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        firstLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the second letter of the word
                    if guess == secondLetter and secondLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(-50, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        secondLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the third letter of the word
                    if guess == thirdLetter and thirdLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(-10, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        thirdLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the fourth letter of the word
                    if guess == fourthLetter and fourthLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(30, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        fourthLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the fifth letter of the word
                    if guess == fifthLetter and fifthLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(70, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        fifthLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the sixth letter of the word
                    if guess == sixthLetter and sixthLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(110, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        sixthLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Runs when you had an incorrect guess (the number of correct letters has not changed)
                    if newNumberCorrect == oldNumberCorrect and not guess in wrongLetters:
                        if guess == firstLetter or guess == secondLetter or guess == thirdLetter or guess == fourthLetter or guess == fifthLetter or guess == sixthLetter:
                            newNumberIncorrect = newNumberIncorrect
                        else:
                            newNumberIncorrect += 1
                            turtle.up()
                            turtle.setpos(spacing, rowHeight)
                            turtle.write(guess, font=("Arial", 25, "normal"))
                            wrongLetters.append(guess)
                            # Changes the spacing between each character for incorrect guesses
                            if spacing < 241:
                                spacing += 30
                            else:
                                spacing = 0
                                rowHeight -= 30
                    # Runs when you had a new incorrect guess
                    if newNumberIncorrect > oldNumberIncorrect:
                        # When the total number of incorrect guesses is 1
                        if newNumberIncorrect == 1:
                            # Draws face
                            turtle.up()
                            turtle.setpos(-125, -10)
                            turtle.pendown()
                            turtle.circle(30)
                        # When the total number of incorrect guesses is 2
                        if newNumberIncorrect == 2:
                            # Draws body
                            turtle.up()
                            turtle.setpos(-125, -10)
                            turtle.pendown()
                            turtle.setpos(-125, -100)
                        # When the total number of incorrect guesses is 3
                        if newNumberIncorrect == 3:
                            # Draws left leg
                            turtle.up()
                            turtle.setpos(-125, -100)
                            turtle.pendown()
                            turtle.setpos(-160, -160)
                        # When the total number of incorrect guesses is 4
                        if newNumberIncorrect == 4:
                            # Draws right leg
                            turtle.up()
                            turtle.setpos(-125, -100)
                            turtle.pendown()
                            turtle.setpos(-90, -160)
                        # When the total number of incorrect guesses is 5
                        if newNumberIncorrect == 5:
                            # Draws left arm
                            turtle.up()
                            turtle.setpos(-125, -35)
                            turtle.pendown()
                            turtle.setpos(-150, -85)
                        # When the total number of incorrect guesses is 6
                        if newNumberIncorrect == 6:
                            # Draws right arm
                            turtle.up()
                            turtle.setpos(-125, -35)
                            turtle.pendown()
                            turtle.setpos(-100, -85)
                        # When the total number of incorrect guesses is 7
                        if newNumberIncorrect == 7:
                            # Draws mouth
                            turtle.up()
                            turtle.setpos(-135, 5)
                            turtle.pendown()
                            turtle.setpos(-115, 5)
            # When the total number of incorrect guesses is 8
            if newNumberIncorrect == 8:
                # Draws left eye
                turtle.up()
                turtle.setpos(-140, 30)
                turtle.pendown()
                turtle.setpos(-130, 20)
                turtle.up()
                turtle.setpos(-130, 30)
                turtle.pendown()
                turtle.setpos(-140, 20)
                # Draws right eye
                turtle.up()
                turtle.setpos(-120, 30)
                turtle.pendown()
                turtle.setpos(-110, 20)
                turtle.up()
                turtle.setpos(-110, 30)
                turtle.pendown()
                turtle.setpos(-120, 20)
                # Fills in the letters
                turtle.up()
                turtle.setpos(-90, -200)
                turtle.write(firstLetter, font=("Arial", 25, "normal"))
                turtle.setpos(-50, -200)
                turtle.write(secondLetter, font=("Arial", 25, "normal"))
                turtle.setpos(-10, -200)
                turtle.write(thirdLetter, font=("Arial", 25, "normal"))
                turtle.setpos(30, -200)
                turtle.write(fourthLetter, font=("Arial", 25, "normal"))
                turtle.setpos(70, -200)
                turtle.write(fifthLetter, font=("Arial", 25, "normal"))
                turtle.setpos(110, -200)
                turtle.write(sixthLetter, font=("Arial", 25, "normal"))
                # Writes "Sorry, you're out of guesses." in the top right corner
                turtle.setpos(-40, 100)
                turtle.pencolor("red")
                turtle.write("Sorry, you're out of guesses.", font=("Arial", 25, "normal"))
            # When you have guessed all the letters
            if newNumberCorrect == wordLength:
                turtle.up()
                turtle.setpos(-20, 100)
                turtle.pencolor("green")
                turtle.write("You guessed correct!!!", font=("Arial", 25, "normal"))

        # 7 letter word
        if wordLength == 7:
            turtle.up()
            turtle.setpos(-100, -200)
            turtle.pendown()
            turtle.setpos(-70, -200)
            turtle.up()
            turtle.setpos(-60, -200)
            turtle.pendown()
            turtle.setpos(-30, -200)
            turtle.up()
            turtle.setpos(-20, -200)
            turtle.pendown()
            turtle.setpos(10, -200)
            turtle.up()
            turtle.setpos(20, -200)
            turtle.pendown()
            turtle.setpos(50, -200)
            turtle.up()
            turtle.setpos(60, -200)
            turtle.pendown()
            turtle.setpos(90, -200)
            turtle.up()
            turtle.setpos(100, -200)
            turtle.pendown()
            turtle.setpos(130, -200)
            turtle.up()
            turtle.setpos(140, -200)
            turtle.pendown()
            turtle.setpos(170, -200)
            firstLetter = letters[0]
            secondLetter = letters[1]
            thirdLetter = letters[2]
            fourthLetter = letters[3]
            fifthLetter = letters[4]
            sixthLetter = letters[5]
            seventhLetter = letters[6]
            # Guessing program for a 7 letter word (runs if the guess is one letter, the user has not yet guessed the word
            # and there are less than 8 incorrect guesses/the hangman has not been fully drawn)
            while newNumberCorrect < wordLength and newNumberIncorrect < 8:
                guess = turtle.textinput("", "What is your guess?")  # Guess user input
                guessLength = len(guess)  # Finds the number of letters in the guess
                oldNumberCorrect = newNumberCorrect  # The old number of correct letters is set to the current value
                oldNumberIncorrect = newNumberIncorrect  # The old number of incorrect letter is set to the current value
                if guessLength == 1 and not guess == "":  # Runs if the guess is more than one letter
                    # Checks to see if the guess is the first letter of the word
                    if guess == firstLetter and firstLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(-90, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        firstLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the second letter of the word
                    if guess == secondLetter and secondLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(-50, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        secondLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the third letter of the word
                    if guess == thirdLetter and thirdLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(-10, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        thirdLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the fourth letter of the word
                    if guess == fourthLetter and fourthLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(30, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        fourthLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the fifth letter of the word
                    if guess == fifthLetter and fifthLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(70, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        fifthLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the sixth letter of the word
                    if guess == sixthLetter and sixthLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(110, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        sixthLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the seventh letter of the word
                    if guess == seventhLetter and seventhLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(150, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        seventhLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Runs when you had an incorrect guess (the number of correct letters has not changed)
                    if newNumberCorrect == oldNumberCorrect and not guess in wrongLetters:
                        if guess == firstLetter or guess == secondLetter or guess == thirdLetter or guess == fourthLetter or guess == fifthLetter or guess == sixthLetter or guess == seventhLetter:
                            newNumberIncorrect = newNumberIncorrect
                        else:
                            newNumberIncorrect += 1
                            turtle.up()
                            turtle.setpos(spacing, rowHeight)
                            turtle.write(guess, font=("Arial", 25, "normal"))
                            wrongLetters.append(guess)
                            # Changes the spacing between each character for incorrect guesses
                            if spacing < 241:
                                spacing += 30
                            else:
                                spacing = 0
                                rowHeight -= 30
                    # Runs when you had a new incorrect guess
                    if newNumberIncorrect > oldNumberIncorrect:
                        # When the total number of incorrect guesses is 1
                        if newNumberIncorrect == 1:
                            # Draws face
                            turtle.up()
                            turtle.setpos(-125, -10)
                            turtle.pendown()
                            turtle.circle(30)
                        # When the total number of incorrect guesses is 2
                        if newNumberIncorrect == 2:
                            # Draws body
                            turtle.up()
                            turtle.setpos(-125, -10)
                            turtle.pendown()
                            turtle.setpos(-125, -100)
                        # When the total number of incorrect guesses is 3
                        if newNumberIncorrect == 3:
                            # Draws left leg
                            turtle.up()
                            turtle.setpos(-125, -100)
                            turtle.pendown()
                            turtle.setpos(-160, -160)
                        # When the total number of incorrect guesses is 4
                        if newNumberIncorrect == 4:
                            # Draws right leg
                            turtle.up()
                            turtle.setpos(-125, -100)
                            turtle.pendown()
                            turtle.setpos(-90, -160)
                        # When the total number of incorrect guesses is 5
                        if newNumberIncorrect == 5:
                            # Draws left arm
                            turtle.up()
                            turtle.setpos(-125, -35)
                            turtle.pendown()
                            turtle.setpos(-150, -85)
                        # When the total number of incorrect guesses is 6
                        if newNumberIncorrect == 6:
                            # Draws right arm
                            turtle.up()
                            turtle.setpos(-125, -35)
                            turtle.pendown()
                            turtle.setpos(-100, -85)
                        # When the total number of incorrect guesses is 7
                        if newNumberIncorrect == 7:
                            # Draws mouth
                            turtle.up()
                            turtle.setpos(-135, 5)
                            turtle.pendown()
                            turtle.setpos(-115, 5)
            # When the total number of incorrect guesses is 8
            if newNumberIncorrect == 8:
                # Draws left eye
                turtle.up()
                turtle.setpos(-140, 30)
                turtle.pendown()
                turtle.setpos(-130, 20)
                turtle.up()
                turtle.setpos(-130, 30)
                turtle.pendown()
                turtle.setpos(-140, 20)
                # Draws right eye
                turtle.up()
                turtle.setpos(-120, 30)
                turtle.pendown()
                turtle.setpos(-110, 20)
                turtle.up()
                turtle.setpos(-110, 30)
                turtle.pendown()
                turtle.setpos(-120, 20)
                # Fills in the letters
                turtle.up()
                turtle.setpos(-90, -200)
                turtle.write(firstLetter, font=("Arial", 25, "normal"))
                turtle.setpos(-50, -200)
                turtle.write(secondLetter, font=("Arial", 25, "normal"))
                turtle.setpos(-10, -200)
                turtle.write(thirdLetter, font=("Arial", 25, "normal"))
                turtle.setpos(30, -200)
                turtle.write(fourthLetter, font=("Arial", 25, "normal"))
                turtle.setpos(70, -200)
                turtle.write(fifthLetter, font=("Arial", 25, "normal"))
                turtle.setpos(110, -200)
                turtle.write(sixthLetter, font=("Arial", 25, "normal"))
                turtle.setpos(150, -200)
                turtle.write(seventhLetter, font=("Arial", 25, "normal"))
                # Writes "Sorry, you're out of guesses." in the top right corner
                turtle.setpos(-40, 100)
                turtle.pencolor("red")
                turtle.write("Sorry, you're out of guesses.", font=("Arial", 25, "normal"))
            # When you have guessed all the letters
            if newNumberCorrect == wordLength:
                turtle.up()
                turtle.setpos(-20, 100)
                turtle.pencolor("green")
                turtle.write("You guessed correct!!!", font=("Arial", 25, "normal"))

        # 8 letter word
        if wordLength == 8:
            turtle.up()
            turtle.setpos(-100, -200)
            turtle.pendown()
            turtle.setpos(-70, -200)
            turtle.up()
            turtle.setpos(-60, -200)
            turtle.pendown()
            turtle.setpos(-30, -200)
            turtle.up()
            turtle.setpos(-20, -200)
            turtle.pendown()
            turtle.setpos(10, -200)
            turtle.up()
            turtle.setpos(20, -200)
            turtle.pendown()
            turtle.setpos(50, -200)
            turtle.up()
            turtle.setpos(60, -200)
            turtle.pendown()
            turtle.setpos(90, -200)
            turtle.up()
            turtle.setpos(100, -200)
            turtle.pendown()
            turtle.setpos(130, -200)
            turtle.up()
            turtle.setpos(140, -200)
            turtle.pendown()
            turtle.setpos(170, -200)
            turtle.up()
            turtle.setpos(180, -200)
            turtle.pendown()
            turtle.setpos(210, -200)
            firstLetter = letters[0]
            secondLetter = letters[1]
            thirdLetter = letters[2]
            fourthLetter = letters[3]
            fifthLetter = letters[4]
            sixthLetter = letters[5]
            seventhLetter = letters[6]
            eighthLetter = letters[7]
            # Guessing program for a 8 letter word (runs if the guess is one letter, the user has not yet guessed the word
            # and there are less than 8 incorrect guesses/the hangman has not been fully drawn)
            while newNumberCorrect < wordLength and newNumberIncorrect < 8:
                guess = turtle.textinput("", "What is your guess?")  # Guess user input
                guessLength = len(guess)  # Finds the number of letters in the guess
                oldNumberCorrect = newNumberCorrect  # The old number of correct letters is set to the current value
                oldNumberIncorrect = newNumberIncorrect  # The old number of incorrect letter is set to the current value
                if guessLength == 1 and not guess == "":  # Runs if the guess is more than one letter
                    # Checks to see if the guess is the first letter of the word
                    if guess == firstLetter and firstLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(-90, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        firstLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the second letter of the word
                    if guess == secondLetter and secondLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(-50, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        secondLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the third letter of the word
                    if guess == thirdLetter and thirdLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(-10, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        thirdLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the fourth letter of the word
                    if guess == fourthLetter and fourthLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(30, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        fourthLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the fifth letter of the word
                    if guess == fifthLetter and fifthLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(70, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        fifthLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the sixth letter of the word
                    if guess == sixthLetter and sixthLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(110, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        sixthLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the seventh letter of the word
                    if guess == seventhLetter and seventhLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(150, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        seventhLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the eighth letter of the word
                    if guess == eighthLetter and eighthLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(190, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        eighthLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Runs when you had an incorrect guess (the number of correct letters has not changed)
                    if newNumberCorrect == oldNumberCorrect and not guess in wrongLetters:
                        if guess == firstLetter or guess == secondLetter or guess == thirdLetter or guess == fourthLetter or guess == fifthLetter or guess == sixthLetter or guess == seventhLetter or guess == eighthLetter:
                            newNumberIncorrect = newNumberIncorrect
                        else:
                            newNumberIncorrect += 1
                            turtle.up()
                            turtle.setpos(spacing, rowHeight)
                            turtle.write(guess, font=("Arial", 25, "normal"))
                            wrongLetters.append(guess)
                            # Changes the spacing between each character for incorrect guesses
                            if spacing < 241:
                                spacing += 30
                            else:
                                spacing = 0
                                rowHeight -= 30
                    # Runs when you had a new incorrect guess
                    if newNumberIncorrect > oldNumberIncorrect:
                        # When the total number of incorrect guesses is 1
                        if newNumberIncorrect == 1:
                            # Draws face
                            turtle.up()
                            turtle.setpos(-125, -10)
                            turtle.pendown()
                            turtle.circle(30)
                        # When the total number of incorrect guesses is 2
                        if newNumberIncorrect == 2:
                            # Draws body
                            turtle.up()
                            turtle.setpos(-125, -10)
                            turtle.pendown()
                            turtle.setpos(-125, -100)
                        # When the total number of incorrect guesses is 3
                        if newNumberIncorrect == 3:
                            # Draws left leg
                            turtle.up()
                            turtle.setpos(-125, -100)
                            turtle.pendown()
                            turtle.setpos(-160, -160)
                        # When the total number of incorrect guesses is 4
                        if newNumberIncorrect == 4:
                            # Draws right leg
                            turtle.up()
                            turtle.setpos(-125, -100)
                            turtle.pendown()
                            turtle.setpos(-90, -160)
                        # When the total number of incorrect guesses is 5
                        if newNumberIncorrect == 5:
                            # Draws left arm
                            turtle.up()
                            turtle.setpos(-125, -35)
                            turtle.pendown()
                            turtle.setpos(-150, -85)
                        # When the total number of incorrect guesses is 6
                        if newNumberIncorrect == 6:
                            # Draws right arm
                            turtle.up()
                            turtle.setpos(-125, -35)
                            turtle.pendown()
                            turtle.setpos(-100, -85)
                        # When the total number of incorrect guesses is 7
                        if newNumberIncorrect == 7:
                            # Draws mouth
                            turtle.up()
                            turtle.setpos(-135, 5)
                            turtle.pendown()
                            turtle.setpos(-115, 5)
            # When the total number of incorrect guesses is 8
            if newNumberIncorrect == 8:
                # Draws left eye
                turtle.up()
                turtle.setpos(-140, 30)
                turtle.pendown()
                turtle.setpos(-130, 20)
                turtle.up()
                turtle.setpos(-130, 30)
                turtle.pendown()
                turtle.setpos(-140, 20)
                # Draws right eye
                turtle.up()
                turtle.setpos(-120, 30)
                turtle.pendown()
                turtle.setpos(-110, 20)
                turtle.up()
                turtle.setpos(-110, 30)
                turtle.pendown()
                turtle.setpos(-120, 20)
                # Fills in the letters
                turtle.up()
                turtle.setpos(-90, -200)
                turtle.write(firstLetter, font=("Arial", 25, "normal"))
                turtle.setpos(-50, -200)
                turtle.write(secondLetter, font=("Arial", 25, "normal"))
                turtle.setpos(-10, -200)
                turtle.write(thirdLetter, font=("Arial", 25, "normal"))
                turtle.setpos(30, -200)
                turtle.write(fourthLetter, font=("Arial", 25, "normal"))
                turtle.setpos(70, -200)
                turtle.write(fifthLetter, font=("Arial", 25, "normal"))
                turtle.setpos(110, -200)
                turtle.write(sixthLetter, font=("Arial", 25, "normal"))
                turtle.setpos(150, -200)
                turtle.write(seventhLetter, font=("Arial", 25, "normal"))
                turtle.setpos(190, -200)
                turtle.write(eighthLetter, font=("Arial", 25, "normal"))
                # Writes "Sorry, you're out of guesses." in the top right corner
                turtle.setpos(-40, 100)
                turtle.pencolor("red")
                turtle.write("Sorry, you're out of guesses.", font=("Arial", 25, "normal"))
            # When you have guessed all the letters
            if newNumberCorrect == wordLength:
                turtle.up()
                turtle.setpos(-20, 100)
                turtle.pencolor("green")
                turtle.write("You guessed correct!!!", font=("Arial", 25, "normal"))

        # 9 letter word
        if wordLength == 9:
            turtle.up()
            turtle.setpos(-100, -200)
            turtle.pendown()
            turtle.setpos(-70, -200)
            turtle.up()
            turtle.setpos(-60, -200)
            turtle.pendown()
            turtle.setpos(-30, -200)
            turtle.up()
            turtle.setpos(-20, -200)
            turtle.pendown()
            turtle.setpos(10, -200)
            turtle.up()
            turtle.setpos(20, -200)
            turtle.pendown()
            turtle.setpos(50, -200)
            turtle.up()
            turtle.setpos(60, -200)
            turtle.pendown()
            turtle.setpos(90, -200)
            turtle.up()
            turtle.setpos(100, -200)
            turtle.pendown()
            turtle.setpos(130, -200)
            turtle.up()
            turtle.setpos(140, -200)
            turtle.pendown()
            turtle.setpos(170, -200)
            turtle.up()
            turtle.setpos(180, -200)
            turtle.pendown()
            turtle.setpos(210, -200)
            turtle.up()
            turtle.setpos(220, -200)
            turtle.pendown()
            turtle.setpos(250, -200)
            firstLetter = letters[0]
            secondLetter = letters[1]
            thirdLetter = letters[2]
            fourthLetter = letters[3]
            fifthLetter = letters[4]
            sixthLetter = letters[5]
            seventhLetter = letters[6]
            eighthLetter = letters[7]
            ninethLetter = letters[8]
            # Guessing program for a 9 letter word (runs if the guess is one letter, the user has not yet guessed the word
            # and there are less than 8 incorrect guesses/the hangman has not been fully drawn)
            while newNumberCorrect < wordLength and newNumberIncorrect < 8:
                guess = turtle.textinput("", "What is your guess?")  # Guess user input
                guessLength = len(guess)  # Finds the number of letters in the guess
                oldNumberCorrect = newNumberCorrect  # The old number of correct letters is set to the current value
                oldNumberIncorrect = newNumberIncorrect  # The old number of incorrect letter is set to the current value
                if guessLength == 1 and not guess == "":  # Runs if the guess is more than one letter
                    # Checks to see if the guess is the first letter of the word
                    if guess == firstLetter and firstLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(-90, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        firstLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the second letter of the word
                    if guess == secondLetter and secondLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(-50, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        secondLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the third letter of the word
                    if guess == thirdLetter and thirdLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(-10, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        thirdLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the fourth letter of the word
                    if guess == fourthLetter and fourthLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(30, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        fourthLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the fifth letter of the word
                    if guess == fifthLetter and fifthLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(70, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        fifthLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the sixth letter of the word
                    if guess == sixthLetter and sixthLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(110, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        sixthLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the seventh letter of the word
                    if guess == seventhLetter and seventhLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(150, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        seventhLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the eighth letter of the word
                    if guess == eighthLetter and eighthLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(190, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        eighthLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the nineth letter of the word
                    if guess == ninethLetter and ninethLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(230, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        ninethLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Runs when you had an incorrect guess (the number of correct letters has not changed)
                    if newNumberCorrect == oldNumberCorrect and not guess in wrongLetters:
                        if guess == firstLetter or guess == secondLetter or guess == thirdLetter or guess == fourthLetter or guess == fifthLetter or guess == sixthLetter or guess == seventhLetter or guess == eighthLetter or guess == ninethLetter:
                            newNumberIncorrect = newNumberIncorrect
                        else:
                            newNumberIncorrect += 1
                            turtle.up()
                            turtle.setpos(spacing, rowHeight)
                            turtle.write(guess, font=("Arial", 25, "normal"))
                            wrongLetters.append(guess)
                            # Changes the spacing between each character for incorrect guesses
                            if spacing < 241:
                                spacing += 30
                            else:
                                spacing = 0
                                rowHeight -= 30
                    # Runs when you had a new incorrect guess
                    if newNumberIncorrect > oldNumberIncorrect:
                        # When the total number of incorrect guesses is 1
                        if newNumberIncorrect == 1:
                            # Draws face
                            turtle.up()
                            turtle.setpos(-125, -10)
                            turtle.pendown()
                            turtle.circle(30)
                        # When the total number of incorrect guesses is 2
                        if newNumberIncorrect == 2:
                            # Draws body
                            turtle.up()
                            turtle.setpos(-125, -10)
                            turtle.pendown()
                            turtle.setpos(-125, -100)
                        # When the total number of incorrect guesses is 3
                        if newNumberIncorrect == 3:
                            # Draws left leg
                            turtle.up()
                            turtle.setpos(-125, -100)
                            turtle.pendown()
                            turtle.setpos(-160, -160)
                        # When the total number of incorrect guesses is 4
                        if newNumberIncorrect == 4:
                            # Draws right leg
                            turtle.up()
                            turtle.setpos(-125, -100)
                            turtle.pendown()
                            turtle.setpos(-90, -160)
                        # When the total number of incorrect guesses is 5
                        if newNumberIncorrect == 5:
                            # Draws left arm
                            turtle.up()
                            turtle.setpos(-125, -35)
                            turtle.pendown()
                            turtle.setpos(-150, -85)
                        # When the total number of incorrect guesses is 6
                        if newNumberIncorrect == 6:
                            # Draws right arm
                            turtle.up()
                            turtle.setpos(-125, -35)
                            turtle.pendown()
                            turtle.setpos(-100, -85)
                        # When the total number of incorrect guesses is 7
                        if newNumberIncorrect == 7:
                            # Draws mouth
                            turtle.up()
                            turtle.setpos(-135, 5)
                            turtle.pendown()
                            turtle.setpos(-115, 5)
            # When the total number of incorrect guesses is 8
            if newNumberIncorrect == 8:
                # Draws left eye
                turtle.up()
                turtle.setpos(-140, 30)
                turtle.pendown()
                turtle.setpos(-130, 20)
                turtle.up()
                turtle.setpos(-130, 30)
                turtle.pendown()
                turtle.setpos(-140, 20)
                # Draws right eye
                turtle.up()
                turtle.setpos(-120, 30)
                turtle.pendown()
                turtle.setpos(-110, 20)
                turtle.up()
                turtle.setpos(-110, 30)
                turtle.pendown()
                turtle.setpos(-120, 20)
                # Fills in the letters
                turtle.up()
                turtle.setpos(-90, -200)
                turtle.write(firstLetter, font=("Arial", 25, "normal"))
                turtle.setpos(-50, -200)
                turtle.write(secondLetter, font=("Arial", 25, "normal"))
                turtle.setpos(-10, -200)
                turtle.write(thirdLetter, font=("Arial", 25, "normal"))
                turtle.setpos(30, -200)
                turtle.write(fourthLetter, font=("Arial", 25, "normal"))
                turtle.setpos(70, -200)
                turtle.write(fifthLetter, font=("Arial", 25, "normal"))
                turtle.setpos(110, -200)
                turtle.write(sixthLetter, font=("Arial", 25, "normal"))
                turtle.setpos(150, -200)
                turtle.write(seventhLetter, font=("Arial", 25, "normal"))
                turtle.setpos(190, -200)
                turtle.write(eighthLetter, font=("Arial", 25, "normal"))
                turtle.setpos(230, -200)
                turtle.write(ninethLetter, font=("Arial", 25, "normal"))
                # Writes "Sorry, you're out of guesses." in the top right corner
                turtle.setpos(-40, 100)
                turtle.pencolor("red")
                turtle.write("Sorry, you're out of guesses.", font=("Arial", 25, "normal"))
            # When you have guessed all the letters
            if newNumberCorrect == wordLength:
                turtle.up()
                turtle.setpos(-20, 100)
                turtle.pencolor("green")
                turtle.write("You guessed correct!!!", font=("Arial", 25, "normal"))

        # 10 letter word
        if wordLength == 10:
            turtle.up()
            turtle.setpos(-100, -200)
            turtle.pendown()
            turtle.setpos(-70, -200)
            turtle.up()
            turtle.setpos(-60, -200)
            turtle.pendown()
            turtle.setpos(-30, -200)
            turtle.up()
            turtle.setpos(-20, -200)
            turtle.pendown()
            turtle.setpos(10, -200)
            turtle.up()
            turtle.setpos(20, -200)
            turtle.pendown()
            turtle.setpos(50, -200)
            turtle.up()
            turtle.setpos(60, -200)
            turtle.pendown()
            turtle.setpos(90, -200)
            turtle.up()
            turtle.setpos(100, -200)
            turtle.pendown()
            turtle.setpos(130, -200)
            turtle.up()
            turtle.setpos(140, -200)
            turtle.pendown()
            turtle.setpos(170, -200)
            turtle.up()
            turtle.setpos(180, -200)
            turtle.pendown()
            turtle.setpos(210, -200)
            turtle.up()
            turtle.setpos(220, -200)
            turtle.pendown()
            turtle.setpos(250, -200)
            turtle.up()
            turtle.setpos(260, -200)
            turtle.pendown()
            turtle.setpos(290, -200)
            firstLetter = letters[0]
            secondLetter = letters[1]
            thirdLetter = letters[2]
            fourthLetter = letters[3]
            fifthLetter = letters[4]
            sixthLetter = letters[5]
            seventhLetter = letters[6]
            eighthLetter = letters[7]
            ninethLetter = letters[8]
            tenthLetter = letters[9]
            # Guessing program for a 10 letter word (runs if the guess is one letter, the user has not yet guessed the word
            # and there are less than 8 incorrect guesses/the hangman has not been fully drawn)
            while newNumberCorrect < wordLength and newNumberIncorrect < 8:
                guess = turtle.textinput("", "What is your guess?")  # Guess user input
                guessLength = len(guess)  # Finds the number of letters in the guess
                oldNumberCorrect = newNumberCorrect  # The old number of correct letters is set to the current value
                oldNumberIncorrect = newNumberIncorrect  # The old number of incorrect letter is set to the current value
                if guessLength == 1 and not guess == "":  # Runs if the guess is more than one letter
                    # Checks to see if the guess is the first letter of the word
                    if guess == firstLetter and firstLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(-90, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        firstLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the second letter of the word
                    if guess == secondLetter and secondLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(-50, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        secondLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the third letter of the word
                    if guess == thirdLetter and thirdLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(-10, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        thirdLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the fourth letter of the word
                    if guess == fourthLetter and fourthLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(30, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        fourthLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the fifth letter of the word
                    if guess == fifthLetter and fifthLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(70, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        fifthLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the sixth letter of the word
                    if guess == sixthLetter and sixthLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(110, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        sixthLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the seventh letter of the word
                    if guess == seventhLetter and seventhLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(150, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        seventhLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the eighth letter of the word
                    if guess == eighthLetter and eighthLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(190, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        eighthLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the nineth letter of the word
                    if guess == ninethLetter and ninethLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(230, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        ninethLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Checks to see if the guess is the tenth letter of the word
                    if guess == tenthLetter and tenthLetterCorrect == 0:
                        newNumberCorrect += 1
                        turtle.up()
                        turtle.setpos(270, -200)
                        turtle.write(guess, font=("Arial", 25, "normal"))
                        tenthLetterCorrect = 1  # Ensures that you don't get another letter correct by entering the same letter again
                    # Runs when you had an incorrect guess (the number of correct letters has not changed)
                    if newNumberCorrect == oldNumberCorrect and not guess in wrongLetters:
                        if guess == firstLetter or guess == secondLetter or guess == thirdLetter or guess == fourthLetter or guess == fifthLetter or guess == sixthLetter or guess == seventhLetter or guess == eighthLetter or guess == ninethLetter or guess == tenthLetter:
                            newNumberIncorrect = newNumberIncorrect
                        else:
                            newNumberIncorrect += 1
                            turtle.up()
                            turtle.setpos(spacing, rowHeight)
                            turtle.write(guess, font=("Arial", 25, "normal"))
                            wrongLetters.append(guess)
                            # Changes the spacing between each character for incorrect guesses
                            if spacing < 241:
                                spacing += 30
                            else:
                                spacing = 0
                                rowHeight -= 30
                    # Runs when you had a new incorrect guess
                    if newNumberIncorrect > oldNumberIncorrect:
                        # When the total number of incorrect guesses is 1
                        if newNumberIncorrect == 1:
                            # Draws face
                            turtle.up()
                            turtle.setpos(-125, -10)
                            turtle.pendown()
                            turtle.circle(30)
                        # When the total number of incorrect guesses is 2
                        if newNumberIncorrect == 2:
                            # Draws body
                            turtle.up()
                            turtle.setpos(-125, -10)
                            turtle.pendown()
                            turtle.setpos(-125, -100)
                        # When the total number of incorrect guesses is 3
                        if newNumberIncorrect == 3:
                            # Draws left leg
                            turtle.up()
                            turtle.setpos(-125, -100)
                            turtle.pendown()
                            turtle.setpos(-160, -160)
                        # When the total number of incorrect guesses is 4
                        if newNumberIncorrect == 4:
                            # Draws right leg
                            turtle.up()
                            turtle.setpos(-125, -100)
                            turtle.pendown()
                            turtle.setpos(-90, -160)
                        # When the total number of incorrect guesses is 5
                        if newNumberIncorrect == 5:
                            # Draws left arm
                            turtle.up()
                            turtle.setpos(-125, -35)
                            turtle.pendown()
                            turtle.setpos(-150, -85)
                        # When the total number of incorrect guesses is 6
                        if newNumberIncorrect == 6:
                            # Draws right arm
                            turtle.up()
                            turtle.setpos(-125, -35)
                            turtle.pendown()
                            turtle.setpos(-100, -85)
                        # When the total number of incorrect guesses is 7
                        if newNumberIncorrect == 7:
                            # Draws mouth
                            turtle.up()
                            turtle.setpos(-135, 5)
                            turtle.pendown()
                            turtle.setpos(-115, 5)
            # When the total number of incorrect guesses is 8
            if newNumberIncorrect == 8:
                # Draws left eye
                turtle.up()
                turtle.setpos(-140, 30)
                turtle.pendown()
                turtle.setpos(-130, 20)
                turtle.up()
                turtle.setpos(-130, 30)
                turtle.pendown()
                turtle.setpos(-140, 20)
                # Draws right eye
                turtle.up()
                turtle.setpos(-120, 30)
                turtle.pendown()
                turtle.setpos(-110, 20)
                turtle.up()
                turtle.setpos(-110, 30)
                turtle.pendown()
                turtle.setpos(-120, 20)
                # Fills in the letters
                turtle.up()
                turtle.setpos(-90, -200)
                turtle.write(firstLetter, font=("Arial", 25, "normal"))
                turtle.setpos(-50, -200)
                turtle.write(secondLetter, font=("Arial", 25, "normal"))
                turtle.setpos(-10, -200)
                turtle.write(thirdLetter, font=("Arial", 25, "normal"))
                turtle.setpos(30, -200)
                turtle.write(fourthLetter, font=("Arial", 25, "normal"))
                turtle.setpos(70, -200)
                turtle.write(fifthLetter, font=("Arial", 25, "normal"))
                turtle.setpos(110, -200)
                turtle.write(sixthLetter, font=("Arial", 25, "normal"))
                turtle.setpos(150, -200)
                turtle.write(seventhLetter, font=("Arial", 25, "normal"))
                turtle.setpos(190, -200)
                turtle.write(eighthLetter, font=("Arial", 25, "normal"))
                turtle.setpos(230, -200)
                turtle.write(ninethLetter, font=("Arial", 25, "normal"))
                turtle.setpos(270, -200)
                turtle.write(tenthLetter, font=("Arial", 25, "normal"))
                # Writes "Sorry, you're out of guesses." in the top right corner
                turtle.setpos(-40, 100)
                turtle.pencolor("red")
                turtle.write("Sorry, you're out of guesses.", font=("Arial", 25, "normal"))
            # When you have guessed all the letters
            if newNumberCorrect == wordLength:
                turtle.up()
                turtle.setpos(-20, 100)
                turtle.pencolor("green")
                turtle.write("You guessed correct!!!", font=("Arial", 25, "normal"))
