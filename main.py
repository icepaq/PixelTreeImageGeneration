from PIL import Image
from stumprandom import Stumprandom
from RandomColor import RandomColor
from RandomFruits import RandomFruits

THRESHOLD = 5

def luminance(pixel):
    return (0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2])


def is_similar(pixel_a, pixel_b, threshold):
    return abs(luminance(pixel_a) - luminance(pixel_b)) < threshold

def sameColor(pixel, color):
    if pixel[0] == color[0] and pixel[1] == color[1] and pixel[2] == color[2]:
        return True

def main():
    im = Image.open("./assets/tree lol.png")

    stump = Stumprandom()
    randomColor = RandomColor()
    randomFruits = RandomFruits()


    im = stump.width(im)
    im = randomFruits.fruit(im)
    im = randomColor.stumpColor(im)
    im = randomColor.leavesColor(im)

    im = im.resize((500, 500), Image.NEAREST)
    

    im.save("tree lol 2.png")

main()