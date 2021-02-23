# set up 
from pathlib import Path
import yaml

def read_args_dict(filepath):
    fp = Path(filepath)
    with open(str(fp)) as handle:
        try:
            return yaml.load(handle)
        except Exception as e:
            raise TypeError(
        f'{filepath} could not be read as a yaml file raised {e}.')


def check_for_config_file(backup_dir, filename):
    name = Path(filename).name
    inferred_path = Path(backup_dir).joinpath(name)
    if inferred_path.is_file():
        return inferred_path
    else:
        raise FileNotFoundError(f'''
    Based on the arguments provides, pyBackup looked for but did not find
    the config file {inferred_path}. Please make sure this path exists before
    rerunning.
    ''')

def infer_config_filepaths(backup_dir, transfer_filename='transfer.csv', 
                           args_filename='args.yaml'):
    bd = Path(backup_dir)
    transfers_path = check_for_config_file(backup_dir, transfer_filename)
    config_path = check_for_config_file(backup_dir, args_filename)
    return transfers_path, config_path

