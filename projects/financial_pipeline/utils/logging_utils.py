#!/usr/bin/env python3

import os 
import logging
from datetime import datetime

def setup_logger(name: str, log_dir: str) -> logging.Logger:
    os.makedirs(log_dir, exist_ok=True)
    log_time = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_file_path = os.path.join(log_dir, f"{prefix}_{log_time}.log")

    logging.basicConfig(
        filename=log_file_path,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(name)
