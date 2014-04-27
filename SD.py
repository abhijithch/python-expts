# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 21:51:00 2014

@author: abhijith
"""

import csv
from collections import defaultdict
import numpy as nmp

data = [];

with open('csvdata.txt','rb') as csvfile:
    csvRdr = csv.reader(csvfile)
    next(csvRdr, None)
    for row in csvRdr:
        data.append(row)
        
dictJob=defaultdict(list)

for City, Job, Salary in data:
    dictJob[Job].append(Salary)
    
for k in dictJob:
    print k,int(nmp.std(map(int,dictJob[k])))
