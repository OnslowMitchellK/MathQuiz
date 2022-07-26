##
# Math Quiz
# 7/6/2022
# Mitchell Kan
# This program is a math quiz game where the user gets asked a math question
# and the user has to guess right or they lose points. There are also random
# bonus multipliers to help the user reach 100 points faster in order to win.

import random
from random import randint

numbers_list = []
operators_list = []
operators = ['+', '-', '*']
BONUSES = {'Double or Nothing': 'Double your points or lose them all!',
           'Double Points Multiplier': 'Double points for 3 questions!',
           'Triple Points Multiplier': 'Triple points for 3 questions!',
           'Sudden Death': 'Get the next question correct or else it ends!',
           'Instant +5 Points': 'Instantly obtain 5 points!'}
NO = ["no", "n"]
YES = ["yes", "y"]
NUMBER_MAX = 99
NUMBER_MIN = 1
OPERATOR_MAX = 2
OPERATOR_MIN = 0


print("""\033\n[1mWelcome to the Math Quiz\033[0m
---------------------------------------------------------------------------
Rules:
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
            if resume in YES:
                break
            elif resume in NO:
                import sys
                print("\nThank you for using this math quiz")
                sys.exit()
        except Exception:
            print("Invalid input")


def bonus():
    """
    Asks user if they would like a bonus, if no, they will continue
    the quiz with no bonus, if yes, randomly choose a bonus and apply
    to user.
    """
    print("\033[1mYou have won a random bonus\033[0m")
    print("(Some of these can cause you to lose and there is no return)\n")
    while True:
        try:
            bonus_confirm = input("Would you like to " +
                                  "redeem it (Y/N)? ").strip().lower()
            if bonus_confirm in YES:
                # https://stackoverflow.com/questions/4859292/how-to-get-a-random-value-from-dictionary
                rand_bonus, description = random.choice(list(BONUSES.items()))
                print(rand_bonus)
                print(description)
                print("\nCongratulations, you have "
                      f"won the following bonus: {rand_bonus}")
                print(description)
            elif bonus_confirm in NO:
                break
        except Exception:
            print("Invalid input\n")


def math_equation():
    """
    Activates other functions to generate a math equation.
    """
    counter = 1
    points = 0
    while True:
        try:
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
            else:
                if points != 0:
                    points -= 5
                if points < 0:
                    points = 0
                print("Wrong!!! minus 5 points!!! " +
                      f"you now have {points} points!!!")
                print(f"The correct answer was \033[1m{answer}\033\n[0m")
                list_clear()
            if points % 5 == 0 and points != 0:
                bonus()
            if counter % 10 == 0:
                resume()
            counter += 1
        except Exception:
            print("Please enter a valid input\n")


math_equation()
