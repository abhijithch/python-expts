from __future__ import with_statement
import csv
import operator
from collections import defaultdict

data = [];
    
def dev(lst,avg):
    return [element-avg for element in lst]

def var(lst):
    return [element**2 for element in lst] 

with open('salaries.csv','rb') as csvfile:
    csvRdr = csv.reader(csvfile)
    for row in csvRdr:
        data.append(row)

dictJob=defaultdict(list)

for City, Job, Salary in data:
    dictJob[Job].append(eval(Salary))

del dictJob['Job']

for k,v in dictJob.items():
    avg = sum(v)/len(v)
    d = dev(v,avg)
    va = var(d)
    mean = sum(va)/len(va)
    sd = mean**0.5
    print k,int(sd)
