# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 19:53:02 2019

@author: USER
"""

import os, shutil
from random import shuffle

Dir_list = os.listdir("train_data")

for plant_name in Dir_list:
    plant_dir = os.path.join("train_data",plant_name)  
    files = [x for x in os.listdir(plant_dir) if os.path.isfile(os.path.join(plant_dir,x))]
    shuffle(files)
    n = int(len(files)*.15) 
    
    destination = os.path.join("test_data",plant_name)
    for f in files[:n]:
        shutil.move(os.path.join(plant_dir,f), destination)
    
    
    
    
    
    