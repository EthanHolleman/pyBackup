import os
from pathlib import Path
from pyBackup.utils import md5sum_file
from datetime import datetime

def process_stat_time(stat_time):
    return datetime.fromtimestamp(stat_time)

def file_report(filepath):
    md5 = md5sum_file(filepath)
    stat = Path(filepath).stat()
    mod_time = process_stat_time(stat.st_mtime)
    create_time = process_stat_time(stat.st_ctime)
    return {
        'md5': md5,
        'path': filepath,
        'mod_time': mod_time,
        'create_time': create_time,
        'size': stat.st_size
    }

def walking_report(start):
    for root, dirs, files in os.walk(start):
        for name in files:
            if os.path.exists(name):
                yield file_report(name)
                # need to get the full name from the start reference
                # or idealy the full path on the system


def identify_duplicated_files(file_reports):
    hash_count = {report['md5']: 0 for report in file_reports}
    for report in file_reports:
        hash_count[report['md5']] += 1
    # return tuples of reports that are duplicated 
