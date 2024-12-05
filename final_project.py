# Author: Arsen Sekmokas 
# Email: asekmokas@umass.edu 
# Spire ID: 34578570 

import pygame
import random
from PIL import Image

pygame.init()

class ImageCropper:
    def __init__(self, im_file): 
        self.im_file = im_file 
        self.im = Image.open(im_file) 
        self.size = self.im.size 
        self.image = None 
        self.rect = None 

        #Initialize angles for each crop with random rotations 
        self.angle = {crop: random.choice([90, 180, 270]) for crop in ["A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4", "C1", "C2", "C3", "C4", "D1", "D2", "D3", "D4"]} 

        self.length = min(self.size[0], self.size[1]) 
        self.screen = pygame.display.set_mode((self.length, self.length)) 

        #Positions and sizes for crops 
        self.crop_positions = {
            "A1": (0, 0, self.length // 4, self.length // 4), 
            "A2": (self.length // 4, 0, self.length // 2, self.length // 4), 
            "A3": (self.length // 2, 0, self.length * 3 // 4, self.length // 4), 
            "A4": (self.length * 3 // 4, 0, self.length, self.length // 4),
            "B1": (0, self.length // 4, self.length // 4, self.length // 2),
            "B2": (self.length // 4, self.length // 4, self.length // 2, self.length // 2), 
            "B3": (self.length // 2, self.length // 4, self.length * 3 // 4, self.length // 2), 
            "B4": (self.length * 3 // 4, self.length // 4, self.length, self.length // 2), 
            "C1": (0, self.length // 2, self.length // 4, self.length * 3 // 4), 
            "C2": (self.length // 4, self.length // 2, self.length // 2, self.length * 3 // 4), 
            "C3": (self.length // 2, self.length // 2, self.length * 3 // 4, self.length * 3 // 4), 
            "C4": (self.length * 3 // 4, self.length // 2, self.length, self.length * 3 // 4),
            "D1": (0, self.length * 3 // 4, self.length // 4, self.length), 
            "D2": (self.length // 4, self.length * 3 // 4, self.length // 2, self.length), 
            "D3": (self.length // 2, self.length * 3 // 4, self.length * 3 // 4, self.length), 
            "D4": (self.length * 3 // 4, self.length * 3 // 4, self.length, self.length) 
        }

        self.crops = {}
        for crop_name, pos in self.crop_positions.items():
            left, top, right, bottom = pos
            self.crops[crop_name] = self.crop_image(left, top, right, bottom)

        self.font = pygame.font.SysFont("Arial", 48)

    #Crop each image
    def crop_image(self, left, top, right, bottom): 
        crop = self.im.crop((left, top, right, bottom)) 
        filename = f"{left}_{top}_{right}_{bottom}.jpg" 
        crop.save(filename) 
        return filename 
    
    #Load the cropped image 
    def load_crop(self, crop_name):
        self.image = pygame.image.load(self.crops[crop_name])
        self.rect = self.image.get_rect()
        x, y = self.crop_positions[crop_name][0], self.crop_positions[crop_name][1]
        self.rect.topleft = (x, y)

        self.image = pygame.transform.rotate(self.image, self.angle[crop_name])
        self.rect = self.image.get_rect(center=self.rect.center) 

    #Check if a cropped image was clicked 
    def check_click(self, pos):
        return self.rect.collidepoint(pos)

    #Rotate when clicked
    def rotate_crop(self, crop_name):
        if crop_name in self.angle:
            self.angle[crop_name] += 90
            if self.angle[crop_name] == 360:
                self.angle[crop_name] = 0
            self.image = pygame.transform.rotate(self.image, 90)
            self.rect = self.image.get_rect(center=self.rect.center)

    #Display the crop at its current position
    def display_crop(self, crop_name): 
        self.load_crop(crop_name)
        self.screen.blit(self.image, self.rect)

    #Check if all pieces are rotated correctly
    def is_puzzle_solved(self):
        for crop_name in self.angle:
            if self.angle[crop_name] != 0:
                return False
        return True

    #Fade in and out of white to show user they have finished 
    def fade_to_white(self):
        white_surface = pygame.Surface((self.length, self.length)) 
        white_surface.fill((255, 255, 255)) 
        self.screen.blit(white_surface, (0, 0)) 
        pygame.display.flip() 
        pygame.time.wait(500) 

    #Fade back to puzzle and show message
    def show_congratulations(self): 
        self.fade_to_white() 

        for crop_name in self.crops:
            self.display_crop(crop_name)
        pygame.display.flip()

        pygame.time.wait(500)

        message = self.font.render("You did it!", True, (80, 200, 120)) 
        message_rect = message.get_rect(center=(self.length // 2, self.length // 2))
        self.screen.blit(message, message_rect)
        pygame.display.flip()

        pygame.time.wait(3500) 

    def run(self): 
        running = True 
        selected_crop = None 

        while running: 
            self.screen.fill((255, 255, 255)) 

            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    running = False 

                if event.type == pygame.MOUSEBUTTONDOWN: 
                    mouse_pos = pygame.mouse.get_pos() 
                    for crop_name in self.crops: 
                        self.load_crop(crop_name) 
                        if self.check_click(mouse_pos): 
                            selected_crop = crop_name 
                            print(f"{crop_name} clicked!")
                            self.rotate_crop(crop_name) 
                            break 

            for crop_name in self.crops:
                self.display_crop(crop_name)

            if self.is_puzzle_solved():
                self.show_congratulations()
                break 

            pygame.display.flip() 
        pygame.quit() 

#Call function 
im_file = "testing_image1.jpg" 
image_cropper = ImageCropper(im_file)
image_cropper.run()
