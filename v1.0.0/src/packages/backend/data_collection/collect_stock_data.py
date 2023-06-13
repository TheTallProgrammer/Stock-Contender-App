# Copyright 2023 Logan Falkenberg
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
from yahooquery import Ticker

from packages.backend.data_collection.collect_stock_attributes import get_best_tickers_info, get_non_key_info
from packages.backend.progress_tracker.global_instance import progress_tracker

def get_key_stats(best_tickers):
    keys = ['forwardPE', 'profitMargins','sharesOutstanding', 'heldPercentInstitutions','bookValue', 'priceToBook', 'netIncomeToCommon', 'trailingEps', '52WeekChange']
    progress_tracker.register_task()
    
    return get_best_tickers_info(best_tickers, 800, keys, "key_stats")

def get_collected_data(best_tickers):
    keys = ['currentPrice', 'returnOnEquity','freeCashflow', 'debtToEquity', 'grossMargins', 'recommendationMean ']
    progress_tracker.register_task()
    
    return get_best_tickers_info(best_tickers, 800, keys, "financial_data")

def get_recom_trend(best_tickers):
    progress_tracker.register_task()
    
    return reformat_data(get_non_key_info(best_tickers, 300, "recommendation_trend"))

def reformat_data(array):
    formatted_data = []
    for stock_dict in array:
        for stock, df in stock_dict.items():
            df = df.reset_index().rename(columns={'index': 'Stock'})
            df['Stock'] = stock
            formatted_data.extend(df.to_dict('records'))
    progress_tracker.register_task()
    
    return formatted_data

def clean_data(data_str):
    data_str = json.dumps(data_str)
    data_str = data_str.replace('{', '').replace('}', '').replace('"', '').replace(',', ', ')
    progress_tracker.register_task()
    
    return data_str

def get_technical_insights(best_tickers, max_tokens=55):
    result = []
    for symbol in best_tickers:
        ticker = Ticker(symbol)
        data = ticker.technical_insights
        data_str = clean_data(data)
        if len(data_str.split()) > max_tokens:
            data_str = ' '.join(data_str.split()[:max_tokens])
        result.append(data_str)
    progress_tracker.register_task()
    
    return result
