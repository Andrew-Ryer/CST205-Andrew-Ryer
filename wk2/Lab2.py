color_list = [ (227, 66, 52), (205, 96, 144), (28, 134, 238), (250, 250, 70), (245, 50, 245), (100, 231, 231)]

for color in color_list:
    if color[0] > color[1] and color[0] > color[2]:
        print(f'The color {color} is reddish.')
    elif color[0] < color[1] and color[1] > color[2]:
        print(f'The color {color} is greenish.')
    elif color[0] < color[2] and color[1] < color[2]:
        print(f'The color {color} is bluish.')

    if color[1] == color[2]:
        print(f'The color {color} is a shade of cyan.')
    elif color[0] == color[2]:
        print(f'The color {color} is a shade of magenta.')
    if color[0] == color[1]:
        print(f'The color {color} is a shade of yellow.')