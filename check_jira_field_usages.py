import tqdm
from itertools import chain
from glob import glob
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory_path', required=True, help="Directory to check")
arguments = parser.parse_args()
python_files = (chain.from_iterable(glob(os.path.join(x[0], '*.py')) for x in os.walk(arguments.directory_path)))
keys_to_check = {'.fields.key_raw', }

found_usage = set()
for file_name in tqdm.tqdm(python_files):
    file_contents = open(file_name).read()
    for key in keys_to_check:
        if key in file_contents:
            found_usage.add(file_name)

if found_usage:
    print("Found usage in following files")
    print("\n".join(found_usage))
else:
    print("All files are good!")
