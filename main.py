
#GUI Lib.
#import tkinter


#main stock data API
import alpha_vantage
from alpha_vantage.timeseries import TimeSeries

#Plotting Lib.
import matplotlib.pyplot as plt

def getSingleStockData(stk_symbl):
    if stk_symbl == "":
        print ("no symbol")
        return -1
    else:
        print ("fetching %s" % stk_symbl)
        ts = TimeSeries(key='3QGQAO7J85VT4771', output_format='pandas')
        data, meta_data = ts.get_intraday(symbol=stk_symbl,interval='1min', outputsize='full')
        data['4. close'].plot()
        plt.title('Intraday Times Series for the ' +stk_symbl+ ' stock (1 min)')
        plt.show()
        #print(data)
        return data
"""
#Main Program
while (True):
    print ("Enter the Stock Symbol (Type quit to exit the program):")
    ss=input()
    getSingleStockData(ss)
    """
"""     stk_symbl = input()
    if stk_symbl == "quit": #exiting command
        break
    else:
        ts = TimeSeries(key='3QGQAO7J85VT4771', output_format='pandas')
        data, meta_data = ts.get_intraday(symbol=stk_symbl,interval='1min', outputsize='full')
        data['4. close'].plot()
        plt.title('Intraday Times Series for the ' +stk_symbl+ ' stock (1 min)')
        plt.show()

    print(data) 
"""

