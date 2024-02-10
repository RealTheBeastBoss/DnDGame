from game import *

class Dice:
    def __init__(self, sides):
        self.sides = sides
        self.sideFacing = sides
        match sides:
            case 6:
                self.sideImage = D6_IMAGES
    def draw(self, x, y):
        dice_width = self.sideImage[self.sideFacing][1][0] * 2
        dice_height = self.sideImage[self.sideFacing][1][1] * 2
        dice_image = self.sideImage[self.sideFacing][0]
        dice_image = pygame.transform.scale(dice_image, (dice_width, dice_height))
        WINDOW.blit(dice_image, (x, y))