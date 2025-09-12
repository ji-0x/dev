#!/usr/bin/env python3

import os
import json
import requests
import time 
from datetime import datetime
from financial_pipeline.utils.logging_utils import setup_logger
from projects.financial_pipeline.scripts.extract_coingecko import LOG_DIR, RAW_DATA_DIR




# -----------------------------
# Setup
# -----------------------------

CONFIG = {}

# -----------------------------
# paths
# -----------------------------

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
LOG_DIR = os.path.join(BASE_DIR, 'logs')
RAW_DATA_DIR = os.path.join(BASE_DIR, 'data', 'raw')


# -----------------------------
# Logging
# -----------------------------

logger. = setup_logger(__name__, LOG_DIR, 'extract_forex')
logger.info("Logger initialised for extract_forex.py")


# -----------------------------
# g
# -----------------------------
