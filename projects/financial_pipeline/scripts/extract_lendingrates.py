#!/usr/bin/env python3

import os
import json
import time
import requests
from datetime import datetime
from financial_pipeline.utils.logging_utils import setup_logger


# ---------------------------
# Setup paths 
# ---------------------------

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
RAW_DATA_DIR = os.path.join(BASE_DIR, 'data', 'raw')
LOG_DIR = os.path.join(BASE_DIR, 'logs')

# ---------------------------
# Setup logging
# ---------------------------

logger = setup_logger(__name__, LOG_DIR, 'extract_lendingrates')
logger.info("Logger initialised for extract_lendingrates.py")

# ---------------------------
# Fetch lending rates
# ---------------------------

def fetch_lending_rates(endpoint, endpoint_path):
    url = f"https://ratesapi.nz/api/v1/{endpoint_path}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.raise_for_status()

    except requests.RequestException as e:
        logger.error(f"Failed to fetch lending rates for {endpoint_path}: {e}")
    return None

# ---------------------------
# Save lending rates
# ---------------------------



# ---------------------------
# Main execution
# ---------------------------

