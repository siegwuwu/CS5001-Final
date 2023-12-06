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
The first line is the header separated by commas. The 'Date' column and at least one price category in the columns beside it are required. The data point in each line should start with the date in the form of YYYY-MM-DD. 

The program will prompt the user to enter the start and end date of the analysis, the price category to run the analysis on, and the number of days of the SMA.

```
Please enter the start date of analysis in the format of YYYY-MM-DD:2022-12-01
Please enter the end date of analysis in the format of YYYY-MM-DD:2023-03-01
Please enter the type of price to perform the analysis:close
Please enter the number of days for the moving average:4
```
Upon entering all the information, the program will generate the strategy for each day based on the input. Typically, 'Close' is used for SMA analysis.
```
Date,Close,Strategy
2022-12-01,20525.500000,hold
2022-12-02,20485.699219,hold
2022-12-05,20242.300781,hold
2022-12-06,19990.199219,hold
2022-12-07,19973.199219,hold
2022-12-08,19969.199219,hold
2022-12-09,19947.099609,hold
2022-12-12,20019.699219,buy
2022-12-13,20023.500000,hold
2022-12-14,19891.699219,sell
2022-12-15,19600.599609,hold
2022-12-16,19443.300781,hold
2022-12-19,19200.800781,hold
2022-12-20,19306.900391,hold
2022-12-21,19571.099609,buy
2022-12-22,19349.699219,sell
2022-12-23,19506.699219,buy
2022-12-28,19284.099609,sell
2022-12-29,19485.900391,buy
2022-12-30,19384.900391,sell
2023-01-03,19443.800781,buy
2023-01-04,19588.800781,hold
2023-01-05,19506.800781,hold
2023-01-06,19814.500000,hold
2023-01-09,19857.099609,hold
2023-01-10,19898.900391,hold
2023-01-11,20025.099609,hold
2023-01-12,20211.199219,hold
2023-01-13,20360.099609,hold
2023-01-16,20390.300781,hold
2023-01-17,20457.500000,hold
2023-01-18,20376.199219,hold
2023-01-19,20341.400391,sell
2023-01-20,20503.199219,buy
2023-01-23,20631.599609,hold
2023-01-24,20629.599609,hold
2023-01-25,20599.599609,hold
2023-01-26,20700.500000,hold
2023-01-27,20714.500000,hold
2023-01-30,20572.099609,sell
2023-01-31,20767.400391,buy
2023-02-01,20751.099609,hold
2023-02-02,20740.400391,hold
2023-02-03,20758.300781,hold
2023-02-06,20628.900391,sell
2023-02-07,20725.000000,buy
2023-02-08,20679.500000,sell
2023-02-09,20597.800781,hold
2023-02-10,20612.099609,hold
2023-02-13,20702.199219,buy
2023-02-14,20704.800781,hold
2023-02-15,20720.400391,hold
2023-02-16,20606.400391,sell
2023-02-17,20515.199219,hold
2023-02-21,20252.599609,hold
2023-02-22,20193.300781,hold
2023-02-23,20188.199219,hold
2023-02-24,20219.199219,hold
2023-02-27,20260.099609,buy
2023-02-28,20221.199219,hold
2023-03-01,20259.800781,hold
What would you like to do? (Enter help for help):
```


## Installation Instructions
If we wanted to run this project locally, what would we need to do?  If we need to get API key's include that information, and also command line startup commands to execute the project. If you have a lot of dependencies, you can also include a requirements.txt file, but make sure to include that we need to run `pip install -r requirements.txt` or something similar.

## Code Review
Go over key aspects of code in this section. Both link to the file, include snippets in this report (make sure to use the [coding blocks](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)).  Grading wise, we are looking for that you understand your code and what you did. 

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
