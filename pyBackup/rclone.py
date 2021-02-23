import subprocess
import pathlib as Path



def make_rclone_cmd(transfer, config_dict):
    cmd = [
        config_dict['exe'], transfer['type'], '--timeout', config_dict['timeout'],
        '--retries', config_dict['retries'], '--transfers', config_dict['transfers']
        ] + config_dict['flags'] + [transfer['local_path'], transfer['targets_hostname']]
    cmd =[str(item) for item in cmd]
    return cmd
    
def run_transfer(transfer, config_dict):
    cmd = make_rclone_cmd(transfer, config_dict)
    print(' '.join(cmd))
    return subprocess.run(cmd)


