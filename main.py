"""
    Jpg To Png Convertor Using Python
"""

from PIL import Image

# input image from present folder
im1 = Image.open('input.jpg')

# output image is generated in the folder
im1.save('output.png')