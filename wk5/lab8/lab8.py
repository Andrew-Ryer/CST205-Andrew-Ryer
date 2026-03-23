from PIL import Image
from colorthief import ColorThief
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
import numpy
import math

#Task 1
img1 = Image.open("apple.jpg")
width = img1.width
height = img1.height
my_trgt = Image.new('RGB', (width+300,height+300), 'salmon')

target_x = 50
for source_x in range(width):
    target_y = 50
    for source_y in range(height):
        p = img1.getpixel((source_x, source_y))
        my_trgt.putpixel((target_x, target_y), p)
        target_y += 1
    target_x += 1

img2 = Image.open("apple.jpg")

target_x = 200
for source_x in range(width):
    target_y = 200
    for source_y in range(height):
        p = img2.getpixel((source_x, source_y))
        my_trgt.putpixel((target_x, target_y), p)
        target_y += 1
    target_x += 1

my_trgt.show()
my_trgt.save('appleOverlap.png')

#Task 2
img1_2 = Image.open("apple.jpg")

my_trgt2 = Image.new('RGB', ((width*2)+300,(height*2)+300), 'salmon')

target_x = 50
for source_x in range(width):
    target_y = 50
    for source_y in range(height):
        p = img1.getpixel((source_x, source_y))
        my_trgt2.putpixel((target_x, target_y), p)
        target_y += 1
    target_x += 1

img2 = Image.open("apple.jpg")

target_x = width+100
for source_x in range(width):
    target_y = height+100
    for source_y in range(height):
        p = img2.getpixel((source_x, source_y))
        my_trgt2.putpixel((target_x, target_y), p)
        target_y += 1
    target_x += 1

my_trgt2.show()
my_trgt2.save('appleNotOverlap.png')

#Task 3

#Code from lab7
def delta_e_distance(pixel_rgb, ref_rgb):
    pixel_lab = convert_color(
        sRGBColor(pixel_rgb[0], pixel_rgb[1], pixel_rgb[2], is_upscaled=True),
        LabColor
    )
    ref_lab = convert_color(
        sRGBColor(ref_rgb[0], ref_rgb[1], ref_rgb[2], is_upscaled=True),
        LabColor
    )
    return delta_e_cie2000(pixel_lab, ref_lab)

def patch_asscalar(a):
    return a.item()
setattr(numpy, "asscalar", patch_asscalar)

#Reference Rosource
#https://stackoverflow.com/questions/51719472/remove-green-background-screen-from-image-using-opencv-python

#chromakey
threshold=25
foreground = Image.open("apple.jpg").convert("RGB")
background = Image.new("RGB", (width + 300, height + 300), "salmon")

# reference chroma pixel
refp = foreground.getpixel((5, 5))  # choose a pixel that is definitely the screen color
# chroma key replacement
for x in range(foreground.width):
    for y in range(foreground.height):
        cur_pixel = foreground.getpixel((x, y))
        if delta_e_distance(cur_pixel, refp) < threshold:
            foreground.putpixel((x, y), background.getpixel((x, y)))

# Takes very long to load
# result
foreground.show()
foreground.save('appleChromaKey.png')