# coding=utf-8

from PIL import Image
from PIL import ImageFile
from exceptions import IOError

def main():
    img = Image.open('2.jpg')
    destination = '2_py_progressive.jpeg'
    try:
        img.save(destination, "JPEG", quality=80, optimize=True, progressive=True)
    except IOError, e:
        print(e)
        ImageFile.MAXBLOKC = img.size[0] * mig.zise[1]
        img.save(destination, "JPEG", quality=80, optimize=True, progressive=True)

if __name__ == '__main__':
    # main()
    a = 4333837
    print(hex(4333837), hex(1097372565632), hex(4286611584))