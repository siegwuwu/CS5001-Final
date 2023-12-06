""" 
Final Project: Stock analysis app
===========================
Course:   CS 5001
Student:  Chen Wu
"""


from calculation import calculate, compare_MA
from process_data import date_range, calc_price

_WELCOME_MESSAGE = """Welcome to the stock analysis app."""
_PROMPT = """What would you like to do? (Enter help for help)"""
_HELP_MESSAGE = """
You have the following command options:
    analyze: program will help you analyze a stock
    help: print this help message
    exit: exit the program
""".strip()
_GOODBYE_MESSAGE = """Thank you for using the app"""


def read_file():
    """
    Prompts the user for the file path. Open file and returns a list with
    each line of the file as a string.

    Returns:
        data (list): the list that contains each line of the file
    """
    data = []

    while True:
        try:
            with open(input("Please enter the file path of the stock price data:"), "r") as file:
                for line in file:
                    line = line.strip()
                    data.append(line)
            return data
        except FileNotFoundError:
            print("Invalid path")

def get_date():
    """
    Ptompts the user for the start and end date of their analysis and returns
    a list that contains the two dates

    Return:
        date (list): contain the start and end date the user wants to look at,
                     in the format of YYYY-MM-DD

    """
    start_date, end_date = '', ''
    date = []
    while len(start_date) != 10 or len(start_date.split('-')[0]) != 4 or len(start_date.split('-')[1]) != 2 or len(start_date.split('-')[2]) != 2:
        start_date = input("Please enter the start date of analysis in the format of YYYY-MM-DD:")
    while len(end_date) != 10 or len(end_date.split('-')[0]) != 4 or len(end_date.split('-')[1]) != 2 or len(end_date.split('-')[2]) != 2:
        end_date = input("Please enter the end date of analysis in the format of YYYY-MM-DD:")
    date.append(start_date)
    date.append(end_date)
    return date
        

def menu():
    """
    Prompts the client for their command.

    See HELP_MESSAGE for more options. Will also
    parse the command and return the command and
    any options that were passed in.

    Returns:
        command (string): the string of the command
    """
    command = input(_PROMPT).strip()
    command = command.casefold()
    while command not in ['analyze', 'exit']:
        print(_HELP_MESSAGE)
        command = input(_PROMPT).strip()
        command = command.casefold()
    return command


def run() -> None:
    """
    Runs the stock analysis application.
    """
    print(_WELCOME_MESSAGE)
    command = ''
    while command != 'exit':
        command = menu()
        if command == 'analyze':
            data = read_file()
            dates = get_date()
            data_range = date_range(data, dates)
            calc_input = calc_price(data_range)
            moving_avg = calculate(calc_input)
            result = compare_MA(calc_input, moving_avg)
            for item in result:
                print(item)
    print(_GOODBYE_MESSAGE)


if __name__ == "__main__":
    run()
