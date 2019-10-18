##############################################################
# Challenge 1: http://www.pythonchallenge.com/pc/def/map.html#
##############################################################

# all letters were shifted two positions right alphabetically
hint = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
alphabet = 'abcdefghijklmnopqrstuvwxyzabc'
arr = []
arr1 = []
arr2 = []
for i in hint:
    arr.append(i)
for i in alphabet:
    arr1.append(i)

for i in range(len(arr)):
    if arr[i] == ' ':
        arr2.insert(i,' ')
    elif arr[i] == '.':
        arr2.insert(i, '.')
    else:
        for j in range(26):
            if arr1[j] == arr[i]:
                arr2.append(arr1[j+2])

decoded = ''
for i in range(len(arr2)):
    decoded = decoded + arr2[i]
print(decoded)
