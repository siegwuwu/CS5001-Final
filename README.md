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

The process_data.py contains functions that process the data.

The first function is date_range, which cut out the data within the date range entered by the user.

```python
def date_range(data: list, dates: list):
    """
    Reads in a list that contains two dates with the first and second
    elements being the start and end date the user wants to check
    respectively. Creates a new list with elements in data that has date
    between (inclusive) the dates given. Assumes the second date in the dates
    list is greater or equal to the first date in the dates list

    Args:
        data(list): the list that contains all the stock data
        dates(list): the list that contains the two dates

    Returns:
        list: the list that contains elements in data that has date within
        the dates
    """

    data_range = []
    data_range.append(data[0])
    
    first_datum = data[1].split(",")[0] ## Parse the start date of the dataset
    last_datum = data[-1].split(",")[0] ## Parse the last date of the dataset
    start_date = dates[0] ## Parse the start date the user entered
    end_date = dates[1] ## Parse the end date the user entered

    if first_datum <= start_date and last_datum >= start_date:
        date1 = start_date
        ## If start date within the range, the start date is the date entered by the user
    elif first_datum > start_date:
        date1 = first_datum
        print("Start date too old, start date defaulted to the oldest datum")
        ## If the entered start date is too old, start date is defaulted to the oldest date in the dataset
        
    else:
        date1 = last_datum
        print("Start date too recent, start date defaulted to the newest datum")
        ## If the entered start date is too recent, start date is defaulted to the newest date in the dataset

    if last_datum >= end_date and first_datum <= end_date: ## Determine the end date similar to the logic of determining start date
        date2 = end_date
    elif last_datum < end_date:
        date2 = last_datum
        print("End date too recent, end date defaulted to the newest datum")
    else:
        date2 = first_datum
        print("End date too old, end date defaulted to the oldest datum")

    for i in range(len(data)):
        if data[i].split(",")[0] >= date1 and data[i].split(",")[0] <= date2:
            data_range.append(data[i])
        ## Include all data between date1 and date2 (inclusive) in the data_range list

    return data_range
```

The calc_price function cut out the data containing the type of price the user specified.
```python
def calc_price(data: list):
    '''
    Reads in a list that contains the price data and a str that specifies the
    type of price to use for calculation (Open, High, Low, Close, Adj Close).

    Args:
        data_range(list): the list that contains all the stock data
        calc_price(str): the str that specifies the type of price to use

    Returns:
        list: the list that contains only the date and type of price selected
        by calc_price
    '''
    cleaned_input = ''
    while cleaned_input not in ['open', 'high', 'low', 'close', 'adj close']:
        cleaned_input = input("Please enter the type of price to perform the analysis:")
        cleaned_input.lower()
        ## Prompt user to enter the type of price to analysis until the user enter the type that is in the dataset
        
    calc_price_list = []
    col_name = data[0].split(',')
    
    
    if cleaned_input == "open":
        for line in data:
            calc_price_list.append(f"{line.split(',')[col_name.index('Date')]},{line.split(',')[col_name.index('Open')]}")
        return calc_price_list    
    elif cleaned_input == "high":
        for line in data:
            calc_price_list.append(f"{line.split(',')[col_name.index('Date')]},{line.split(',')[col_name.index('High')]}")
        return calc_price_list  
    elif cleaned_input == "low":
        for line in data:
            calc_price_list.append(f"{line.split(',')[col_name.index('Date')]},{line.split(',')[col_name.index('Low')]}")
        return calc_price_list  
    elif cleaned_input == "close":
        for line in data:
            calc_price_list.append(f"{line.split(',')[col_name.index('Date')]},{line.split(',')[col_name.index('Close')]}")
        return calc_price_list
    else:
        for line in data:
            calc_price_list.append(f"{line.split(',')[col_name.index('Date')]},{line.split(',')[col_name.index('Adj Close')]}")
        return calc_price_list
    ## Return the list containing the column of date and the corresponding column of price data based on the user input
```

The calculation.py contains the function to calculate the moving average and function to use the moving average to produce strategies

The calculate_MA function returns a list with the moving average corresponding to each of the price data.
```python
def calculate_MA(data_with_header: list):
    '''
    Reads in a list of price data and a int for range of moving average, return
    a list with the moving average(MA) corresponding to each data in the list

    Args:
        data_with_header (list): list consists of items in the format of 'date,price'
    Reuturns:
        MA: the list of moving average corresponding to the price on each date
        in the Arg: data (list)
    '''
    moving_range = int(input("Please enter the number of days for the moving average:"))
    ## Prompt the user to enter the number of days they want to use for calculating MA
    
    while moving_range <= 0:
            moving_range = int(input("Please enter the number of days for calculating moving average:"))
            ## Ask the user to re-enter the integer if it is <= 0

    data = data_with_header[1:] ## Create a list with the data but without header
    data_len = len(data) ## Get the number of data points in the list
    MA = [',MA'] ## Initialize the MA list with the header
    for i in range(data_len):
    ## Iterate through every data in the list
        
        moving_avg = 0
        ## Initial the moving_avg value as 0
        
        if i >= moving_range:
        ## The case for when the data point has more data points before it than the moving_range specified by the user (the complete moving average can be calcualted)
            range_start = i - moving_range
            while range_start < i:
                moving_avg += float(data[range_start].split(',')[1])
                range_start += 1
            ## Sum the the number of data equal to the moving_range
            
            moving_avg /= moving_range
            ## Average the sum to get the moving average
            
        elif i > 1:
        ## The case when the data point is not the first data point but does not have enough data point before it to calculatet the complete MA
            range_start = 0
            while range_start < i:
                moving_avg += float(data[range_start].split(',')[1])
                ## If the datum does not have enough number of days before, the MA is assumed to be the average of all prices before it
                range_start += 1
            moving_avg /= i
        else:
        ## The case when the data point is the first data point
            
            moving_avg = float(data[0].split(',')[1])
            ## The first price datum is assumed to have MA of the price itself
            
        MA.append(moving_avg)
        ## Append the calculated MA to the MA list
        
    return MA
```

The compare_MA function determines the strategy for each day based on the price and moving average of that day.

```python
def compare_MA(price_data: list, MA_data: list):
    '''
    Reads in a list of price data and a list of the corresponding moving average,
    return a list that indicate the strategy for each date (buy, sell, or hold)

    Args:
        price_data (list): list consists of items in the format of 'date,price'
        MA_data (list): list consists of moving average for each data in price_data
    Reutrns:
        result (list): list consists of strategy corresponding to each item
        in price_data
    '''
    comparison = ['hold'] ## The strategy on the first day is always 'hold' as no previous data point is available
    price_data_number = []
    MA_data_number = []
    header = [price_data[0] + ",MA,Strategy"] ## This is the header (adding MA and Strategy header for the corresponding columns)
    
    for i in range(1, len(price_data)):
        price_data_number.append(float(price_data[i].split(',')[1]))
        ## Parse the price information and store each price as an item in price_data_number (header is excluded)

    for i in range(1, len(MA_data)):
        MA_data_number.append(float(MA_data[i]))
        ## Parse the MA information and store each MA as an item in MA_data_number (header is excluded)

    for i in range(1, len(price_data_number)):
        
        if (price_data_number[i] - MA_data_number[i]) * (price_data_number[i-1] - MA_data_number[i-1]) > 0:
            comparison.append('hold')
            ## If difference between price and MA on day i times difference on day i - 1 is positive, the trend has not changed, so strategy is hold
            
        elif (price_data_number[i] - MA_data_number[i]) * (price_data_number[i-1] - MA_data_number[i-1]) < 0:
            if price_data_number[i-1] - MA_data_number[i-1] > 0:
                comparison.append('sell')
            else:
                comparison.append('buy')
            ## If difference between price and MA on day i times difference on day i - 1 is positive, the trend has changed, so strategy for day i is opposite of day i - 1
                
        else:
            if i == 1:
                comparison.append('hold')
                ## The strategy on the second day (i = 1) is also hold as we cannot determine the trend (either day 1 or day 2 or both day 1 and 2 has difference of 0). 
                
            else:
                if (price_data_number[i] - MA_data_number[i]) * (price_data_number[i-2] - MA_data_number[i-2]) > 0:
                    comparison.append(comparison[i-2])
                elif (price_data_number[i] - MA_data_number[i]) * (price_data_number[i-2] - MA_data_number[i-2]) < 0:
                    if price_data_number[i-2] - MA_data_number[i-2] > 0:
                        comparison.append('sell')
                    else:
                        comparison.append('buy')
                ## Compare the difference on day i - 2 with the difference on day i
                        
                else:
                    comparison.append('hold')
                ## If the difference on day i times the difference on day i - 2 is 0, either day i difference is 0 or day i - 2 and day i - 1 are both zero, in which case would result in hold strategy on day i
    for i in range(1, len(price_data)):
        header.append(f"{price_data[i]},{MA_data_number[i-1]},{comparison[i-1]}")
        
    return header
```

### Major Challenges
Key aspects could include pieces that your struggled on and/or pieces that you are proud of and want to show off.


## Example Runs
Explain how you documented running the project, and what we need to look for in your repository (text output from the project, small videos, links to videos on youtube of you running it, etc)

Below is a sample run of the program. The file used is the S&P/TSX data from 2022-11-23 to 2023-11-22.

```
Welcome to the stock analysis app.
What would you like to do? (Enter help for help):analyze
Please enter the file path of the stock price data:/Users/chenwu/Desktop/MSCS/CS5001/Final/S&P-TSX.csv
Please enter the start date of analysis in the format of YYYY-MM-DD:2022-11-30
Please enter the end date of analysis in the format of YYYY-MM-DD:2022-12-31
Please enter the type of price to perform the analysis:close
Please enter the number of days for the moving average:5
Date,Close,MA,Strategy
2022-11-30,20453.300781,20453.300781,hold
2022-12-01,20525.500000,20453.300781,hold
2022-12-02,20485.699219,20489.4003905,sell
2022-12-05,20242.300781,20488.166666666668,hold
2022-12-06,19990.199219,20426.70019525,hold
2022-12-07,19973.199219,20339.4,hold
2022-12-08,19969.199219,20243.3796876,hold
2022-12-09,19947.099609,20132.1195314,hold
2022-12-12,20019.699219,20024.3996094,hold
2022-12-13,20023.500000,19979.879297,buy
2022-12-14,19891.699219,19986.5394532,sell
2022-12-15,19600.599609,19970.2394532,hold
2022-12-16,19443.300781,19896.5195312,hold
2022-12-19,19200.800781,19795.7597656,hold
2022-12-20,19306.900391,19631.980078,hold
2022-12-21,19571.099609,19488.6601562,buy
2022-12-22,19349.699219,19424.5402342,sell
2022-12-23,19506.699219,19374.3601562,buy
2022-12-28,19284.099609,19387.0398438,sell
2022-12-29,19485.900391,19403.6996094,buy
2022-12-30,19384.900391,19439.4996094,sell
What would you like to do? (Enter help for help):exit
Thank you for using the app
```

## Testing
How did you test your code? What did you do to make sure your code was correct? If you wrote unit tests, you can link to them here. If you did run tests, make sure you document them as text files, and include them in your submission. 

> _Make it easy for us to know you *ran the project* and *tested the project* before you submitted this report!_


## Missing Features / What's Next
Focus on what you didn't get to do, and what you would do if you had more time, or things you would implement in the future. 

## Final Reflection
Write at least a paragraph about your experience in this course. What did you learn? What do you need to do to learn more? Key takeaways? etc.
