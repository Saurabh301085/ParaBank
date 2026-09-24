# import logging
# import os
#
#
# def get_logger():
#     logger = logging.getLogger(__name__)
#     logger.setLevel(logging.INFO)
#
#     # Get Parabank project folder path
#     project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
#     # Create log file path
#     log_path = os.path.join(project_path, "logs", "banklog.log")
#
#     file_handler = logging.FileHandler(log_path)
#
#     formatter = logging.Formatter(
#         "%(asctime)s - %(levelname)s - %(message)s"
#     )
#
#     file_handler.setFormatter(formatter)
#
#     logger.addHandler(file_handler)
#
#     return logger

import logging
import os


def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_path = os.path.join(project_path, "logs", "banklog.log")
    filehandler = logging.FileHandler(log_path)
    file_formatter = logging.Formatter("%(asctime)s - %(levelname)s -%(message)s,")
    filehandler.setFormatter(file_formatter)
    logger.addHandler(filehandler)
    return logger
