# Author: Arsen Sekmokas 
# Email: asekmokas@umass.edu 
# Spire ID: 34578570 

import pygame 
import numpy 
import PIL

from PIL import Image

im_file = "testing_image.jpg"

im = Image.open(im_file)
# im.rotate(90).show()
size = im.size 

def crop(im_file): 
    A1 = im.crop((0, 0, 200, 200)) 
    A2 = im.crop((200, 0, 400, 200))
    A3 = im.crop((400, 0, 600, 200))
    A4 = im.crop((600, 0, 800, 200))
    B1 = im.crop((0, 200, 200, 400))
    B2 = im.crop((200, 200, 400, 400))
    B3 = im.crop((400, 200, 600, 400))
    B4 = im.crop((600, 200, 800, 400))
    C1 = im.crop((0, 400, 200, 600))
    C2 = im.crop((200, 400, 400, 600))
    C3 = im.crop((400, 400, 600, 600))
    C4 = im.crop((600, 400, 800, 600))
    D1 = im.crop((0, 600, 200, 800))
    D2 = im.crop((200, 600, 400, 800))
    D3 = im.crop((400, 600, 600, 800))
    D4 = im.crop((600, 600, 800, 800))

crop(im_file)

A1 = im.crop((0, 0, 200, 200)) 
A2 = im.crop((200, 0, 400, 200))

# make sure both images have the same size 
if A1.size != A2.size: 
    A2 = A2.resize(A1.size)

# blend images 
merged_image = Image.new('RGB', (400, 200))

merged_image.paste(A1, (0, 0))

merged_image.paste(A2, (200, 0))

merged_image.show() 
