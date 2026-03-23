from PIL import Image

#Task 1
im = Image.open('penguin.jpg')

negative_list = [(255-p[0], 255-p[1], 255-p[2]) for p in im.get_flattened_data()]
im.putdata(negative_list)

im.save('negative_penguin.png')

# double negative
negative_list2 = [(255-p[0], 255-p[1], 255-p[2]) for p in im.get_flattened_data()]
im.putdata(negative_list2)

im.save('not_negative_penguin.png')
# when we negate the negative, the image looks just like the original

#Task 2
# sunset code
sunset_list = [(p[0], p[1]//2, p[2]//2) for p in im.get_flattened_data()]
im.putdata(sunset_list)

im.save('sunset_penguin.png')

# revert
sunset_list2 = [(p[0], p[1]*2, p[2]*2) for p in im.get_flattened_data()]
im.putdata(sunset_list2)
# This filter is kind of unimpressive. It just looks like a red sheet is over the top of the image

#Task 3
# This fuction takes a pixel that is in a certain range, depending on the range a different calulation is preformed
def sepia(p):
    # tint shadows
    if p[0] < 63:
        r,g,b = int(p[0] * 1.1), p[1], int(p[2] * 0.9)
    # tint midtones
    elif p[0] > 62 and p[0] < 192:
        r,g,b = int(p[0] * 1.15), p[1], int(p[2] * 0.85)
    # tint highlights
    else:
        r = int(p[0] * 1.08)
        g,b = p[1], int(p[2] * 0.5)
    return (r, g, b)

sepia_list = [sepia(p) for p in im.get_flattened_data()]
im.putdata(sepia_list)
# I think that this filter does a better job at creating a sunset effect than our other code
im.save('sepia_penguin.png')