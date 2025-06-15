import logging
import os
from datetime import datetime

# Timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create a separate folder for each log
logs_folder = os.path.join(os.getcwd(), "logs", LOG_FILE.replace(".log", ""))
os.makedirs(logs_folder, exist_ok=True)

# Create log file inside that folder
LOG_FILE_PATH = os.path.join(logs_folder, LOG_FILE)

# Configure logging — this will now run even when imported
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
