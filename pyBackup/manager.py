import os
from pathlib import Path
from pyBackup.utils import md5sum_file
from datetime import datetime
import pandas as pd
import multiprocessing as mp


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


def walk_files(start):
    for root, dirs, files in os.walk(start):
        for name in files:
            if os.path.exists(name):
                yield os.path.join(root, name)


def identify_duplicated_files(file_reports):
    hash_count = {report['md5']: 0 for report in file_reports}
    for report in file_reports:
        hash_count[report['md5']] += 1
    # return tuples of reports that are duplicated


def write_report_file(file_reports, filepath):
    report_df = pd.DataFrame.from_dict(file_reports)
    report_df.to_csv(str(filepath))
    return filepath


def file_reports_from_step(queue, reports):
    while True:
        step = queue.get()
        if step is None:
            break
        root, dirs, files = step
        for each_file in files:
            full_path = os.path.join(root, each_file)
            if os.path.exists(full_path):
                reports.append(file_report(full_path))


def create_file_report(start_dir, ncore=4):
    # https://stackoverflow.com/questions/43078980/python-multiprocessing-with-generator
    # https://docs.python.org/3/library/multiprocessing.html
    filepaths = os.walk(start_dir)
    q = mp.Queue(maxsize=ncore)
    iolock = mp.Lock()
    with mp.Manager() as manager:
        reports = manager.list()
        pool = mp.Pool(ncore, initializer=file_reports_from_step, initargs=(q, reports))
        for each_step in filepaths:
            q.put(each_step)
        for _ in range(ncore):
            q.put(None)
        pool.close()
        pool.join()
        return list(reports)


def dummy_report(start_dir):
    reports = []
    filepaths = os.walk(start_dir)
    for root, dirs, files in filepaths:
        for each_file in files:
            full_path = os.path.join(root, each_file)
            if os.path.exists(full_path):
                reports.append(file_report(full_path))
    return reports
        

# import time
# start = time.time()
# p = dummy_report('/home/ethan/Documents/github/')
# end = time.time()
# print(len(p))
# print('Time:', end-start)

# mutliprocessed Time: 162.1233057975769