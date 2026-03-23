"""
Name: Andrew Ryer
Class: CST 205
Date: 3-13-2026
Homework 3 - my_search() function should take a single’ string argument and return an image id or “no results”.
"""

from PIL import Image
from image_info import image_info

# used to appy our image and manipulations
OUTPUT_FILE = "temp_output.jpg"

# Searches for terms in image_info
def my_search(term):
    term = term.strip().lower()
    if term == "":
        return "no results"

    best_id = "no results"
    best_score = 0

    for item in image_info:
        score = 0
        # Increase the score if title appears
        title_words = item["title"].lower().split()
        if term in title_words:
            score += 1
        # Increase the score if term appears
        tags_lower = [tag.lower() for tag in item["tags"]]
        if term in tags_lower:
            score += 1
        # Compares the best score
        if score > best_score:
            best_score = score
            best_id = item["id"]
    # No matching results
    if best_score == 0:
        return "no results"
    # Return ID with best match (most score)
    return best_id

# Find the correct image based on ID (else return the no_results.jpg)
def image_path_from_id(image_id):
    if image_id == "no results":
        return "no_results.jpg"
    return f"{image_id}.jpg"

# Based on selection from drop down menu, apply proper manipulation
def apply_manipulation(image_path, manipulation):
    manipulation = manipulation.lower()

    # no_results.jpg = no manipulation
    if image_path == "no_results.jpg":
        return image_path

    if manipulation == "none":
        return image_path

    img = Image.open(image_path).convert("RGB")
    w, h = img.size

    # thumbnail returns image but "zoomed in"
    if manipulation == "thumbnail":
        new_img = Image.new("RGB", (w // 2, h // 2))
        for y in range(h // 2):
            for x in range(w // 2):
                new_img.putpixel((x, y), img.getpixel((x, y)))
        new_img.save(OUTPUT_FILE)
        return OUTPUT_FILE

    pixels = list(img.getdata())
    new_pixels = []

    # Make black and white
    if manipulation == "grayscale":
        for r, g, b in pixels:
            gray = (r + g + b) // 3
            new_pixels.append((gray, gray, gray))

    # reverse RGB values
    elif manipulation == "negative":
        for r, g, b in pixels:
            new_pixels.append((255 - r, 255 - g, 255 - b))

    # Specific RGB values applied
    elif manipulation == "sepia":
        for p in pixels:
            # tint shadows
            if p[0] < 63:
                r, g, b = int(p[0] * 1.1), p[1], int(p[2] * 0.9)

            # tint midtones
            elif p[0] > 62 and p[0] < 192:
                r, g, b = int(p[0] * 1.15), p[1], int(p[2] * 0.85)

            # tint highlights
            else:
                r = int(p[0] * 1.08)
                g, b = p[1], int(p[2] * 0.5)

            r = min(255, r)
            g = min(255, g)
            b = min(255, b)

            new_pixels.append((r, g, b))
    else:
        return image_path

    new_img = Image.new("RGB", img.size)
    new_img.putdata(new_pixels)
    new_img.save(OUTPUT_FILE)
    return OUTPUT_FILE