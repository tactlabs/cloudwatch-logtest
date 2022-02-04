import os
from dotenv import load_dotenv

import logging

load_dotenv()

LOG_FILE_NAME = os.environ["LOG_FILE_NAME"]

logging.basicConfig(
    filename = LOG_FILE_NAME, 
    level = logging.DEBUG
)

