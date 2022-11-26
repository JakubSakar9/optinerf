import numpy as np
import scipy.io

import os
from os import path
import shutil
import sys

dataset_path = os.path.join(os.getcwd(), sys.argv[1])
depth_dir = os.path.join(dataset_path, 'depth_stat')
err_dir = os.path.join(dataset_path, 'confidence')
print(os.listdir(depth_dir))
depth_files = [os.path.join(depth_dir, f) for f in os.listdir(depth_dir)]
err_files = [os.path.join(err_dir, f) for f in os.listdir(err_dir)]
depth_files = filter(lambda str: str[-3:] == 'mat', depth_files)
err_files = filter(lambda str: str[-3:] == 'mat', err_files)
for d, e in zip(depth_files, err_files):
    m_d = scipy.io.loadmat(d)
    m_e = scipy.io.loadmat(e)
    D = m_d['mean_c2X']
    E = m_e['confidence_mvs']
    d_path = d[:-3] + 'npy'
    e_path = e[:-3] + 'npy'
    os.remove(d)
    os.remove(e)
    np.save(d_path, D)
    np.save(e_path, E)

os.makedirs(os.path.join(dataset_path, 'sparse', '0'))
sparse_path = os.path.join(dataset_path, 'sparse', '0')
shutil.move(os.path.join(dataset_path, 'cameras.txt'), sparse_path)
shutil.move(os.path.join(dataset_path, 'images.txt'), sparse_path)
shutil.move(os.path.join(dataset_path, 'points3D.txt'), sparse_path)
shutil.move(depth_dir, os.path.join(dataset_path, 'depths'))
shutil.move(err_dir, os.path.join(dataset_path, 'err'))
