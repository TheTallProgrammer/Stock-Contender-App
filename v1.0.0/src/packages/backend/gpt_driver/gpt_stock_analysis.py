from . import gpt_driver
import re
from packages.backend.data_collection.collect_stock_data import get_key_stats, get_recom_trend, get_technical_insights
from packages.backend.gpt_driver.gpt_driver import receive_input
from packages.backend.progress_tracker.global_instance import progress_tracker

def gpt_response(input):
    progress_tracker.register_task()
    
    return gpt_driver.receive_input(input)

def extract_tickers(selected_tickers):
    preprocessed_tickers = re.sub(r"P/E", "", selected_tickers)
    pattern = r"\b[A-Z]{1,5}\b"
    progress_tracker.register_task()
    
    return re.findall(pattern, preprocessed_tickers)

def get_top_stocks(best_tickers_info):
    input_data = f"You're an AI stock broker, based off this given information, \
    list the stocks in best to investing order with bullet points only including \
    the tickers. Only include the top 3 stocks out of the 5, remove the worst 2{best_tickers_info}"
    progress_tracker.register_task()
    
    return extract_tickers(gpt_response(input_data))

def generate_stock_review(best_tickers):
    key_stats = get_key_stats(best_tickers)
    recom_trend = get_recom_trend(best_tickers)
    stock_news = get_technical_insights(best_tickers)
    progress_tracker.register_task()
    
    return create_final_response(key_stats, recom_trend, stock_news)

def create_final_response(key_stats, recom_trend, stock_news):
    input_data = f"You're an AI stock broker. Based off of the stocks you have chosen to be the best out of the ones given to you. Use this new information as well as the previous information you gathered to come up with an order of the 3 chosen stocks, ranked from best to worst. I want you to provide an extensive review of each stock and why it's in the place you put it in in regards to best to worst. Provide expert analysis based off of this information.{key_stats, recom_trend, stock_news}"
    progress_tracker.register_task()
    
    return receive_input(input_data)