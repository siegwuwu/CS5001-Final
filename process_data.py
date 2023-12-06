""" 
Final Project: Stock analysis app
===========================
Course:   CS 5001
Student:  Chen Wu

This file contains the functions that process the data and convert them to
format used by other functions
"""

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
    
    first_datum = data[1].split(",")[0]
    last_datum = data[-1].split(",")[0]
    start_date = dates[0]
    end_date = dates[1]

 #   print(first_datum, last_datum, start_date, end_date)

    if first_datum <= start_date and last_datum >= start_date:
        date1 = start_date
    elif first_datum > start_date:
        date1 = first_datum
        print("Start date too old, start date defaulted to the oldest datum")
    else:
        date1 = last_datum
        print("Start date too new, start date defaulted to the newest datum")

    if last_datum >= end_date and first_datum <= end_date:
        date2 = end_date
    elif last_datum < end_date:
        date2 = last_datum
        print("End date too new, end date defaulted to the newest datum")
    else:
        date2 = first_datum
        print("End date too old, end date defaulted to the oldest datum")

    for i in range(len(data)):
        if data[i].split(",")[0] >= date1 and data[i].split(",")[0] <= date2:
            data_range.append(data[i])

    return data_range

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
        cleaned_input = calc_price.strip().lower()
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


def main():
    test_list = ['Date,Open,High,Low,Close,Adj Close,Volume',
                 '2022-11-23,20185.099609,20303.599609,20185.099609,20282.300781,20282.300781,238316600',
                 '2022-11-24,20309.199219,20386.699219,20309.199219,20344.099609,20344.099609,88111700',
                 '2022-11-25,20348.900391,20446.300781,20342.199219,20383.800781,20383.800781,157063000']
    test_passed = 0
    test_failed = 0
    
    if date_range(test_list, ['2022-11-20', '2022-11-22']) == test_list[:2]:
        test_passed += 1
    else:
        test_failed += 1

    if date_range(test_list, ['2022-11-20', '2022-11-24']) == test_list[:3]:
        test_passed += 1
    else:
        test_failed += 1

    print('Passed tests:', test_passed, '; Failed tests:', test_failed)

if __name__ == "__main__":
    main()
