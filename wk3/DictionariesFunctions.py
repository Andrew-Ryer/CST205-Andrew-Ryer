import ast

# Task 1
color_dictionary = {
    'green' : (0, 255, 0),
    'blue' : (0, 0, 255),
    'magenta' : (255, 0, 255)
}

# Task 2
print(f'The green channel of Green has value {color_dictionary['green'][1]}')
print(f'The blue channel of Blue has value {color_dictionary['blue'][2]}')
print(f'The red and blue channel of Magenta has value {color_dictionary['magenta'][0]} \n')

# Task 3
tineye_sample = {
    "status": "ok",
    "error": [],
    "method": "extract_collection_colors",
    "result": [
        {
            "color": (141,125,83),
            "weight": 76.37,
            "name": "Clay Creek",
            "rank": 1,
            "class": "Grey"
        },
        {
            "color": (35,22,19),
            "weight": 23.63,
            "name": "Seal Brown",
            "rank": 2,
            "class": "Black"
        }
    ]
}
# print out the red channel of Clay Creekand
#               blue channel of Seal Brown
print(f'The red channel of Clay Creekand has value {tineye_sample["result"][0]["color"][0]}')
print(f'The blue channel of Seal Brown has value {tineye_sample["result"][1]["color"][2]} \n')

#Task 4
# Enter red: 23
# Enter green: 67
# Enter blue: 200
# Thank you, your RGB color is (23, 67, 200)
def color_input():
    red_val = input("Enter red: ")
    green_val = input("Enter green: ")
    blue_val = input("Enter blue: ")
    
    print(f'\nThank you, your RGB color is ({red_val}, {green_val}, {blue_val})\n')

color_input()

#Task 5
def  RGB_tuple():
    rgb_tuple = input("Enter an RGB tuple (r,g,b): ")
    RGB_tuple = ast.literal_eval(rgb_tuple)

    print(f'The red channel intensity is: {RGB_tuple[0]}')
    print(f'The green channel intensity is: {RGB_tuple[1]}')
    print(f'The blue channel intensity is: {RGB_tuple[2]}')

RGB_tuple()

#Task 6
def rgb_to_hex():
    rgb_text = input("\nEnter an RGB tuple (r,g,b): ")
    # example: (23, 67, 200)
    rgb = ast.literal_eval(rgb_text)

    r, g, b = rgb
    hex_color = f"#{r:02X}{g:02X}{b:02X}"

    print(f'Hex value is: {hex_color}')

rgb_to_hex()


# Task 7 (hex string -> RGB tuple)
def hex_to_rgb():
    hex_str = input('\nEnter a hex color (#RRGGBB): ')
    # example: #FF0000
    hex_str = hex_str.strip()

    if hex_str.startswith("#"):
        hex_str = hex_str[1:]

    r = int(hex_str[0:2], 16)
    g = int(hex_str[2:4], 16)
    b = int(hex_str[4:6], 16)

    print(f'RGB tuple is: ({r}, {g}, {b})')

hex_to_rgb()