from PIL import Image
import random

class RandomColor:
    def __init__(self) -> None:
        pass


    def sameColor(self, pixel, color) -> bool:
        if pixel[0] == color[0] and pixel[1] == color[1] and pixel[2] == color[2]:
            return True

    def stumpColor(self, im: Image):
        STUMP_COLOR = (176, 124, 63)
        rand = random.randint(0, 3)

        offset = random.randint(-30, 0)

        pix = im.load()
        
        # Color randomizer
        for x in range(im.size[0]):
            for y in range(im.size[1]):
                
                if self.sameColor(pix[x,y], STUMP_COLOR):
                    print("Changing color at " + str(x) + ", " + str(y))
                    
                    NEW_STUMP_COLOR = (STUMP_COLOR[0] + random.randint(-10,10) + offset, 
                                       STUMP_COLOR[1] + random.randint(-10,10) + offset, 
                                       STUMP_COLOR[2] + random.randint(-10,10) + offset)

                    pix[x, y] = NEW_STUMP_COLOR

        return im

    def leavesColor(self, im: Image):
        LEAF_COLOR = (38, 129, 35)
        rand = random.randint(0,3)

        pix = im.load()
        
        # Color randomizer
        for x in range(im.size[0]):
            for y in range(im.size[1]):
                
                if self.sameColor(pix[x,y], LEAF_COLOR):
                    print("Changing color at " + str(x) + ", " + str(y))
                    NEW_LEAF_COLOR = (LEAF_COLOR[0] + random.randint(-20,20), LEAF_COLOR[1] + random.randint(-20,20), LEAF_COLOR[2] + random.randint(-20,20))
                    pix[x, y] = NEW_LEAF_COLOR

        return im