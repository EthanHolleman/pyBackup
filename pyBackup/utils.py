import os
import hashlib

def md5sum_file(filepath):
    return hashlib.md5(open(str(filepath),'rb').read()).hexdigest()
