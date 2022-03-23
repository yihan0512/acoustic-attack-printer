"""
train and test split of a dataset
dataset dir in the structure of - dataset_dir
    - class 1
    - class 2
    ...
splitted dataset in the structure of
- dataset_dir
    - train
        - class 1
        - class 2
        ...
    - test
        - class 1
        -class 2
        ...
"""
import os
import sys
import shutil
from tqdm import tqdm
from random import shuffle

if __name__ == '__main__':
    # args
    dataset_dir = sys.argv[1]
    splitted_dir = dataset_dir.strip('/') + '_split/'
    percent = float(sys.argv[2])

    # get info about source dataset
    classes = os.listdir(dataset_dir)

    # create splitted dataset structure and put data in it
    for cls in tqdm(classes):
        sample_names = os.listdir(os.path.join(dataset_dir, cls))
        shuffle(sample_names)
        n_train_samples = round(len(sample_names) * percent)

        # train
        os.makedirs(os.path.join(splitted_dir, 'train', cls), exist_ok=True)
        for name in sample_names[:n_train_samples]:
            shutil.copy2(os.path.join(dataset_dir, cls, name),
                         os.path.join(splitted_dir, 'train', cls))
        # test
        os.makedirs(os.path.join(splitted_dir, 'val', cls), exist_ok=True)
        for name in sample_names[n_train_samples:]:
            shutil.copy2(os.path.join(dataset_dir, cls, name),
                         os.path.join(splitted_dir, 'val', cls))
