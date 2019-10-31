##################################################################
#Challenge 10: http://www.pythonchallenge.com/pc/return/bull.html#
##################################################################

#a = [1, 11, 21, 1211, 111221, 
#len(a[30]) = ?
# This is the look-and-say sequence
 
def lookandsay(n): 
	if (n == 1): 
		return '1'
	if (n == 2): 
		return '11'

	s = '11'
	for i in range(3, n+1): 
		s += '$'
		l = len(s) 

		count = 1 
		temp = ''

		for j in range(1 , l): 
			if (s[j] != s[j-1]): 
				temp += str(count) 
				temp += s[j-1] 
				count = 1
			else: 
				count += 1
		s = temp 
	return s

a = []

for i in range(1,32):
    a.append(lookandsay(i))

print(len(a[30]))
