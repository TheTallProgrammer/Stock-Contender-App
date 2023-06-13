from yahooquery import Ticker
import yahoo_fin.stock_info as si
from packages.backend.progress_tracker.global_instance import progress_tracker

def get_best_tickers_info(best_tickers, tokens_per_ticker, important_keys, attribute):
    # Assume each ticker's data might have 800 tokens
    max_tokens = 4000
    max_tickers = max_tokens // tokens_per_ticker

    # Store the reduced financial data of all tickers
    all_tickers_attribute_data = []

    for i in range(0, len(best_tickers), max_tickers):
        batch_tickers = best_tickers[i:i+max_tickers]
        ticker_details = Ticker(batch_tickers)
        
        # Extract and process the financial data
        for ticker in batch_tickers:
            # Get financial data
            attribute_data = getattr(ticker_details, attribute)[ticker]
            
            # Check if important_keys is empty
            if important_keys:
                # Only keep important keys if important_keys is not empty
                reduced_financial_data = {key: attribute_data[key] for key in important_keys if key in attribute_data}
                all_tickers_attribute_data.append({ticker: reduced_financial_data})
            else:
                # Keep all financial data if important_keys is empty
                all_tickers_attribute_data.append({ticker: attribute_data})
    progress_tracker.register_task()    
       
    return all_tickers_attribute_data



def get_non_key_info(best_tickers, tokens_per_ticker, attribute):
    # Assume each ticker's data might have 800 tokens
    max_tokens = 4000
    max_tickers = max_tokens // tokens_per_ticker
    # Store the reduced financial data of all tickers
    all_tickers_attribute_data = []
    # Extract and process the financial data
    for ticker in best_tickers:
        # Get financial data
        ticker_details = Ticker(ticker)
        attribute_data = getattr(ticker_details, attribute)
        all_tickers_attribute_data.append({ticker: attribute_data})
    progress_tracker.register_task()    
    
    return all_tickers_attribute_data


