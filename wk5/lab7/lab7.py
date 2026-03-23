from PIL import Image
from colorthief import ColorThief
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
import numpy
import math

#Task 1
image1 = Image.open('valley.jpg')

average_list = [((a[0] + a[1] + a[2] )//3,) * 3 for a in image1.get_flattened_data()]

image1.putdata(average_list)
image1.save('average_valley.png')
# image1.show()

#Task 2
image2 = Image.open('valley.jpg')

luminance_list = [((a[0]*299 + a[1]*587 + a[2]*114 )//1000,) * 3 for a in image2.get_flattened_data()]

image2.putdata(luminance_list)
image2.save('luminance_valley.png')
# image2.show()

#Compare:
# The luminance_list has more vivid blacks than the average_list

#Task 3
color_thief = ColorThief('valley.jpg')
dominant_color = color_thief.get_color(quality=1)
print(dominant_color)
#print("\n")

#Task 4
def patch_asscalar(a):
    return a.item()
setattr(numpy, "asscalar", patch_asscalar)

#L*A*B* color distance
apple1 = sRGBColor(176, 63, 81, True)
apple2 = sRGBColor(185, 77, 89, True)

apple1_lab = convert_color(apple1, LabColor)
apple2_lab = convert_color(apple2, LabColor)

delta_lab = delta_e_cie2000(apple1_lab, apple2_lab)

print(f'The lab difference is {delta_lab}.')

#Task 5
#Euclidean color distance'
apple1_e = (176, 63, 81)
apple2_e = (185, 77, 89)
def color_distance_Euclidean(c1, c2):
    r_diff = (c1[0] - c2[0])**2
    g_diff = (c1[1] - c2[1])**2
    b_diff = (c1[2] - c2[2])**2
    return (r_diff + g_diff + b_diff)**(1/2)

delta_E = color_distance_Euclidean(apple1_e, apple2_e)

print(f'The Euclidean difference is {delta_E}.')

#Compare:
# The The lab difference is 4.085359189274008.
# The Euclidean difference is 18.466185312619388.
# Difference is about 14 units