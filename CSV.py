# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 13:31:37 2014

@author: abhijith
"""

import numpy as nmp
import operator
import csv 

data = [];

#populate the data into a list, data
with open('csvdata.txt','rb') as csvfile:
    csvRdr = csv.reader(csvfile)
    next(csvRdr, None)
    for row in csvRdr:
        data.append(row)
        
#Initialize empty dict
dictJob={}
        
#Form a dict of dict
for City, Job, Salary in data:
    dictJob.setdefault(Job, {})[City] = int(Salary)
    

dictLawyers = dictJob['Lawyers']
#print dictLawyers['Delhi']

SortedList_Salary=sorted(dictLawyers.items(), key=operator.itemgetter(1),reverse=True)
#SortedList_Salary=sorted(dictLawyers.items(),key=lambda x: x[1])
for l in SortedList_Salary: print l


#my_data = nmp.recfromcsv('csvdata.txt', delimiter=',',skip_header=1)
#my_data1 = nmp.genfromtxt('csvdata.txt', dtype=[('City','S20'),('Job','S20'),('Salary','f8')], delimiter=",",skip_header=1)
#
#print my_data1
