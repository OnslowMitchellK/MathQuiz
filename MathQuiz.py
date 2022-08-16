##
# Math Quiz
# 7/6/2022
# Mitchell Kan
# This program is a math quiz game where the user gets asked a math question
# and the user has to guess right or they lose points. There are also random
# bonus multipliers to help the user reach 100 points faster in order to win.

import random
from random import randint
import os
import time
import sys

numbers_list = []
operators_list = []
operators = ['+', '-', '*']
BONUSES = {'Double or Nothing': 'Double your points or lose them all!',
           'Double Points Multiplier': 'Double points for 2 questions!',
           'Triple Points Multiplier': 'Triple points for 1 question!',
           'Sudden Death': 'Get the next question correct or else it ends!',
           'Instant +5 Points': 'Instantly obtain 5 points!'}
NO = ["no", "n"]
YES = ["yes", "y"]
NUMBER_MAX = 99
NUMBER_MIN = 1
OPERATOR_MAX = 2
OPERATOR_MIN = 0
FIVE_POINTS = 5
points = 0
counter = 1
print("""\033\n[1mWelcome to the Super Hard Math Quiz\033[0m
---------------------------------------------------------------------------
Info:
You will gain a point after each correct answer.
You will lose 5 points after each incorrect answer.
You will be offered a random bonus after every 5 correct answers.
You will be asked if you would like to continue after every 10 questions.
\033\n[1mNOTE: You cannot drop below 0 points\033[0m
---------------------------------------------------------------------------""")


def generate_numbers():
    """
    Generates three random numbers for the math equation.
    """
    while len(numbers_list) < 3:
        random_number = str(randint(NUMBER_MIN, NUMBER_MAX))
        numbers_list.append(random_number)


def generate_operators():
    """
    Generates random number that corresponds to a operator two times
    for the math equation.
    """
    while len(operators_list) < 2:
        random_operator = randint(OPERATOR_MIN, OPERATOR_MAX)
        operators_list.append(random_operator)


def list_clear():
    """
    Clears the list for numbers and operators.
    """
    numbers_list.clear()
    operators_list.clear()


def resume():
    """
    Asks the user if they would like to continue playing or quit
    """
    while True:
        try:
            resume = input("\nWould you still like to " +
                           "continue? (Y/N) ").lower().strip()
            print("")
            if resume in YES:
                break
            elif resume in NO:
                print("\nThank you for playing this math quiz")
                sys.exit()
        except Exception:
            print("Invalid input")


def bonus():
    """
    Asks user if they would like a bonus, if no, they will continue
    the quiz with no bonus, if yes, randomly choose a bonus and apply
    to user.
    """
    print("\033[1mYou have won a random bonus!\033[0m")
    print("(Some of these can cause you to lose and there is no return)\n")
    global points
    while True:
        try:
            bonus_confirm = input("Would you like to " +
                                  "redeem it (Y/N)? ").strip().lower()
            if bonus_confirm in YES:
                # https://stackoverflow.com/questions/4859292/how-to-get-a-random-value-from-dictionary
                rand_bonus, description = random.choice(list(BONUSES.items()))
                print("\nCongratulations, you have "
                      f"won the following bonus: {rand_bonus}")
                print(f"{description}\n")
                time.sleep(5)
                break
            elif bonus_confirm in NO:
                break
        except Exception:
            print("Invalid input\n")
    if rand_bonus == list(BONUSES.keys())[0]:
        DON()
    elif rand_bonus == list(BONUSES.keys())[1]:
        DPM()
    elif rand_bonus == list(BONUSES.keys())[2]:
        TPM()
    elif rand_bonus == list(BONUSES.keys())[3]:
        SD()
    elif rand_bonus == list(BONUSES.keys())[4]:
        points += FIVE_POINTS


def DON():
    """
    Function for Double or Nothing bonus multiplier,
    Makes two random numbers and makes the user guess
    the answer of the two multiplied together. If the
    user gets it correct, they double their current
    amount of points, if it is wrong, they lose all
    of their current points.
    """
    global points
    print("This special question will be extrememly hard")
    print("You only get one try")
    number_one = randint(100, 1000)
    number_two = randint(1, 10)
    answer = number_one*number_two
    while True:
        try:
            user_answer = int(input(f"What is {number_one} * {number_two}? "))
            if user_answer == answer:
                points = points*2
                print(f"Amazing!!! You are now on {points} points!")
                break
            else:
                points = 0
                print("\nWhat unfortunate news, you are now on 0 points")
                break
        except Exception:
            print("Please enter valid interger\n")


def DPM():
    """
    Double Points Multiplier, it's activated
    for two questions and basically has the same
    coding as math_equation() but the points
    are just changed to 2 instead of 1. After 2
    questions it will go back to normal points.
    """
    global counter
    global points
    multiplier = 2
    while multiplier != 0:
        generate_numbers()
        generate_operators()
        try:
            answer = int(eval(numbers_list[0] +
                              operators[operators_list[0]] +
                              numbers_list[1] +
                              operators[operators_list[1]] +
                              numbers_list[2]))
            # https://stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python
            print(f'\033\n[1m  Question {counter}  \033[0m')
            user_input = int(input(f"{numbers_list[0]} " +
                                   f"{operators[operators_list[0]]} " +
                                   f"{numbers_list[1]} " +
                                   f"{operators[operators_list[1]]} " +
                                   f"{numbers_list[2]} = "))
            if user_input == answer:
                print("CORRECT!!! You have gained 2 points " +
                      "with the multiplier!\n")
                points += 2
                list_clear()
                if points >= 100:
                    gigachad()
            else:
                if points != 0:
                    points -= 5
                if points < 0:
                    points = 0
                print("Wrong!!! minus 5 points!!! " +
                      f"you now have {points} points!!!")
                print(f"The correct answer was \033[1m{answer}\033\n[0m")
                list_clear()
            counter += 1
            multiplier -= 1
        except Exception:
            print("Please enter valid interger\n")
    print("Your bonus has run out")


def TPM():
    """
    Triple Points Multiplier, it's activated
    for one question and basically has the same
    coding as math_equation() but the points
    are just changed to 3 instead of 1. After 1
    question it will go back to normal points.
    """
    global counter
    global points
    multiplier = 1
    list_clear()
    generate_numbers()
    generate_operators()
    while multiplier != 0:
        try:
            answer = int(eval(numbers_list[0] +
                              operators[operators_list[0]] +
                              numbers_list[1] +
                              operators[operators_list[1]] +
                              numbers_list[2]))
            # https://stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python
            print(f'\033\n[1m  Question {counter}  \033[0m')
            user_input = int(input(f"{numbers_list[0]} " +
                                   f"{operators[operators_list[0]]} " +
                                   f"{numbers_list[1]} " +
                                   f"{operators[operators_list[1]]} " +
                                   f"{numbers_list[2]} = "))
            if user_input == answer:
                print("CORRECT!!! You have gained 3 points " +
                      "with the multiplier!\n")
                points += 3
                list_clear()
                if points >= 100:
                    gigachad()
            else:
                if points != 0:
                    points -= 5
                if points < 0:
                    points = 0
                print("Wrong!!! minus 5 points!!! " +
                      f"you now have {points} points!!!")
                print(f"The correct answer was \033[1m{answer}\033\n[0m")
                list_clear()
            counter += 1
            multiplier -= 1
        except Exception:
            print("Please enter valid interger\n")
    print("Your bonus has run out")


def SD():
    """
    Sudden Death, the unlucky bonus where
    a hard question is thrown at you and if
    you get it wrong, the whole code ends.
    """
    number_one = randint(1000, 100000)
    number_two = randint(1000, 100000)
    answer = number_one+number_two
    while True:
        try:
            print("This special question will be extrememly hard")
            print("You only get one try")
            user_answer = int(input(f"What is {number_one} + {number_two}? "))
            if user_answer == answer:
                print(f"WOW! You may continue with the quiz")
                break
            elif user_answer != answer:
                print("You were wrong.")
                time.sleep(5)
                sys.exit()
        except Exception:
            print("Please enter valid interger\n")


def gigachad():
    """
    This function is basically the winning screen, it just
    makes the gigachad dude slowly come up on the screen and
    then after it goes up for a bit, it will say thanks for
    playing the quiz.
    """
    distanceFromTop = 20
    while True:
        print("\n" * distanceFromTop)
        print(r"""

__  ______  __  __  _      _______  __
\ \/ / __ \/ / / / | | /| / /  _/ |/ /
 \  / /_/ / /_/ /  | |/ |/ // //    /
 /_/\____/\____/   |__/|__/___/_/|_/

    ⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⠋⠉⠈⠉⠉⠉⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡏⣀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿
    ⣿⣿⣿⢏⣴⣿⣷⠀⠀⠀⠀⠀⢾⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿
    ⣿⣿⣟⣾⣿⡟⠁⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣷⢢⠀⠀⠀⠀⠀⠀⠀⢸⣿
    ⣿⣿⣿⣿⣟⠀⡴⠄⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⣿
    ⣿⣿⣿⠟⠻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⢴⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⣿
    ⣿⣁⡀⠀⠀⢰⢠⣦⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⡄⠀⣴⣶⣿⡄⣿
    ⣿⡋⠀⠀⠀⠎⢸⣿⡆⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⠗⢘⣿⣟⠛⠿⣼
    ⣿⣿⠋⢀⡌⢰⣿⡿⢿⡀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣧⢀⣼
    ⣿⣿⣷⢻⠄⠘⠛⠋⠛⠃⠀⠀⠀⠀⠀⢿⣧⠈⠉⠙⠛⠋⠀⠀⠀⣿⣿⣿⣿⣿
    ⣿⣿⣧⠀⠈⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠀⠀⠀⠀⢀⢃⠀⠀⢸⣿⣿⣿⣿
    ⣿⣿⡿⠀⠴⢗⣠⣤⣴⡶⠶⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡸⠀⣿⣿⣿⣿
    ⣿⣿⣿⡀⢠⣾⣿⠏⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠉⠀⣿⣿⣿⣿
    ⣿⣿⣿⣧⠈⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿
    ⣿⣿⣿⣿⡄⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣦⣄⣀⣀⣀⣀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠙⣿⣿⡟⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠁⠀⠀⠹⣿⠃⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢐⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⠿⠛⠉⠉⠁⠀⢻⣿⡇⠀⠀⠀⠀⠀⠀⢀⠈⣿⣿⡿⠉⠛⠛⠛⠉⠉
    ⣿⡿⠋⠁⠀⠀⢀⣀⣠⡴⣸⣿⣇⡄⠀⠀⠀⠀⢀⡿⠄⠙⠛⠀⣀⣠⣤⣤⠄ """)
        time.sleep(0.1)
        os.system('cls')
        distanceFromTop -= 1
        if distanceFromTop < 0:
            distanceFromTop = 20
        elif distanceFromTop == 0:
            print("""Thank you for playing this math quiz
(Ran out of budget for ths part)""")
            time.sleep(5)
            sys.exit()


def math_equation():
    """
    Activates other functions to generate a math equation. Asks the math
    question and user gets 1 point if they get it correct and if they don't,
    they lose 5 points
    """
    global points
    global counter
    while True:
        try:
            if points >= 100:
                gigachad()
            list_clear()
            generate_numbers()
            generate_operators()
            answer = int(eval(numbers_list[0] + operators[operators_list[0]] +
                              numbers_list[1] + operators[operators_list[1]] +
                              numbers_list[2]))
            # https://stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python
            print(f'\033\n[1m  Question {counter}  \033[0m')
            user_input = int(input(f"{numbers_list[0]} " +
                                   f"{operators[operators_list[0]]} " +
                                   f"{numbers_list[1]} " +
                                   f"{operators[operators_list[1]]} " +
                                   f"{numbers_list[2]} = "))
            if user_input == answer:
                print("CORRECT!!! You have gained 1 point\n")
                points += 1
                list_clear()
                if points >= 100:
                    gigachad()
            else:
                if points != 0:
                    points -= 5
                if points < 0:
                    points = 0
                print("Wrong!!! minus 5 points!!! " +
                      f"you now have {points} points!!!")
                print(f"The correct answer was \033[1m{answer}\033\n[0m")
                list_clear()
            if counter % 10 == 0:
                resume()
            counter += 1
            if points % 5 == 0 and points != 0:
                print(f"You now have {points} points, that means...")
                bonus()
        except Exception:
            print("Please enter valid interger")


math_equation()
