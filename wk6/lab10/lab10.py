from PIL import Image
from pprint import pprint

#Task 1 (from lab9 Task4)
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
    
    # Print " 'songName' by artist (album) [genre] - length (min:sec)""
    def __str__(self):
        minutes = self.length // 60
        seconds = self.length % 60
        return f'"{self.name}" by {self.artist} ({self.album}) [{self.genre}] - {minutes}:{seconds:02d}'

    def __eq__(self, other1):
        return (self.name == (other1.name))


    def play(self):
        print(f'Now playing: "{self.name}" by {self.artist}.')
    
    def get_length_minutes(self):
        print(f'{self.length // 60}:{self.length % 60}')
    
    def show_cover(self):
        if self.cover_image is not None:
            self.cover_image.show()

#lab9 stuff --------------------------
Linkin_Park = Song('In the End', 'Linkin Park', 'Nu metal', 219, 'Hybrid Theory')
Imagine_Dragons = Song('Believer', 'Imagine Dragons', 'Pop rock', 217, 'Evolve')
Green_Day = Song('Holiday', 'GreenDay', 'Punk rock', 233, 'American Idiot')
print(Linkin_Park.name)
print(Imagine_Dragons.artist)
print(Green_Day.genre)

Song.play(Linkin_Park)
Song.get_length_minutes(Imagine_Dragons)
print("\n")
#-------------------------------------

#Task 2
#Add an __str__() method to your Song class and try it out.
print(Linkin_Park)
print(Imagine_Dragons)
print(Green_Day)

#Task 3
#Add an __eq__() method to your Song class and try it out.
print(Linkin_Park == Imagine_Dragons)
print(Linkin_Park == Linkin_Park)

#Task 4
'''
The MyWidget subclass inherits from the QtWidgets Class and extends QWidget
class MyWidget(QtWidgets.QWidget):
'''

#Task 5
'''
Create a new Python class called MyImage. The purpose of this class is to wrap a Pillow Image
and provide a few basic operations in an object-oriented way.
Key features to include:
• __init__(self, filename) → loads an image file.
• grayscale(self) → converts the image to grayscale.
• shrink(self) → resizes the image
• crop_center(self, width, height) → crops a centered box from the image.
• save(self, outname) → saves the edited image to a new file.
You should write your own methods for grayscale, shrink, and crop_center
'''
class MyImage:
    ''' a image class '''
    def __init__(self, filename):
        self.filename = filename
        self.img = Image.open(filename)

    def grayscale(self):
        width, height = self.img.size

        for x in range(width):
            for y in range(height):
                r, g, b = self.img.getpixel((x, y))

                # compute grayscale value (luminance)
                gray = int((r + g + b)//3)

                # set pixel to gray using putpixel()
                self.img.putpixel((x, y), (gray, gray, gray))

        self.img.show()

    #Not enough time
    # def shrink(self):

    #Not enough time
    # def crop_center(self, width, height):

    #Untested
    def save(self, outname):
        self.img.save(outname)

#Try it out
img1 = MyImage("penguin.jpg")
img1.grayscale()