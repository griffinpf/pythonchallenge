##################################################################
#Challenge 3: http://www.pythonchallenge.com/pc/def/equality.html#
##################################################################
import os

cwd = os.getcwd()
# Mess of characters found in the end of the page source:
txt = cwd + '/resources/Challenge 3.txt'
with open(txt,'r') as file:
    comment = file.read().replace('\n','-')

url = ''

for i in range(3,len(comment)-3):
    if i == 0 or not comment[i-4].isupper():
        if comment[i-3].isupper():
            if comment[i-2].isupper():
                if comment[i-1].isupper():
                    if comment[i].islower():
                        if comment[i+1].isupper():
                            if comment[i+2].isupper():
                                if comment[i+3].isupper():
                                    if i == len(comment) - 3 or not comment[i+4].isupper():
                                        url = url + comment[i]

print(url)
