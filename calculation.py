""" 
Final Project: Stock analysis app
===========================
Course:   CS 5001
Student:  Chen Wu

This file contains the function that calculate the moving average and determine
the trading strategy
"""

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


def main() -> None:
    """
    Runs the stock analysis application.
    """

    test_passed = 0
    test_failed = 0
    
    if compare_MA(['Date,Close', '1,2', '2,3', '3,4'], ['MA', '1', '3', '4']) == ['Date,Close,MA,Strategy', '1,2,1.0,hold', '2,3,3.0,hold', '3,4,4.0,hold']:
        test_passed += 1
    else:
        test_failed += 1
    ## Test when day 1, 2, 3 all have difference in close and MA of 0, all days should have strategy of hold

    if compare_MA(['Date,Close', '1,2', '2,3', '3,4'], ['MA', '1', '4', '1']) == ['Date,Close,MA,Strategy', '1,2,1.0,hold', '2,3,4.0,sell', '3,4,1.0,buy']:
        test_passed += 1
    else:
        test_failed += 1
    ## This test should return sell for day 2 as the (price - MA) turns negative, and buy for day 3 as the (price - MA) turns positive
    
    print('Passed tests:', test_passed, '; Failed tests:', test_failed)


if __name__ == "__main__":
    main()
