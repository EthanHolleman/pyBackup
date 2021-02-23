import os
import socket
from pathlib import Path


import pandas as pd

from pyBackup.rclone import run_transfer

def execute_transfers(processed_transfers_df, config_dict):
    for index, transfer in processed_transfers_df.iterrows():
        run_transfer(transfer, config_dict)

def process_targets(targets_csv):
    transfers_df = pd.read_csv(targets_csv)
    transfers_df = discard_non_existant_paths(transfers_df)
    transfers_df = add_hostname_targetpath(transfers_df)
    transfers_df = sort_transfers_df(transfers_df)
    return transfers_df

def discard_non_existant_paths(transfers_df):
    non_local_targets = [i for i, p in enumerate(transfers_df['local_path']) if not Path(p).exists()]
    return transfers_df.drop(non_local_targets)

def add_hostname_targetpath(transfers_df):
    local_machine = socket.gethostname()
    home = str(Path.home())

    targets = transfers_df['target']
    remotes = []
    for i, transfers in transfers_df.iterrows():
        homeless_local = transfers['local_path'].replace(home, '')
        remote = Path(transfers['target']).joinpath(local_machine)
        remote = str(remote) + homeless_local
        remotes.append(remote)

    transfers_df['targets_hostname'] = remotes
    return transfers_df

def sort_transfers_df(transfers_df):
    return transfers_df.sort_values(by=['priority'])
    

