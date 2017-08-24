#!/usr/bin/env python

import sys, os
import subprocess
import shlex

if len(sys.argv) != 2:
    print "This script requires one command line argument: the name of the dataset folder in NetDissect/dataset"
else:
    dataset_name = sys.argv[1]
    working_dir = os.getcwd()
    os.chdir('csv_files')

    subprocess.call(shlex.split('cp label.csv ' + working_dir + '/' + dataset_name + '/ '))
    subprocess.call(shlex.split('cp category.csv ' + working_dir + '/' + dataset_name + '/ '))
    subprocess.call(shlex.split('cp c_[category].csv ' + working_dir + '/' + dataset_name + '/ '))
