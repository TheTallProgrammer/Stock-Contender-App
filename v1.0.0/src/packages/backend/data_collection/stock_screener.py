import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import re
from packages.backend.progress_tracker.global_instance import progress_tracker
from packages.backend.gpt_driver import gpt_driver, gpt_stock_analysis
from yahooquery import Screener

def retrieve_stocks():
    s = Screener()
    found_stocks = s.get_screeners(['undervalued_large_caps', 'undervalued_growth_stocks', 'day_gainers'], 15)    
    progress_tracker.register_task()
    
    return [
        {
            's': stock.get('symbol', None),
            'ef': stock.get('epsForward'),
            '52wh': stock.get('fiftyTwoWeekHigh'),
            '52wl': stock.get('fiftyTwoWeekLow'),
            'rmp': stock.get('regularMarketPrice', None),
            'mc': stock.get('marketCap', None), 
            'rmcp': stock.get('regularMarketChangePercent', None)
        } 
        for category in ['undervalued_large_caps', 'undervalued_growth_stocks'] 
        for stock in found_stocks[category]['quotes'] 
        if stock.get('regularMarketPrice', 0) >= 10
    ]


def re_format_data(data):
    progress_tracker.register_task()
    
    return [
        f"Stock: {item['s']}, epsForward: {item['ef']}, 52wk high: {item['52wh']}, 52wk low {item['52wl']}, Price: {item['rmp']}, Market Cap: {item['mc']}, Market Change % : {item['rmcp']}"
        for item in data
    ]


def structure_for_gpt():
    gpt_question = "You are an AI stock broker. pick out the best 5 stocks that seem best based on the given statistics and logic that you gathered from the data. Respond with only the best 5 tickers and their letters and nothing else. I repeat, only respond with the tickers, no bullet points or numbers/"
    input_data = "{0}{1}".format(gpt_question, " ".join(re_format_data(retrieve_stocks())))
    progress_tracker.register_task()
    
    return input_data


def get_gpt_response():
    return gpt_stock_analysis.gpt_response(structure_for_gpt())