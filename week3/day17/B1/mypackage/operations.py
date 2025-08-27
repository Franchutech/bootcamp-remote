from . import utils

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: división entre cero"
    return a / b


def welcome_user(name):
    return utils.greet(name)