##
# Math Quiz
# 7/6/2022
# Mitchell Kan
# This programme is a math quiz game where the user gets asked a math question
# and the user has to guess right or they lose points. There is also random
# bonus multipliers to help the user reach 100 points faster in order to win.

from random import randint

numbers_list = []
operators_list = []
operators = ['+', '-', '*']
NO = ["no", "n"]
YES = ["yes", "y"]
NUMBER_MAX = 99
NUMBER_MIN = 1
OPERATOR_MAX = 2
OPERATOR_MIN = 0


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
    numbers_list.clear()
    operators_list.clear()


def resume():
    while True:
        try:
            resume = input("Would you still like to " +
                           "continue? (Y/N) ").lower().strip()
            if resume in YES:
                break
            elif resume in NO:
                import sys
                print("\nThank you for using this math quiz")
                sys.exit()
        except Exception:
            print("wd")


def math_equation():
    """
    Activates other functions to generate a math equation.
    """
    counter = 1
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

                print("CORRECT!!! YOU HAVE GAINED 1 POINT\n")
                list_clear()
            else:
                print("WRONG!!! MINUS 5 POINTS!!! YOU NOW HAVE [] POINTS!!!\n")
                list_clear()
            if counter % 10 == 0:
                resume()
            counter += 1
        except Exception:
            print("Please enter a valid input\n")
            counter -= 1


math_equation()
