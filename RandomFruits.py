import random
from PIL import Image

class RandomFruits:
    def __init__(self) -> None:
        pass


    def sameColor(self, pixel, color) -> bool:
        if pixel[0] == color[0] and pixel[1] == color[1] and pixel[2] == color[2]:
            return True

    def fruit(self, im: Image):
        LEAF_COLOR = (38, 129, 35)
        FRUIT = (0, 0, 0)

        rand = random.randint(1, 10)
        colorVariation = random.randint(-10, 10)
        if rand == 1:
            FRUIT = (200 + colorVariation, 0, 0)
        elif rand > 3 and rand < 6:
            FRUIT = (255 + colorVariation, 150 + colorVariation, 0)
        else:
            FRUIT = (0, 0, 0)
            return im

        pix = im.load()

        # Color randomizer
        for x in range(im.size[0]):
            for y in range(im.size[1]):
                if self.sameColor(pix[x,y], LEAF_COLOR):

                    rand = random.randint(0, 70)
                    if rand == 1:
                        print("Changing fruit at " + str(x) + ", " + str(y))
                        pix[x, y] = FRUIT

        return im