This directory contains the following data:

        image/patches/...
                jpeg images softlinked from mount_donuts/data/ddsm/patches/resized_images

        index.csv
                contains a list of all the images in the dataset, together with
                available labeled data, in the form: image,split,ih,iw,sh,sw,[binaryclassification]
                e.g. benign_01-B_3091_1.LEFT_CC.LJPEG.1-x109u.jpg,train,227,227,113,113,0
                
		The first column is always the original image filename relative to
                the images/ subdirectory; then image height and width and segmentation
                height and width dimensions are followed by six columns for label
                data in the six categories. Label data can be per-pixel or per-image
                (assumed to apply to every pixel in the image), and 0 or more labels
                can be specified per category. If there are no labels, the field is ''.
                If there are multiple labels, they are separated by semicolons,
                and it is assumed that dominant interpretations are listed first.
                Per-image labels are represented by a decimal number; and per-image
                labels are represented by a filename for an image which encodes
                the per-pixel labels in the (red + 256 * green) channels.

        category.csv
                name,first,last,count,frequency
                e.g. binaryclassification,,,2,76574

                In the generic case there may not be six categories; this directory
                may contain any set of categories of segmentations. This file
                lists all segmentation categories found in the data sources,
                along with statistics on now many class labels apply to
                each category, and in what range; as well as how many
                images mention a label of that category

        label.csv
                number,name,category,frequency,coverage,syns
                e.g. 1,cancer,diagnosis,27479,,

                This lists all label numbers and corresponding names, along
                with some statistics including the number of images for
                which the label appears in each category; the total number
                of images which have the label; and the pixel portions
                of images that have the label.

        c_[category].csv (e.g. c_material.csv)
                code,number,name,frequency,coverage
                e.g. 1,6,left,,

                Although labels are stored under a unified code, this file lists a 
                standard dense coding that can be used for a specific subcategory of 
		labels.

        create_index_csv.py
                python create_index_csv.py train_file.txt val_file.txt

                Script to generate "index.csv" from the lmdb-associated .txt
		files: one train and one val.
                
		Extracts information about the image file name and other
		designated labels
