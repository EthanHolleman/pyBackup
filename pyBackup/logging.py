import logging
from datetime import datetime
from pathlib import Path

def make_default_logger(name, logpath):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(levelname)s\t%(asctime)s\t%(name)s\t%(lineno)d\t%(message)s')
    file_handler = logging.FileHandler(str(logpath))
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

def assign_log_path(backup_dir):
    now = datetime.now()
    log_dir = Path(backup_dir).joinpath('logs')
    if not log_dir.is_dir():
        log_dir.mkdir()
    return log_dir.joinpath(f'pyBackup_{now}.log')

