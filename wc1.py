import string

flText = open("diamond.txt",'r')

strText = flText.read()

iNC = len(strText)

iNL = len(strText.splitlines())

strWords = string.split(strText)

iWC = len(strWords)

print iNL, iWC, iNC

