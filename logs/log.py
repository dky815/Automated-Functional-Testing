import logging
import os.path
import time

from common.tools import get_project_path, sep


def get_log(logger_name):
    # create logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    # set log file name
    # get current time
    rq = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    # set log path
    all_log_path = get_project_path() + sep(["logs", "all_logs"], add_sep_before=True, add_sep_after=True)
    # if the log path does not exist, create it
    if not os.path.exists(all_log_path):
        os.makedirs(all_log_path)
    # set log file name
    all_log_name = all_log_path + rq + ".log"

    # create a handler to write all logs
    fh = logging.FileHandler(all_log_name)
    fh.setLevel(logging.INFO)

    # define the output format of handler
    all_log_formatter = logging.Formatter(
        "%(asctime)s - %(filename)s - %(module)s - %(funcName)s - %(lineno)d - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S")
    # add formatter to handler
    fh.setFormatter(all_log_formatter)

    # add handler to logger
    logger.addHandler(fh)
    return logger

log = get_log("autotest")