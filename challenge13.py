#############################################################################
#Challenge 13: http://www.pythonchallenge.com/pc/return/disproportional.html#
#############################################################################

# Clicking the phone gives an XML error, and an RPC fault
# so it's probably solved via RPC to that address

import xmlrpc.client

server = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')

# let's see what methods are available
for method in server.system.listMethods():
    print(method)
    print(server.system.methodHelp(method))

# The only non-standard method is phone, but it needs parameters.
# Anything other than the right string returns "He is not the evil"
# When we tried evil4.jpg in last challenge in Chrome it just shows
# a square, but in IE it shows "Bert is evil! Go back!" so we'll use 'Bert'

print(server.phone('Bert'))

# This returns our keyword