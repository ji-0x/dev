#!/usr/bin/env python3

import os
import json
import requests
from datetime import datetime
from financial_pipeline.utils.logging_utils import setup_logger



# -----------------------------
# Paths
# ----------------------------

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
RAW_DATA_DIR = os.path.join(BASE_DIR, 'raw')
LOG_DIR = os.path.join(BASE_DIR, 'logs')

os.makedirs(RAW_DATA_DIR,exist_ok=True)
os.makedirs(LOG_DIR,exist_ok=True)


# -----------------------------
# Logging
# -----------------------------

logger = setup_logger(__name__, LOG_DIR, 'extract_coingecko')
logger.info('Logger initialised for extract_coingecko.py')


# -----------------------------
# Fetch coingecko market data
# -----------------------------

def fetch_coingecko_data(coin_ids, vs_currency='usd'):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": vs_currency,
        "ids": ','.join(coin_ids),
        "order": "market_cap_desc",
        "per_page": len(coin_ids),
        "page": 1,
        "sparkline": "false",
        "price_change_percentage": "1h,24h,7d"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logger.error(f"Failed to fetch coingecko data: {e}")
        return None


# -----------------------------
# Save coingecko market data to data/raw/
# -----------------------------

def save_coingecko_data(data: dict) -> bool:
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"coingecko_market_{timestamp}.json"
    filepath = os.path.join(RAW_DATA_DIR, filename)

    try:
        wrapped = {
            "metadata": {
                "source": "coingecko",
                "extracted_at": timestamp,
                "record_count": len(data),
            },
        "data": data
        }

        with open(filepath, 'w') as f:
            json.dump(wrapped, f, indent=4) 
        logger.info(f"Saved raw coingecko data to {filepath}")
        return True
    except Exception as e:
        logger.error(f"Failed to save raw coingecko data: {e}")
        return False


def main():
    # Define coins list
    coins = [
        'bitcoin', 'ethereum', 'solana', 'ripple', 'cardano',
        'dogecoin','stellar','hedera-hashgraph','algorand','vechain',
        'bnb'
    ]

    try:


    except Exception as e:
    

if __name__ == '__main__':
    main()
