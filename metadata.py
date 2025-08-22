import eyed3
import time
import os



# path = "Song\\How It_s Done.mp3"
# # print(eyed3.AudioFile(path))
# file = eyed3.load(path)
# length = file.info.time_secs
# length = round(length)
# print(length)
# album = file.tag.album
# print(album)
# artist = file.tag.artist
# print(artist)
# title = file.tag.title
# print(title)
# year = file.tag.getBestDate()
# print(year)


# SecToConvert = length

# Convertedformat = time.strftime("%M:%S", time.gmtime(SecToConvert))
# print()
# print("After converting the seconds :", Convertedformat)
open("songs.txt", "w").close()

for filename in os.listdir('Song'):
    #  print(filename)

     dir = "Song\\" + filename
    #  print(dir)

     file = eyed3.load(dir)
     length = file.info.time_secs
     length = round(length)
     album = file.tag.album
     artist = file.tag.artist
     title = file.tag.title
     year = file.tag.getBestDate()
     with open("songs.txt", "a") as tex:
        tex.write("name: \"" + file.tag.title + "\",\n")
        tex.write("artist: \"" + file.tag.title + "\",\n")
        tex.write("image: \"" + "https://images.pexels.com/photos/3100835/pexels-photo-3100835.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=250&w=250\",\n")
        tex.write("path: \"" + dir + "\"\n\n")


