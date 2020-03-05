import os
import imageio
import numpy as np
import argparse
import shutil


parser = argparse.ArgumentParser()
parser.add_argument('--currentsplit', type=str, default='../../training/train_groups')
parser.add_argument('--sequences', type=str, default='../../training/images_nogt')
parser.add_argument('--savefolder', type=str, default='./datasets/ultrasound')

opt = parser.parse_args()


currentsplit = opt.currentsplit
sequences = opt.sequences
savefolder = opt.savefolder

current_folders = os.listdir(currentsplit)
sequences_folder = ['Good', 'Poor']

for mode_folders in sequences_folder:
    if mode_folders == 'Good':
        domain = 'trainA'
    elif (mode_folders == 'Poor'): # (mode_folders == 'Medium') or (mode_folders == 'Poor'):
        domain = 'trainB'
    current_ = os.path.join(currentsplit, mode_folders, 'images')
    sequences_ = os.path.join(sequences, mode_folders)
    if not os.path.isdir(os.path.join(savefolder, domain)):
        os.makedirs(os.path.join(savefolder, domain))
    patients = os.listdir(current_)
    all_patients = os.listdir(sequences_)
    for patient in patients:
        # import pdb; pdb.set_trace()
        id_patient = '_'.join(patient.replace('.png', '').split('_')[0:2])
        mode_all_patients = [pat for pat in all_patients if '_'.join(pat.split('_')[0:2]) == id_patient]
        [shutil.copy(os.path.join(sequences_, pat), os.path.join(savefolder, domain, pat)) for pat in mode_all_patients]
