again = "y"

while again == "y":

    # General setup stuff
    import turtle

    turtle.shape("blank")
    turtle.setup(width=1.0, height=1.0, startx=0, starty=0)
    turtle.title("Hangman! V2 2 Player")
    turtle.clear()
    turtle.pencolor("black")
    turtle.pensize(4)
    turtle.speed(0)

    # Variable defaults
    newNumberCorrect = 0
    newNumberIncorrect = 0
    newCorrectLetters = []
    oldCorrectLetters = []
    spacing = 0
    wrongLetters = []
    dashX = -100
    dashY = -200

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

    # Functions
    def letterCorrect(x, xLetter):
        global newNumberCorrect
        global newCorrectLetters
        global oldCorrectLetters
        y = -200
        if guess == xLetter and not xLetter == " " and not guess in oldCorrectLetters:
            newNumberCorrect += 1
            turtle.up()
            turtle.setpos(x, y)
            turtle.write(guess, font=("Arial", 25, "normal"))
            newCorrectLetters.append(guess)


    # Word setup
    word = turtle.textinput("", "Please enter a word that is between 3 and 10 letters long: ")
    wordLength = len(word)
    while wordLength < 3 or wordLength > 10:
        word = turtle.textinput("",
                                "Sorry, your word must be between 3 and 10 letters long, please enter another word: ")
        wordLength = len(word)
    letters = list(word)

    # Filling the rest of the spaces in the list with " "
    i = 10 - wordLength
    while i > 0:
        letters.append(" ")
        i -= 1

    # Drawing the dashes on the turtle display
    i = 0
    while i < wordLength:
        turtle.up()
        turtle.setpos(dashX, dashY)
        turtle.pendown()
        dashX += 30
        turtle.setpos(dashX, dashY)
        dashX += 10
        i += 1

    # Assigning each letter a variable then setting it to lowercase
    firstLetter = letters[0]
    firstLetter = firstLetter.lower()
    secondLetter = letters[1]
    secondLetter = secondLetter.lower()
    thirdLetter = letters[2]
    thirdLetter = thirdLetter.lower()
    fourthLetter = letters[3]
    fourthLetter = fourthLetter.lower()
    fifthLetter = letters[4]
    fifthLetter = fifthLetter.lower()
    sixthLetter = letters[5]
    sixthLetter = sixthLetter.lower()
    seventhLetter = letters[6]
    seventhLetter = seventhLetter.lower()
    eighthLetter = letters[7]
    eighthLetter = eighthLetter.lower()
    ninethLetter = letters[8]
    ninethLetter = ninethLetter.lower()
    tenthLetter = letters[9]
    tenthLetter = tenthLetter.lower()

    # Guessing algorithm
    while newNumberCorrect < wordLength and newNumberIncorrect < 8:

        # User input for the guess
        guess = turtle.textinput("", "What is your guess?")
        guess = guess.lower()

        # Gets the length of the guess
        guessLength = len(guess)

        if guessLength == 1 and not guess == "":

            # Sets the variable values
            oldNumberCorrect = newNumberCorrect
            oldNumberIncorrect = newNumberIncorrect

            # Calls the function for each letter
            letterCorrect(-90, firstLetter)
            letterCorrect(-50, secondLetter)
            letterCorrect(-10, thirdLetter)
            letterCorrect(30, fourthLetter)
            letterCorrect(70, fifthLetter)
            letterCorrect(110, sixthLetter)
            letterCorrect(150, seventhLetter)
            letterCorrect(190, eighthLetter)
            letterCorrect(230, ninethLetter)
            letterCorrect(270, tenthLetter)

            # Runs if the guess did not match any of the letters and it has not already been guessed
            if newNumberCorrect == oldNumberCorrect and not guess in wrongLetters and not guess in letters:
                newNumberIncorrect += 1
                turtle.up()
                turtle.setpos(spacing, -30)
                turtle.write(guess, font=("Arial", 25, "normal"))
                wrongLetters.append(guess)

                # Changes the spacing between each character for incorrect guesses
                spacing += 30

                # When the total number of incorrect guesses is
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

    # oldCorrectLetters = newCorrectLetters

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

    again = turtle.textinput("", "Play again? (y/n)")
