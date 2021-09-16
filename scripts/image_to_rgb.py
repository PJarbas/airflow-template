#!/usr/bin/env python3

import sys
from PIL import Image
import numpy as np
from datetime import date
import pathlib


class ToRGB:
    def __init__(self, image_name):
        """
        Get a single image and create 3 new images with r, g, b decompositions
        :param image_name: name of image
        """

        self.img = Image.open(image_name)

        self.width, self.height = self.img.size
    
    def run(self):
        for color in ['red', 'green', 'blue']:
            self.single_color(color)

    def pixel(self, r, g, b, color):
        """

        :return: tuple with pixel R G B
        """

        color_dict = {'red': (r, 0, 0),
                      'green': (0, g, 0),
                      'blue': (0, 0, b)}

        return color_dict[color]

    def single_color(self, color):
        """

        :param image: object PIL ImageFile
        :param color: string with color ex: 'red'
        """
        image_out = self.img.copy()
        image = image_out.load()
        for x in range(self.width):
            for y in range(self.height):
                r, g, b = self.img.getpixel((x, y))
                image[x, y] = self.pixel(r, g, b, color)

        pathlib.Path("output").mkdir(parents=True, exist_ok=True)
        
        image_out.save('output/{0}.png'.format(color))


if __name__ == "__main__":

    file_name = f"data/dog_{date.today().strftime('%Y-%m-%m')}.jpg"
    
    process = ToRGB(file_name).run()
    print("image to RGB Done!")