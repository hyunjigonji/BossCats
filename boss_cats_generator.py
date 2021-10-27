from PIL import Image
import numpy as np
import os
from random import randint

dirname = os.path.dirname(__file__)
dirname = "."
dimensions = 480, 480

for x in range(1, 51):
    b=11981207

    hd = (randint(0, 256), randint(0, 256), randint(0, 256))

    #eye color
    ew = (randint(0, 10), randint(0, 10), randint(0, 10))
    ey = (randint(0, 10), randint(0, 10), randint(0, 10))

    bk = (randint(0, 170), randint(0, 170), randint(0, 170))
    #bk = (hd[0]-50 if hd[0] >= 50 else hd[0], hd[1]-50 if hd[1] >= 50 else hd[1], hd[2]-50 if hd[2] >= 50 else hd[2])

    # background color
    bg = (randint(200, 256), randint(200, 256), randint(200, 256))
    # outline color
    ol = (0, 0, 0)

    cat = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, ol, bk, ol, bg, bg, bg, bg, bg, ol, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, ol, bk, bk, ol, ol, ol, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, ol, bk, bk, bk, bk, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg],
        [bg, bg, bg, ol, bk, bk, bk, bk, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg],
        [bg, bg, bg, ol, bk, bk, ew, hd, hd, hd, ew, hd, hd, ol, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg],
        [bg, bg, bg, ol, bk, bk, bk, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg],
        [bg, bg, bg, ol, bk, bk, hd, hd, ey, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, hd, hd, ey, hd, ey, hd, hd, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, hd, hd, hd, hd, hd, bk, bk, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, hd, hd, hd, hd, hd, hd, bk, bk, bk, ol, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, bk, hd, hd, hd, hd, hd, hd, bk, bk, ol, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, bk, bk, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, ol, ol, ol, bk, ol, ol, ol, hd, ol, ol, ol, hd, ol, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, hd, ol, bg, ol, bk, ol, bg, ol, hd, ol, bg, ol, hd, ol, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, ol, ol, bg, ol, ol, ol, bg, ol, ol, ol, bg, ol, ol, ol, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
    ]

    pixels = cat
    p = "cat"
    # convert the pixels into an array using numpy
    array = np.array(pixels, dtype=np.uint8)

    # use PIL to create an image from the new array of pixels
    new_image = Image.fromarray(array)
    new_image = new_image.resize(dimensions, resample=0)
    imgname = dirname + '/cat_images/' + (str(x)) + '.png'
    new_image.save(imgname)
