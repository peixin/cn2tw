# coding=utf-8

import os
import os.path as path
from PIL import Image
import glob

thumn_size = 50, 15

def test():
    im = Image.open("8001.jpg")
    im.rotate(45).show()

def main():
    # origin_list = [x for x in os.listdir('coordMap') if path.splitext(x)[1].lower() == '.jpg']
    for infile in glob.glob('coordMap/*.jpg'):
        file_name, ext = path.splitext(infile)
        file_path, file_name = path.split(file_name)
        im = Image.open(infile)
        im.thumbnail(thumn_size, Image.ANTIALIAS)
        im.save(path.join('thumb', file_name) + ext, 'JPEG')


if __name__ == '__main__':
    test()