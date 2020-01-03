# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 13:09:38 2020

@author: Akaash Preetham
"""

import pandas as pd
import os
import numpy as np 
#import pandas as pd 

# FUNCTIONALITIES

# Input resolution
name = input("Enter the name: ")
goal = input("Enter the goal: ")
unit = input("Enter the unit: ")
resolution = []
resolution.append(name)
resolution.append(goal)
resolution.append(unit)
print(resolution)
resolutions.append(resolution)

df = pd.DataFrame(resolutions, columns = ['Name', 'Goal', 'Unit'])
df.to_csv('Resolutions.xlsx')

# Display resolution 
pd.read_csv('Resolutions.xlsx')

# Update performance

# Reminder