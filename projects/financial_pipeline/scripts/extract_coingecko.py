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


