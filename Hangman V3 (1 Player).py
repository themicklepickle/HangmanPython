# import modules
import string
import turtle

from random_word import RandomWords

guessedLetters = []


def setup():
    # setup turtle settings
    turtle.shape("blank")
    turtle.setup(width=1.0, height=1.0, startx=0, starty=0)
    turtle.title("Hangman! V2 1 Player")
    turtle.clear()
    turtle.pencolor("black")
    turtle.pensize(4)
    turtle.speed(0)

    # write title
    turtle.up()
    turtle.setpos(-75, 200)
    turtle.write("Hangman!", font=("Arial", 30, "normal"))

    # draw frame
    turtle.setpos(-125, 50)
    turtle.pendown()
    turtle.setpos(-125, 100)
    turtle.setpos(-250, 100)
    turtle.setpos(-250, -200)
    turtle.up()
    turtle.setpos(-300, -200)
    turtle.pendown()
    turtle.setpos(-150, -200)

    # draw dashes
    for i in range(len(word)):
        turtle.up()
        turtle.setpos(-100 + 30 * i, -200 + 10 * i)
        turtle.pendown()
        turtle.setpos(-100 + 30 * i, -200 + 10 * i)

    # generate random word
    word = RandomWords().get_random_word(hasDictionaryDef="true", minLength=3, maxLength=10, minDictionaryCount=8,
                                         includePartOfSpeech="noun,verb,adjective")


def fill_letters():
    turtle.up()
    for i in range(len(word)):
        turtle.setpos(-90 + i * 40, -200)
        turtle.write(word[i], font=("Arial", 25, "normal"))


def play_again():
    while True:
        again = turtle.textinput("", "Play again? (y/n)")
        if again == "y":
            return True
        if again == "n":
            return False


def guess():
    while True:
        guess = turtle.textinput("", "What is your guess?").lower()
        if len(guess) == 1 and guess in string.ascii_lowercase and guess not in guessedLetters:
            break
    for letter in word:
        if guess == letter:
            guessedLetters.append(letter)
            turtle.up()
            turtle.setpos(-90 + 40 * word.index(letter), -200)
            turtle.write(guess, font=("Arial", 25, "normal"))
            word[word.index(letter)] = " "
        else:
            guessedLetters.append(letter)
            turtle.up()
            turtle.setpos(spacing, -30)
            turtle.write(guess, font=("Arial", 25, "normal"))


def win():
    turtle.up()
    turtle.setpos(-20, 100)
    turtle.pencolor("green")
    turtle.write("You guessed correct!!!", font=("Arial", 25, "normal"))


def lose():
    turtle.setpos(-40, 100)
    turtle.pencolor("red")
    turtle.write("Sorry, you're out of guesses.", font=("Arial", 25, "normal"))

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


# Sets the variable
oldCorrectLetters = newCorrectLetters

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
