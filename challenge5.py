##############################################################
#Challenge 5: http://www.pythonchallenge.com/pc/def/peak.html#
##############################################################

import pickle
from urllib.request import urlopen

#location of pickle file (hurr-hurr Peak Hell) in the page source
pickleRick = pickle.load(urlopen('http://www.pythonchallenge.com/pc/def/banner.p'))

iTurnedMyselfIntoAPickleMorty = ''
for i in range(len(pickleRick)):
    print(iTurnedMyselfIntoAPickleMorty)
    iTurnedMyselfIntoAPickleMorty = ''
    for j in range(len(pickleRick[i])):
        for k in range(pickleRick[i][j][1]):
            iTurnedMyselfIntoAPickleMorty = iTurnedMyselfIntoAPickleMorty + pickleRick[i][j][0]
