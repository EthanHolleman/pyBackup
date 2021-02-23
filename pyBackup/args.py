import argparse
from pathlib import Path

here = Path(__file__).parent.absolute()

def get_args():
    parser = argparse.ArgumentParser('Python backup program using Rclone.')
    parser.add_argument('backup', help='Path to directory with backup args.yaml and transfers.csv files. Log files will be written here.')
    parser.add_argument('-t', '--transfer_filename', default='transfers.csv', help='Name of transfer config file. Default is transfers.csv')
    parser.add_argument('-a', '--args_filename', default='args.yaml', help='Name of args config file. Default is args.yaml.')
    return parser.parse_args()
