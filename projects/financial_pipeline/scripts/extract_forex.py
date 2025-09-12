#!/usr/bin/env python3

import os
import json
import requests
import time 
from datetime import datetime
from financial_pipeline.utils.logging_utils import setup_logger



# -----------------------------
# Setup
# -----------------------------

CONFIG = {
    "api_key": "",
    "fx_function": "FX_DAILY",
    "base_currency": "USD",
    "target_currencies": ["EUR", "GBP", "JPY", "AUD", "NZD", "CAD"],
    "api_url": "https://www.alphavantage.co/query",
    "rate_limit_delay": 12
}

# -----------------------------
# paths
# -----------------------------

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
LOG_DIR = os.path.join(BASE_DIR, 'logs')
RAW_DATA_DIR = os.path.join(BASE_DIR, 'data', 'raw')

# -----------------------------
# Logging
# -----------------------------
logger  = setup_logger(__name__, LOG_DIR, 'extract_forex')
logger.info("Logger initialised for extract_forex.py")

# -----------------------------
# Fetch forex rates from Aplha vantage
# -----------------------------

def fetch_forex_rates(from_currency, to_currency, config):
    params = {
        "function": config["fx_function"],
        "from_symbol": from_currency,
        "to_symbol": to_currency,
        "outputsize": "compact",
        "api_key": config["api_key"]
    }
    
    try:
        response = requests.get(config["api_url"], params=params,timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logger.error(f"Request error for {from_currency}/{to_currency}: {e}")
    return None



# -----------------------------
# Save forex data
# -----------------------------

def save foroex_rates():
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"forex_rates_{timestamp}.json"
    filepath = os.path.join(RAW_DATA_DIR, filename)

    wrapped = {
        "metadta": {
            "source": "Alpha Vantage - FX_DAILY",
            "extracted_at": timestamp,
            "record_count": len(data),
        },
        "data": data
    }

    try:
        with open(filepath, 'w') as f:
            json.dump(wrapped, f, indent=4)
        logger.info(f"Saved raw forex data to {filepath}")
        return True

    except Exception as e:
        logger.error(f"Failed to save raw forex data: {e}")
        return False 

def main():
    # 
if __name__ == '__main__':
    main()


