#################################################################
#Challenge 6: http://www.pythonchallenge.com/pc/def/channel.html#
#################################################################

import os
import zipfile

# Zip file can be found by changing .html in the url to .zip

cwd = os.path.dirname(__file__)
zipdict = {}

with zipfile.ZipFile(cwd + '/resources/channel.zip', 'r') as f:
    for name in f.namelist():
        if name != 'readme.txt':
            zipdict[name.replace('.txt','')] = f.read(name).decode('utf-8')

# Per the readme, start with 90052
x = '90052'
while 'Next nothing is ' in zipdict[x]:
    x = zipdict[x][16:]

print(x+': '+zipdict[x])

# Since that outputs "Collect the comments", check the comments of the zip file
archive = zipfile.ZipFile(cwd + '/resources/channel.zip','r')
x = '90052'
comments = ''
while 'Next nothing is ' in zipdict[x]:
    comments += archive.getinfo(x+'.txt').comment.decode('utf-8')
    x = zipdict[x][16:]

print(comments)