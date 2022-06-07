##
# Math Quiz
# 7/6/2022
# Mitchell Kan
# This programme is a math quiz game where the user gets asked a math question
# and the user has to guess right or they lose points. There is also random
# bonus multipliers to help the user reach 100 points faster in order to win.

import random
numbers_list = []
operators_list = []
operators = ["+", "-", "*"]


def generate_numbers():
    """
    Generates three random numbers for the math equation.
    """
    while len(numbers_list) < 3:
        random_number = random.randint(1, 99)
        numbers_list.append(random_number)


def generate_operators():
    """
    Generates random number that corresponds to a operator two times
    for the math equation.
    """
    while len(operators_list) < 2:
        random_operator = random.randint(0, 2)
        operators_list.append(random_operator)
    print(operators_list)
    print(operators[operators_list[0]])
    print(operators[operators_list[1]])



def math_equation():
    """
    Activates other functions to generate a math equation.
    """
    generate_numbers()
    generate_operators()
    question = int(input(f"What is " +
                         f"{numbers_list[0]} " +
                         f"{operators[operators_list[0]]} " +
                         f"{numbers_list[1]} " +
                         f"{operators[operators_list[1]]} " +
                         f"{numbers_list[2]}? "))
    pass


math_equation()
