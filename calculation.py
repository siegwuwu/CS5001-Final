""" 
Final Project: Stock analysis app
===========================
Course:   CS 5001
Student:  Chen Wu

This file contains the function that calculate the moving average and determine
the trading strategy
"""

def calculate(data_with_title: list):
    '''
    Reads in a list of price data and a int for range of moving average, return
    a list with the moving average(MA) corresponding to each data in the list

    Args:
        data (list): list consists of items in the format of 'date,price'
        moving_range (int): range of the moving average specified by the user
    Reuturns:
        MA: the list of moving average corresponding to the price on each date
        in the Arg: data (list)
    '''
    moving_range = int(input("Please enter the number of days for the moving average:"))
    while moving_range <= 0:
            moving_range = int(input("Please enter the number of days for calculating moving average:"))

    data = data_with_title[1:]        
    data_len = len(data)
    MA = []
    for i in range(data_len):
        moving_avg = 0
        if i >= moving_range:
            range_start = i - moving_range
            while range_start < i:
                moving_avg += float(data[range_start].split(',')[1])
                range_start += 1
            moving_avg /= moving_range
        elif i > 0:
            range_start = 0
            while range_start < i:
                moving_avg += float(data[range_start].split(',')[1])
                range_start += 1
            moving_avg /= i
        else:
            moving_avg = float(data[0].split(',')[1])
        MA.append(moving_avg)
    return MA

def compare_MA(price_data: list, MA_data: list):
    '''
    Reads in a list of price data and a list of the corresponding moving average,
    return a list that indicate the strategy for each date (buy, sell, or hold)

    Args:
        price_data (list): list consists of items in the format of 'date,price'
        MA_data (list): list consists of moving average for each data in price_data
    Reutrns:
        comparision (list): list consists of strategy corresponding to each item
        in price_data
    '''
    comparision = ['hold']
    price_data_number = []
    result = [price_data[0] + ",Strategy"]
    
    for i in range(1, len(price_data)):
        price_data_number.append(float(price_data[i].split(',')[1]))

    for i in range(1, len(price_data_number)):
        if (price_data_number[i] - MA_data[i]) * (price_data_number[i-1] - MA_data[i-1]) > 0:
            comparision.append('hold')
        elif (price_data_number[i] - MA_data[i]) * (price_data_number[i-1] - MA_data[i-1]) < 0:
            if price_data_number[i-1] - MA_data[i-1] > 0:
                comparision.append('sell')
            else:
                comparision.append('buy')
        else:
            if i == 1:
                comparision.append('hold')
            elif i > 1:
                if (price_data_number[i] - MA_data[i]) * (price_data_number[i-2] - MA_data[i-2]) > 0:
                    comparision.append(comparision[i-2])
                elif (price_data_number[i] - MA_data[i]) * (price_data_number[i-2] - MA_data[i-2]) < 0:
                    if price_data_number[i-2] - MA_data[i-2] > 0:
                        comparision.append('sell')
                    else:
                        comparision.append('buy')
    for i in range(1, len(price_data)):
        price_data[i] = price_data[i] + ',' + comparision[i - 1]
        result.append(price_data[i])
        
    return result
