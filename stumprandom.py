from PIL import Image
import random

class Stumprandom:
    def __init__(self) -> None:
        pass
        
    def sameColor(self, pixel, color) -> bool:
        if pixel[0] == color[0] and pixel[1] == color[1] and pixel[2] == color[2]:
            return True

    def width(self, im: Image) -> Image:
        STUMP_COLOR = (176, 124, 63)
        rand = random.randint(0,3)

        pix = im.load()
        
        # Making things wider
        if rand == 1:
            for x in range(im.size[0]):
                for y in range(im.size[1]):
                    
                    if self.sameColor(pix[x,y], STUMP_COLOR) and not self.sameColor(pix[x - 1,y], STUMP_COLOR):
                        pix[x - 1, y] = STUMP_COLOR
                        print("Updating Stump at " + str(x) + ", " + str(y))

        return im