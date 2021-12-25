from PIL import Image
from stumprandom import Stumprandom
from RandomColor import RandomColor
from RandomFruits import RandomFruits
import random

THRESHOLD = 5

def luminance(pixel):
    return (0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2])


def is_similar(pixel_a, pixel_b, threshold):
    return abs(luminance(pixel_a) - luminance(pixel_b)) < threshold

def sameColor(pixel, color):
    if pixel[0] == color[0] and pixel[1] == color[1] and pixel[2] == color[2]:
        return True

def main():

    trees = ['big leaves.png', 'tall tree.png', 'tree lol.png', 'tree with clouds.png']

    for i in range(20):
        tree = trees[random.randint(0, len(trees) - 1)]
        im = Image.open('./assets/' + tree)

        stump = Stumprandom()
        randomColor = RandomColor()
        randomFruits = RandomFruits()

        im = stump.width(im)
        im = randomFruits.fruit(im)
        im = randomColor.stumpColor(im)
        im = randomColor.leavesColor(im)

        im = im.resize((500, 500), Image.NEAREST)        

        im.save("./output/" + str(i) + ".png")

main()