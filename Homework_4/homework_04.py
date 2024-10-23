# Author: Arsen Sekmokas 
# Email: asekmokas@umass.edu 
# Spire ID: 34578570 

import pygame 
import numpy 
import PIL

from PIL import Image

pygame.init()

im_file = "testing_image.jpg"
im = Image.open(im_file)
size = im.size 

# set up screen size based on jpg's dimmensions 
if size[0]<size[1]: 
    length = size[0]
else: 
    length = size[1]
screen = pygame.display.set_mode((length, length))

# show original image 
og = pygame.image.load(im_file)
screen.blit(og, (0, 0))
pygame.display.update()
pygame.time.wait(200)

# global variables 
image = None 
rect = None 
angle = 0 

# crop and save image
A1 = im.crop((0, 0, length//4, length//4))
A1.save("A1.jpg") 
A1 = "A1.jpg"

def load_crop(position):
    global image, rect
    image = pygame.image.load(position)
    rect = image.get_rect()
    rect.x = 0 
    rect.y = 0

def check_click(pos): 
    return rect.collidepoint(pos) 

def rotate_crop(): 
    global image, rect, angle
    angle = (angle + 90) % 360 
    rotated_crop = pygame.transform.rotate(image, angle)
    rect = rotated_crop.get_rect(center=rect.center)
    return rotated_crop 


def func(position): 
    global image, rect
    clock = pygame.time.Clock() 
    load_crop(position)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if check_click(event.pos):
                    image = rotate_crop()
        
        # Clear screen(white vv) and draw the image
        screen.fill((255, 255, 255)) 
        screen.blit(image, rect.topleft)
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    func(A1)
    func(A2)


pygame.quit() 











#old code to use for later: 
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

#merged_image.show() 



