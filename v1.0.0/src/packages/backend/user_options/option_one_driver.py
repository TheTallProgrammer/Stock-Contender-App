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

import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import os
import shutil
import pandas as pd
from packages.backend.data_collection.stock_screener import get_gpt_response
from packages.backend.gpt_driver.gpt_stock_analysis import (
    get_top_stocks, 
    extract_tickers, 
    generate_stock_review
)
from packages.backend.data_collection.collect_stock_data import get_collected_data

def handle_errors(function):
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as e:
            print(f"Error trying to {function.__name__}: {e}")
    return wrapper

@handle_errors
def user_option_one_driver():
    best_tickers = get_gpt_response()
    best_tickers_info = handle_best_tickers(best_tickers)
    best_tickers = get_top_stocks(best_tickers_info)
    return generate_stock_review(best_tickers)
        
@handle_errors
def handle_best_tickers(gpt_reply):
    best_tickers = extract_tickers(gpt_reply)
    return get_collected_data(best_tickers)

        

