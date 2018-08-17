# encoding=utf-8

import getpass
import os
import sys
import getopt
import shutil


def main(argv):
    source, target = get_source_target(argv)
    os.chdir(source)
    shutil.copy(os.path.join(source, 'night.css'), target)
    shutil.copy(os.path.join(source, 'night.user.css'), target)
    shutil.copy(os.path.join(source, 'base.user.css'), target)


def get_source_target(argv):
    source = target = None
    params = getopt.getopt(argv, 's:t:')

    for lst in params:
        if lst:
            for i in lst:
                if isinstance(i, tuple):
                    key, value = i
                    if key == '-s':
                        source = value
                    elif key == '-t':
                        target = value

    if not source:
        source = get_default_source()
    if not target:
        target = get_default_target()

    return source, target


def get_default_target():
    path_fmt = r'C:\Users\%s\AppData\Roaming\Typora\themes'
    return path_fmt % getpass.getuser()


def get_default_source():
    return os.getcwd()


if __name__ == "__main__":
    main(sys.argv[1:])
