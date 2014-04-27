from __future__ import with_statement
import csv
import operator
from collections import defaultdict

data = [];

with open('salaries.csv','rb') as csvfile:
    csvRdr = csv.reader(csvfile)
    for row in csvRdr:
        data.append(row)

dictJob=defaultdict(list)

for City, Job, Salary in data:
    dictJob[Job].append(eval(Salary))

del dictJob['Job']

for k,v in dictJob.items():
      print k,sorted(v)[len(v)//2]

