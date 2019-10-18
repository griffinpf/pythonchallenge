################################################################
#Challenge 7: http://www.pythonchallenge.com/pc/def/oxygen.html#
################################################################

from PIL import Image

im = Image.open("C:/Users/pgriffi2/AppData/Local/Programs/Python/Python36-32/pythonchallenge/resources/oxygen.png")

d = {}

# Get counts of how many pixels are each color
for x in range(im.width):
    for y in range(im.height):
        if im.getpixel((x,y)) in d:
            d[im.getpixel((x,y))] += 1
        else:
            d[im.getpixel((x,y))] = 1

# The gray boxes are 7 pixels across and are right in the middle
chars = []
for x in range(im.width):
    if x % 7 == 0:
        # RGB values for grays are all the same number, so just grab the first one
        chars.append(im.getpixel((x,(im.height//2)))[0])        

# They look like ASCII values, so print out what that string would look like
print(''.join(chr(i) for i in chars))

# The hint is that the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121], so let's decode those too
hint = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print(''.join(chr(i) for i in hint))