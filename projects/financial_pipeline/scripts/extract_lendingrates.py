#!/usr/bin/env python3

import os
import json
import requests
from datetime import datetime
from financial_pipeline.utils.logging_utils import setup_logger


# ---------------------------
# Setup paths 
# ---------------------------

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
RAW_DATA_DIR = os.path.join(BASE_DIR, 'data', 'raw')
LOG_DIR = os.path.join(BASE_DIR, 'logs')

os.makedirs(RAW_DATA_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

# ---------------------------
# Setup logging
# ---------------------------

logger = setup_logger(__name__, LOG_DIR, 'extract_lendingrates')
logger.info("Logger initialised for extract_lendingrates.py")

# ---------------------------
# Fetch lending rates
# ---------------------------

def fetch_lending_rates(endpoint_key, endpoint_path):
    url = f"https://ratesapi.nz/api/v1/{endpoint_path}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.RequestException as e:
        logger.error(f"Failed to fetch lending rates for {endpoint_path}: {e}")
    return None

# ---------------------------
# Save lending rates
# ---------------------------

def save_lending_rates(endpoint_key, data):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{endpoint_key}_rates_{timestamp}.json"
    filepath = os.path.join(RAW_DATA_DIR, filename)

    try:
        wrapped = {
            "metadata": {
                "source": "ratesapi.nz",
                "extracted_at": timestamp,
                "record_count": len(data)
            },
            "data": data
        }

        with open(filepath, 'w') as f:
            json.dump(wrapped, f, indent=4)
            logger.info(f"Saved raw lending rates data for {endpoint_key} to: {filepath}")
            return True

    except Exception as e:
        logger.error(f"Failed to write file for {endpoint_key}: {e}")
        return False


# ---------------------------
# Main execution
# ---------------------------


def main():

    ENDPOINTS = {
        "car_loan": "car-loan-rates",
        "credit_card": "credit-card-rates",
        "mortgage": "mortgage-rates",
        "personal_loan": "personal-loan-rates"
    }

    success_count = 0

    try:
        for key, path in ENDPOINTS.items():
            logger.info(f"Fetching rates for: {key}")
            data = fetch_lending_rates(key, path)
        
            if data:
                if save_lending_rates(key, data):
                    #logger.info(f"Lending rates ingestion completed. {len(data)} rates fetched.")
                    # Get count of product rates? len(data["data"]["data"][0]["products"][0]["rates"][0]["rate"])
                    logger.info(f"Lending rates ingestion for {key} completed.")
                    success_count += 1
            else:
                logger.warning(f"No data return for {key}")

        if success_count == 0:
            logger.warning("No data fetched from any endpoints.")
            return False

        logger.info(f"Lending rates extraction job completed successfully. {success_count}/{len(ENDPOINTS)} endpoints fetched.")
        return True

    except Exception as e:
        logger.error(f"Error during extraction job: {e}", exc_info=True)
        return False

if __name__ == '__main__':
    main()
