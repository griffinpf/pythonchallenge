##############################################################
# Challenge 2: http://www.pythonchallenge.com/pc/def/ocr.html#
##############################################################
import os

cwd = os.path.dirname(__file__)
#Mess of characters found in a comment at the end of the page source:
txt = cwd + '/resources/Challenge 2.txt'
with open(txt,'r') as file:
    comment = file.read().replace('\n','')

d = dict()

for i in comment:
    if i not in d:
        d[i] = 1
    else:
        d[i] +=1

result = ''

for key,val in d.items():
    if val == 1:
        result += key

print(result)
