#!/usr/bin/env python3

import os
import json
import requests
from datetime import datetime
from financial_pipeline.utils.logging_utils import setup_logger
from scripts.extract_forex import BASE_DIR, LOG_DIR, RAW_DATA_DIR



# ---------------------------
# Setup paths 
# ---------------------------

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
RAW_DATA_DIR = os.path.join(BASE_DIR, 'data', 'raw')
LOG_DIR = os.path.join(BASE_DIR, 'logs')

# ---------------------------
# Setup logging
# ---------------------------



# ---------------------------
# Fetch lending rates
# ---------------------------



# ---------------------------
# Save lending rates
# ---------------------------



# ---------------------------
# Main execution
# ---------------------------

