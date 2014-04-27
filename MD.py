# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 21:11:14 2014

@author: abhijith
"""


import csv
from collections import defaultdict
import numpy as nmp

data = [];


    
def dev(lst,avg):
    return [element-avg for element in lst]

def squarelist(lst):
    return [element**2 for element in lst] 
    


with open('csvdata.txt','rb') as csvfile:
    csvRdr = csv.reader(csvfile)
    next(csvRdr, None)
    for row in csvRdr:
        data.append(row)
        
dictJob=defaultdict(list)

for City, Job, Salary in data:
    dictJob[Job].append(Salary)
    
#md = nmp.median(dictJob['Plumbers'])
    
#print nmp.median(int(dictJob['Plumbers'])

for k in dictJob:
    print k,int(nmp.median(map(int,dictJob[k])))
    

#temp = dictJob['Plumbers']

#tt=map(float, temp)

#print nmp.std(tt)