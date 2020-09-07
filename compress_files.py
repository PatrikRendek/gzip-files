#!/usr/bin/python3
"""
  Compress files in directory using gzip
    usage:
       ./compress_files.py <directory>
    example:
       ./compress_files.py /var/log/
"""

import os
import pathlib
import gzip
import sys


def gzip_files(files:list):
    """Gzip files in paths from list.

        Parameters:
        files (list) -- Paths of files
    """
    for file in files:
        try:
            with open(file, 'rb') as f_in, gzip.open(file + '.gz', 'wb') as f_out:
                f_out.writelines(f_in)
        except Exception as exception:
            print(exception)


def get_files(root_path: str):
    """Get paths of files in root directory and its subdirectories.

        Parameters:
        root_path (string) -- Path of root directory

        Returns:
        list: List of paths.
    """
    files_list = []
    for path, subdirs, files in os.walk(root_path):
        for name in files:
            pure_path = str(pathlib.PurePath(path, name))
            files_list += [pure_path]
    return files_list


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    path = (sys.argv[1])
    gzip_files(get_files(path))
