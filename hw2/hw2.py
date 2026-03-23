"""
Name: Andrew Ryer
Class: CST 205
Date: 2-15-2026
Homework 2
"""

from PIL import Image
from glob import glob

def load_images(location, type):
    img_list = []
    for image in glob(f'{location}/*.{type}'):
        img_list.append(Image.open(image))
    return img_list

# Task 1 - Code for my_median() function
def my_median(int_list):
    # make a copy of the list
    nums = int_list.copy()
    # sort the copied list
    nums.sort()

    # calculate the middle location
    mid_index = (len(nums)) // 2

    # return value at middle location
    return nums[mid_index]

# Testing
# list = [2, 4, 6, 237, 1]
# print(my_median(list))

#--------------------------------------------------------------------\

# Task 2
# load_images('task2_images', 'png')
def task2():
    # returns a list of PIL Images found in the folder
    imgs = load_images('task2_images', 'png')

    # Grab the first three images from the list
    img1 = imgs[0]
    img2 = imgs[1]
    img3 = imgs[2]

    # Convert each image to RGB mode (guarantees pixels are (R, G, B))
    img1 = img1.convert("RGB")
    img2 = img2.convert("RGB")
    img3 = img3.convert("RGB")

    # Get width and height from the first image
    w = img1.size[0]   # width
    h = img1.size[1]   # height

    # Create a blank output image with the same size
    out = Image.new("RGB", (w, h))

    # Get pixel-access objects (lets you read/write pixels using [x, y])
    p1 = img1.load()
    p2 = img2.load()
    p3 = img3.load()
    po = out.load()

    # Loop through every pixel location
    for y in range(h):
        for x in range(w):
            # Get the RGB pixel from each image at (x, y)
            r1, g1, b1 = p1[x, y]
            r2, g2, b2 = p2[x, y]
            r3, g3, b3 = p3[x, y]

            # Take median per channel
            r_med = my_median([r1, r2, r3])
            g_med = my_median([g1, g2, g3])
            b_med = my_median([b1, b2, b3])

            # Write the median pixel to the output image
            po[x, y] = (r_med, g_med, b_med)

    out.save("task2.png")
    return out

# run it
task2()

#--------------------------------------------------------------------

# Task 3
# load_images('task3_images', 'png')
def task3():
    imgs = load_images('task3_images', 'png')

    # Convert each image to RGB mode
    for i in range(len(imgs)):
        imgs[i] = imgs[i].convert("RGB")

    # Get width and height from the first image
    w = imgs[0].size[0]   # width
    h = imgs[0].size[1]   # height

    # Create a blank output image with the same size
    out = Image.new("RGB", (w, h))

    # Pixel access for output image
    po = out.load()

    # Pixel access objects for each input image
    pixel_lists = []
    for i in range(len(imgs)):
        pixel_lists.append(imgs[i].load())

    # Loop through every pixel location
    for y in range(h):
        for x in range(w):

            # Build lists of all R, G, B values at (x, y) across the images
            r_vals = []
            g_vals = []
            b_vals = []

            for i in range(len(pixel_lists)):
                r, g, b = pixel_lists[i][x, y]
                r_vals.append(r)
                g_vals.append(g)
                b_vals.append(b)

            # Take median per channel across ALL images
            r_med = my_median(r_vals)
            g_med = my_median(g_vals)
            b_med = my_median(b_vals)

            # Write the median pixel to the output image
            po[x, y] = (r_med, g_med, b_med)

    out.save("task3.png")
    return out

# run it
task3()

# Code to perform median filter and generate new image.