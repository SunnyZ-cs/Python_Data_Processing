#!/usr/bin/env python3

"""
Python Portfolio Project: Image Grid Project
"""

import sys
import random

# This line imports SimpleImage for use here
# This depends on the Pillow package
from simpleimage import SimpleImage


def draw_image(image, out, left, top, mode):
    """
    Draw a copy of "image" into "out", with image's origin
    at (left, top) within the out image.
    Mode is one of 'red' 'green' 'blue' 'all',
    controlling which colors of each pixel are copied.
    (See handout for details)
    """
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            out_pixel = out.get_pixel(x + left, y + top)
            if mode == 'red':
                out_pixel.red = pixel.red
            if mode == 'green':
                out_pixel.green = pixel.green
            if mode == 'blue':
                out_pixel.blue = pixel.blue
            if mode == 'all':
                out_pixel.red = pixel.red
                out_pixel.green = pixel.green
                out_pixel.blue = pixel.blue
    return out







def make_channels(filename):
    """
    Given an image filename.
    Creates an out image with 3x the width,
    filled with the red, green, and blue channels
    of the original image.
    """
    image = SimpleImage(filename)
    # Specifying 'black' as the color for the blank image.
    out = SimpleImage.blank(image.width * 3, image.height, back_color='black')

    # -your code here-
    draw_image(image, out, 0, 0, 'red')
    draw_image(image, out, image.width, 0, 'green')
    draw_image(image, out, 2 * image.width, 0, 'blue')

    out.show()  # Show output on screen


def make_art(filename, n):
    """
    Given an image filename, create an out
    image and draw the channels on it as
    described in the handout.
    """
    image = SimpleImage(filename)
    # Create black image with 2 * n extra space
    out = SimpleImage.blank(image.width + 2 * n, image.height + 2 * n, back_color='black')

    # -your code here-
    draw_image(image, out, 0, 0, 'red')
    draw_image(image, out, n, n, 'green')
    draw_image(image, out, 2 * n, 2 * n, 'blue')

    out.show()  # Show output on screen


def make_test(filename):
    """
    Uses draw_image() to create a larger blue background
    with the image centered on it as a basic test.
    (provided code)
    """
    image = SimpleImage(filename)
    top_margin = 20
    side_margin = 40
    out = SimpleImage.blank(image.width + side_margin * 2, image.height + top_margin * 2, back_color='blue')
    draw_image(image, out, side_margin, top_margin, 'all')
    out.show()


def make_grid(filename, n, plain):
    """
    Create an n x n grid image of the given image filename.
    If plain is True, the images are copied plain.
    If plain is False, random color versions of each
    are used.
    (provided code)
    """
    image = SimpleImage(filename)
    out = SimpleImage.blank(image.width * n, image.height * n, back_color='black')
    # Row and col numbers identify the individual rows and columns
    # e.g. 3 columns would use numbers 0, 1, 2
    for row in range(n):
        for col in range(n):
            # Based on row/col numbers compute the left/top of each image
            if plain:
                draw_image(image, out, col * image.width, row * image.height, 'all')
            else:
                # This selects one of the colors at random
                choice = random.choice(['red', 'green', 'blue'])
                draw_image(image, out, col * image.width, row * image.height, choice)
    out.show()


def main():
    # (Core Utility)
    args = sys.argv[1:]

    # Usability - error message for malformed command line args
    # since this is their first use of the command line.
    if len(args) >= 1:
        if args[0] == '-hello':
            if len(args) != 2:
                return

        if args[0] in ['-test', '-channels']:
            if len(args) != 2:
                print('command line syntax error\nusage: ' + args[0] + ' image-filename')
                return

        if args[0] in ['-art', '-grid', '-random']:
            if len(args) != 3 or not args[2].isdigit():
                print('command line syntax error\nusage: ' + args[0] + ' image-filename n')
                return

    # -hello name
    if len(args) == 2 and args[0] == '-hello':
        print("Everything's coming up", args[1] + '!')

    # -test img
    if len(args) == 2 and args[0] == '-test':
        make_test(args[1])

    # -channels img
    if len(args) == 2 and args[0] == '-channels':
        make_channels(args[1])

    # -art img n
    if len(args) >= 1 and args[0] == '-art':
        n = int(args[2])
        make_art(args[1], n)

    # -grid img n
    if len(args) == 3 and args[0] == '-grid':
        n = int(args[2])
        make_grid(args[1], n, True)

    # -random img n
    if len(args) == 3 and args[0] == '-random':
        n = int(args[2])
        make_grid(args[1], n, False)


if __name__ == '__main__':
    main()
