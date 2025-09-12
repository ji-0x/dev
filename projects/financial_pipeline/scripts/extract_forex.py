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

def 
