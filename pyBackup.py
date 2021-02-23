from pyBackup.transfers import process_targets, execute_transfers
from pyBackup.config import infer_config_filepaths, read_args_dict
from pyBackup.args import get_args
from pyBackup.logging import make_default_logger, assign_log_path

from pathlib import Path

def main():
    args = get_args()
    logpath = assign_log_path(args.backup)
    logger = make_default_logger(__name__, logpath)
    logger.info('Started backup')
    transfer_path, args_path = infer_config_filepaths(args.backup, args.transfer_filename, args.args_filename)
    logger.info(f'Transfer file: {transfer_path}')
    logger.info(f'Args file: {args_path}')
    args_dict = read_args_dict(args_path)
    transfers = process_targets(transfer_path)
    execute_transfers(transfers, args_dict)
    logger.info(f'Completed backup of {len(transfers)} transfers.')

if __name__ == '__main__':
    main()

    
