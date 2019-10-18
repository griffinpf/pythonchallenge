###################################################################
#Challenge 4: http://www.pythonchallenge.com/pc/def/linkedlist.php#
###################################################################

from urllib import request

nothing = '12345'
response = 'and the next nothing'
count = 0
while 'and the next nothing' in response or response == 'Yes. Divide by two and keep going.':
    count +=1
    if count > 400:
        print('Too high')
        break
    a = request.urlopen(url='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+nothing)
    response = a.read().decode('utf-8')
    response = response.replace('/','')
    if response.find('and the next nothing is ') == 0:
        nothing = response[24:]
    elif response == 'Yes. Divide by two and keep going.':
        nothing = str((int(nothing)/2))
        nothing = nothing[:nothing.find('.')]
    else:
        nothing = response[response.find('and the next nothing is ')+ 24:]
print(response)
