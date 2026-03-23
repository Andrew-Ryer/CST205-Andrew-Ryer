from PIL import Image
from pprint import pprint

#Task 1
'''
I believe that the class Image starts on line 617
'''
#Task 2
"""
    This class represents an image object.  To create
    :py:class:`~PIL.Image.Image` objects, use the appropriate factory
    functions.  There's hardly ever any reason to call the Image constructor
    directly.

    * :py:func:`~PIL.Image.open`
    * :py:func:`~PIL.Image.new`
    * :py:func:`~PIL.Image.frombytes`
"""
#Task 3
#pprint(dir(Image))
'''
merge
allows us to merge a set of single band images into a new multiband image.
parameters:
    mode: The mode to use for the output image.
    bands: A sequence containing one single-band image for each band in the output image.(All bands must have the same size)
returns an image object
'''
#Task 4
class Song:
    ''' a song class '''
    def __init__(self, name, artist, genre, length, album, cover_image=None):
        # instance variables unique to each instance
        self.name = name
        self.artist = artist
        self.genre = genre
        self.length = length
        self.album = album
        self.cover_image = cover_image

    def play(self):
        print(f'Now playing: "{self.name}" by {self.artist}.')
    
    def get_length_minutes(self):
        print(f'{self.length // 60}:{self.length % 60}')
    
    def show_cover(self):
        if self.cover_image is not None:
            self.cover_image.show()

Linkin_Park = Song('In the End', 'Linkin Park', 'Nu metal', 219, 'Hybrid Theory')
Imagine_Dragons = Song('Believer', 'Imagine Dragons', 'Pop rock', 217, 'Evolve')
Green_Day = Song('Holiday', 'GreenDay', 'Punk rock', 233, 'American Idiot')
print(Linkin_Park.name)
print(Imagine_Dragons.artist)
print(Green_Day.genre)

#Task 5
Song.play(Linkin_Park)
Song.get_length_minutes(Imagine_Dragons)

#Task 6
'''
Let each Song have an optional cover_image attribute. show_cover() written.
Updated __init__ method.
No cover images included, so it will default to None.
'''
Song.show_cover(Green_Day)