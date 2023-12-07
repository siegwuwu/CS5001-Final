# Final Project Report

* Student Name: Chen Wu
* Github Username: siegwuwu
* Semester: 23Fall
* Course: CS5001



## Description 
The final project focuses on building a stock analysis application. It uses the concept of moving averages to guide the trading strategy of the current day (as the data we use is the daily price). The selection of this topic results from a combination of personal trading experience as well as interest in the application of computer science in the finance field.

## Key Features
Highlight some key features of this project that you want to show off/talk about/focus on. 

The key feature of this application is the calculation of simple moving averages (SMA). SMA is the average of the prices of the x days before the current day with the x days being specified by the user based. By comparing the current day price with the SMA, one can understand if a datum is high, low, or equal compared with the SMA. The strategy is to buy a stock on the day when the price turns larger than its SMA or vice versa. This allows the user to buy in when the trend of the price turns into an increasing trend, sell when the trend becomes a decreasing trend, and hold for any other time.

## Guide
How do we run your project? What should we do to see it in action? - Note this isn't installing, this is actual use of the project.. If it is a website, you can point towards the gui, use screenshots, etc talking about features. 

The program consists of three .py files. stock_analysis_app is the file that the user interacts with. Open the file and run it. The program will ask what the user wants to do. From the help message, there are 'analyze', 'help', and 'exit' commands available. 
```
Welcome to the stock analysis app.
What would you like to do? (Enter help for help):help
You have the following command options:
    analyze: program will help you analyze a stock
    help: print this help message
    exit: exit the program
What would you like to do? (Enter help for help):
```
As suggested by the name, the 'analyze' command will start an analysis session. The user will then be prompted to enter the path to the data file. The data format required by the program is as follows:

```
Date,Open,High,Low,Close,Adj Close,Volume
2022-11-23,20185.099609,20303.599609,20185.099609,20282.300781,20282.300781,238316600
2022-11-24,20309.199219,20386.699219,20309.199219,20344.099609,20344.099609,88111700
2022-11-25,20348.900391,20446.300781,20342.199219,20383.800781,20383.800781,157063000
```
The first line is the header separated by commas. The 'Date' column and at least one type of price in the columns beside it are required. The data point in each line should start with the date in the form of YYYY-MM-DD. 

The program will then prompt the user to enter the start and end date of the analysis, the type of price to run the analysis on (typically, 'Close' is used for SMA analysis), and the number of days of the SMA.

```
Please enter the start date of analysis in the format of YYYY-MM-DD:2022-11-30
Please enter the end date of analysis in the format of YYYY-MM-DD:2022-12-30
Please enter the type of price to perform the analysis:close
Please enter the number of days for the moving average:1
```
Upon entering all the information, the program will generate the strategy for each day based on the input. 
```
Date,Close,MA,Strategy
2022-11-30,20453.300781,20453.300781,hold
2022-12-01,20525.500000,20453.300781,hold
2022-12-02,20485.699219,20525.5,sell
2022-12-05,20242.300781,20485.699219,hold
2022-12-06,19990.199219,20242.300781,hold
2022-12-07,19973.199219,19990.199219,hold
2022-12-08,19969.199219,19973.199219,hold
2022-12-09,19947.099609,19969.199219,hold
2022-12-12,20019.699219,19947.099609,buy
2022-12-13,20023.500000,20019.699219,hold
2022-12-14,19891.699219,20023.5,sell
2022-12-15,19600.599609,19891.699219,hold
2022-12-16,19443.300781,19600.599609,hold
2022-12-19,19200.800781,19443.300781,hold
2022-12-20,19306.900391,19200.800781,buy
2022-12-21,19571.099609,19306.900391,hold
2022-12-22,19349.699219,19571.099609,sell
2022-12-23,19506.699219,19349.699219,buy
2022-12-28,19284.099609,19506.699219,sell
2022-12-29,19485.900391,19284.099609,buy
2022-12-30,19384.900391,19485.900391,sell
What would you like to do? (Enter help for help):
```
At the end, the program will ask what further action to take. The user can exit the program as the analysis process is finished.

## Installation Instructions
Place the three .py files under the same folder, and running the stock_analysis_app.py will start the program.

## Code Review
Go over key aspects of code in this section. Both link to the file, include snippets in this report (make sure to use the [coding blocks](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)).  Grading wise, we are looking for that you understand your code and what you did. 

Starting with the stock_analysis_app.py, the file first imports the functions from calculation.py and process_data.py. The strings to be used later are also assigned to global variables.

```python
from calculation import calculate_MA, compare_MA
from process_data import date_range, calc_price
## Import the functions form the other two files

_WELCOME_MESSAGE = """Welcome to the stock analysis app."""
_PROMPT = """What would you like to do? (Enter help for help):"""
_HELP_MESSAGE = """
You have the following command options:
    analyze: program will help you analyze a stock
    help: print this help message
    exit: exit the program
""".strip()
_GOODBYE_MESSAGE = """Thank you for using the app"""
```

The first function is read_file which is used to read the file.

```python
def read_file():
    """
    Prompts the user for the file path. Open file and returns a list containing
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
        ## Prompt the user to enter a file path until the file path is valid
```

The get_date function will ask the user for the start and end date of the analysis and store the two dates in a list.

```python
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
    ## Check the total length and the length of each element with .split('-') to ensure it is in the format of YYYY-MM-DD
    ## Assume the input without the '-' is numeric
    
    date.append(start_date)
    date.append(end_date)
    return date
```

The menu function will get the command from the user.

```python
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
    ## Prompt the user to enter command and clean the input
    
    while command not in ['analyze', 'exit']:
        print(_HELP_MESSAGE)
        command = input(_PROMPT).strip()
        command = command.casefold()
        ## Print help message and ask for input until input is in the list of ['analyze', 'exit']
        
    return command
```

The main function is the main function of the entire program. Running main function will start the program.

```python
def main() -> None:
    """
    Runs the stock analysis application.
    """
    print(_WELCOME_MESSAGE)
    command = ''
    while command != 'exit':
    ## Keep the program running unless user entered 'exit'
        
        command = menu()
        ## Call the menu() function to get input
        if command == 'analyze':
            data = read_file()
            dates = get_date()
            data_range = date_range(data, dates)
            calc_input = calc_price(data_range)
            moving_avg = calculate_MA(calc_input)
            result = compare_MA(calc_input, moving_avg)
            for item in result:
                print(item)
            ## Print out each line of the result list
    print(_GOODBYE_MESSAGE)


if __name__ == "__main__":
    main()
```

### Major Challenges
Key aspects could include pieces that your struggled on and/or pieces that you are proud of and want to show off.


## Example Runs
Explain how you documented running the project, and what we need to look for in your repository (text output from the project, small videos, links to videos on youtube of you running it, etc)

## Testing
How did you test your code? What did you do to make sure your code was correct? If you wrote unit tests, you can link to them here. If you did run tests, make sure you document them as text files, and include them in your submission. 

> _Make it easy for us to know you *ran the project* and *tested the project* before you submitted this report!_


## Missing Features / What's Next
Focus on what you didn't get to do, and what you would do if you had more time, or things you would implement in the future. 

## Final Reflection
Write at least a paragraph about your experience in this course. What did you learn? What do you need to do to learn more? Key takeaways? etc.
