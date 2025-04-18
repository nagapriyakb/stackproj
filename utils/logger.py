import logging
import os
from datetime import datetime

def get_logger(logger_name):
    # Get the project root directory dynamically
    # project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    project_root=r"C:\Users\DELL\PycharmProjects\PythonProject\shopstack"
    print(project_root)
    # Define the logs directory inside Reports
    log_dir = os.path.join(project_root, "Reports", "logs")
    os.makedirs(log_dir, exist_ok=True)
    print(log_dir)
    # Timestamp for unique log file
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # log_dir = "Reports/logs"
    # os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, f"{logger_name}_{timestamp}.log")

    # Set up logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    file_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)

    return logger
