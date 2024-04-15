# make a quiz program to study the sin and cos notable angles
# 0, 30, 45, 60, 90, 180, 270, 360
# 0, pi/6, pi/4, pi/3, pi/2, pi, 3pi/2, 2pi
# 0, 1/2, sqrt(2)/2, sqrt(3)/2, 1, 0, -1, 0
# 0, 0.5, 0.707, 0.866, 1, 0, -1, 0
# 0, 0.5, 0.707, 0.866, 1, 0, -1, 0

import random
import math

# make a list of the questions in degrees
questions = ["sin(0)", "sin(30)", "sin(45)", "sin(60)", "sin(90)", "sin(120)", "sin(135)", "sin(150)", "sin(180)",
             "sin(270)", "sin(360)"]

# give radical symbol
answers = [0, "1/2", u"\u221A2/2", u"\u221A3/2", 1, u"\u221A3/2", u"\u221A2/2", "1/2", 0, -1, 0]

# make the program
print("Welcome to the sin and cos quiz!")
print("You will be given a question and you will have to answer it.")
print("You can choose to answer in degrees, radians, or pi.")

# make a variable to keep track of the score
score = 0
# make a variable to keep track of the number of questions
numQuestions = 0

# make a loop to ask the questions in a multiple choice style
while True:
    questionNum = random.randint(0, len(questions) - 1)
    print("What is " + str(questions[questionNum]) + "?")

    correctPlace = random.randint(0, 3)
    for i in range(0, 4):
        if i == correctPlace:
            print(str(i + 1) + ". " + str(answers[questionNum]))
        else:
            ansWithoutCorrect = answers.copy()
            ansWithoutCorrect.remove(answers[questionNum])
            pickedAns = []

            print(str(i + 1) + ". " + str(ansWithoutCorrect[random.randint(0, len(ansWithoutCorrect) - 1)]) + " ")

    answer = input("Your answer: ")

    print(questionNum)
    if answer == correctPlace + 1:
        print("Correct!")
        # add one to the score
        score += 1
    elif answer == "quit":
        break
    else:
        print("Incorrect!")
    # add one to the number of questions
    numQuestions += 1

# print the score
print("Your score is " + str(score) + "/" + str(numQuestions))
