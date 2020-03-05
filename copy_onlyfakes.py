import os
import imageio
import numpy as np
import argparse
import shutil


parser = argparse.ArgumentParser()
parser.add_argument('--dataroot', type=str, default='./results')
parser.add_argument('--savefolder', type=str, default='./results/exps')
# parser.add_argument('--exps_name', type=str)
parser.add_argument('--epoch', type=int, default=100)
# parser.add_argument('--phase', type=str, default='train', help='train, val, test, etc')
# parser.add_argument('--tumor', type=str, default='WT_imgs', help='train, val, test, etc')

opt = parser.parse_args()

epoch = opt.epoch
which_one = 'fake'
DATA_ROOT_1 = './results/ultrasound_unet/val_all_{}/images/'.format(epoch)
# DATA_ROOT_2 = './results/noncyc_LapLoss/val_all_{}/images/'.format(epoch)
# DATA_ROOT_3 = './results/morelevels_LapLoss/val_all_{}/images/'.format(epoch)
# DATA_ROOT_4 = './results/real_PM/train_groups_{}/images/'.format(epoch)

SAVE_ROOT = './results/exp/train_groups_{}/'.format(epoch)

if not os.path.exists(SAVE_ROOT):
	os.makedirs(SAVE_ROOT)

files_1 = os.listdir(DATA_ROOT_1)
# files_2 = os.listdir(DATA_ROOT_2)
# files_3 = os.listdir(DATA_ROOT_3)
# files_4 = os.listdir(DATA_ROOT_4)

def num_from_fname(x):
    return int(x.replace('.png', '').split('_')[-3])
# import pdb; pdb.set_trace()

save_folder_1 = DATA_ROOT_1.replace('images', 'fakes')
# save_folder_2 = DATA_ROOT_2.replace('images', 'fakes')
# save_folder_3 = DATA_ROOT_3.replace('images', 'fakes')
# save_folder_4 = DATA_ROOT_4.replace('images', 'fakes')

if not os.path.exists(save_folder_1):
    os.makedirs(save_folder_1)
# if not os.path.exists(save_folder_2):
#     os.makedirs(save_folder_2)
# if not os.path.exists(save_folder_3):
#     os.makedirs(save_folder_3)
# if not os.path.exists(save_folder_4):
    # os.makedirs(save_folder_4)

for file in files_1:
    check = file.split('_')
    if len(check) == 4 and (which_one in file):
        if which_one in file:
            # if check[-1][0] == 'B':
            original_path = os.path.join(DATA_ROOT_1, file)
            save_path = os.path.join(save_folder_1, file)
            shutil.copy(original_path, save_path)
            # fake_1.append(file)      

# for file in files_2:
#     check = file.split('_')
#     if len(check) == 4 and (which_one in file):
#         if which_one in file:
#             # if check[-1][0] == 'B':
#             original_path = os.path.join(DATA_ROOT_2, file)
#             save_path = os.path.join(save_folder_2, file)
#             shutil.copy(original_path, save_path)
#             # fake_2.append(file)

# for file in files_3:
#     check = file.split('_')
#     if len(check) == 4 and (which_one in file):
#         if which_one in file:
#             # if check[-1][0] == 'B':
#             original_path = os.path.join(DATA_ROOT_3, file)
#             save_path = os.path.join(save_folder_3, file)
#             shutil.copy(original_path, save_path)
#             # fake_3.append(file)


# for file in files_4:
    # check = file.split('_')
    # if len(check) == 5 and (which_one in file):
    #     if which_one in file:
    #         if check[-1][0] == 'B':
    #             original_path = os.path.join(DATA_ROOT_4, file)
    #             save_path = os.path.join(save_folder_4, file.replace('_B', '_A'))
    #             shutil.copy(original_path, save_path)
    #             # fake_3.append(file)
