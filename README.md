# pyBackup

Python and `rclone` based file backup program.

## Usage

pyBackup is designed to make using the already great `rclone`
program even easier. Start by setting up destinations to
backup your files to using the `rclone config` script. You
might want to test that you can actually transfer files to and
from these locations before going further.

Once `rclone` knows how to transfer your files around you can
start working on the `pyBackup` specific files that tells the
program how to run. These are collectively referred to as
`config` files and include:

### Transfers file

This is a `csv` formatted file that tells `pyBackup` which files to backup, where to back them up to and how to do it. These
attrbutes are specified under the headers of each column and are discussed in more detail below. It is 
critical these are present in your `transfers` csv
file or `pyBackup` *will fail*. 

- `local_path`: This is the path to directory on the
  machine that `pyBackup` is being run on. You can have local paths for multiple machines. `pyBackup`
  will figure out which ones actually exist on the
  current machine at runtime.

- `type`: This is an `rclone` keyword and specifies
    the type of transfer that should be completed. Common options are `sync` or `copy`. 

- `target`: This is the remote path the `local_path` should be copied to and should be given as it would be passed to the `rclone` command with a few caveats. `pyBackup` will add the name of the local machine to this path first, and then append the rest of the local path - the path to user's local home directory.

So if you passed `mydrive-gdrive:backups` here while running on a machine called `myPC` and the local path
to be copied is `/home/user/Documents`. The path
the files will actually be written to on the remote
computer will be `mydrive-gdrive:backups/myPC/Documents`. The thinking for this is to make it clear
where the backed-up files are coming from. 

- `priority`: Integer that indicates the order of the backup. Lower numbers are higher priority and a number must be specified for each transfer (row of your transfer csv file).

An example is available [here](example_backup/transfers.csv).

### Args 

This is a `yaml` formatted file that mainly specifies
arguments to be passed to `rclone`.

An example is available [here](example_backup/args.yaml).


Both of these files should be placed in a empty
directory which will be specified on the command line with the `backup` argument. It is recommended to follow the file naming
schema used in the [example_backup](example_backup/)
folder. If you decide to use different names for the
`transfers` and `args` files those changes can be specified when running `pyBackup` on the command line. 

## At the command line

```
usage: Python backup program using Rclone. [-h] [-t TRANSFER_FILENAME] [-a ARGS_FILENAME] backup

positional arguments:
  backup                Path to directory with backup args.yaml and transfers.csv files. Log files
                        will be written here.

optional arguments:
  -h, --help            show this help message and exit
  -t TRANSFER_FILENAME, --transfer_filename TRANSFER_FILENAME
                        Name of transfer config file. Default is transfers.csv
  -a ARGS_FILENAME, --args_filename ARGS_FILENAME
                        Name of args config file. Default is args.yaml.
```








