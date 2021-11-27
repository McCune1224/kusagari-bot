import numpy as np 
from PIL import Image
import sys
import random
import math
import requests

#Gray Scale values in text: http://paulbourke.net/dataformats/asciiart/

grayscale_complex = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
grayscale_simple = '@%#*+=-:. '

def imageDownload(url):
    with requests.get(url, stream=True) as r:
        with open("temp.jpg", "wb") as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
    image = Image.open("temp.jpg").convert('L')
    return image

def getGrayscale(image):
    im = np.array(image)
    width , height = im.shape
    return np.average(im.reshape(width*height))

def imageToAscii(image, cols = 80, scale = 0.8, complex=False):

    W, H = image.size[0], image.size[1]

    w = W/cols
    
    # compute tile height based on aspect ratio and scale
    h = w/scale

    # compute number of rows
    rows = int(H/h)
    

    #scale resolution down to not exceeed discord's 2000 character limit

    print("cols: %d, rows: %d" % (cols, rows))
    print("tile dims: %d x %d" % (w, h))

    # check if image size is too small
    if cols > W or rows > H:
        print("Image too small for specified cols!")
        exit(0)

    # ascii image is a list of character strings
    aimg = []
    # generate list of dimensions
    for j in range(rows):
        y1 = int(j*h)
        y2 = int((j+1)*h)

        # correct last tile
        if j == rows-1:
            y2 = H

        # append an empty string
        aimg.append("")

        for i in range(cols):

            # crop image to tile
            x1 = int(i*w)
            x2 = int((i+1)*w)

            # correct last tile
            if i == cols-1:
                x2 = W

            # crop image to extract tile
            img = image.crop((x1, y1, x2, y2))

            # get average luminance
            avg = int(getGrayscale(img))

            # look up ascii char
            if complex:
                gsval = grayscale_complex[int((avg*69)/255)]
            else:
                gsval = grayscale_simple[int((avg*9)/255)]

            # append ascii char to string
            aimg[j] += gsval
    
    out_file = "final.txt"
    f = open(out_file, 'w')

    # write to file
    for row in aimg:
        f.write(row + '\n')
    # cleanup
    f.close()

    print(f"ASCII art written to {out_file}") 
if __name__ == "__main__":
    image_source = input("insert image url:")
    image = imageDownload(image_source)
    imageToAscii(image)
    
