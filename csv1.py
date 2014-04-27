from __future__ import with_statement
import csv
import operator
from collections import defaultdict

data = [];

with open('salaries.csv','rb') as csvfile:
    csvRdr = csv.reader(csvfile)
    #next(csvRdr, None)
    for row in csvRdr:
        data.append(row)


#Initialize empty dict
dictJob={}

#Form a dict of dict
for City, Job, Salary in data:
    dictJob.setdefault(Job, {})[City] = eval(Salary)

dictLawyers = dictJob['Lawyers']

SortedList_Salary=sorted(dictLawyers.iteritems(), key=operator.itemgetter(1),reverse=True)

for l in SortedList_Salary: print l
