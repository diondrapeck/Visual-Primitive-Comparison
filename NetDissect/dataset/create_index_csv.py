#!/usr/bin/env python

import sys, os

# create new index.csv file with column headers as first line
output_file = open("index.csv", 'w')
output_file.write("image,split,ih,iw,sh,sw,diagnosis,binaryclassification,side\n")

img_prefix = sys.argv[3]

# copy image name and attributes to index.csv in appropriate format
with open(sys.argv[1], 'r') as input_file:
    for line in input_file.readlines():
        words = line.split()
        image_name = os.path.join(img_prefix, words[0])
        binary_classification = words[1]

        if image_name.startswith('c'):
            diagnosis = "cancer"
        elif image_name.startswith('b'):
            diagnosis = "benign"
        else:
            diagnosis = "normal"

        if 'LEFT' in image_name:
            side = "left"
        else:
            side = "right"

        output_file.write(image_name + ",train,227,227,113,113," + diagnosis + "," + binary_classification + "," + side + "\n")

with open(sys.argv[2], 'r') as input_file:
    for line in input_file.readlines():
        words = line.split()
        image_name = os.path.join(img_prefix, words[0])
        binary_classification = words[1]

        if image_name.startswith('c'):
            diagnosis = "cancer"
        elif image_name.startswith('b'):
            diagnosis = "benign"
        else:
            diagnosis = "normal"

        if 'LEFT' in image_name:
            side = "left"
        else:
            side = "right"

        output_file.write(image_name + ",val,227,227,113,113," + diagnosis + "," + binary_classification + "," + side + "\n")

output_file.close()
