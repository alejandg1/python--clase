from PIL import Image

import os

downloadFolder ='/Users/USUARIO/Music/Workspace/projects/capturas'

if __name__ == "__main__":
    for filename in os.listdir(downloadFolder):
        name,extension = os.path.splitext(downloadFolder+filename)

        if extension in [".jpg","jpeg","png"]:
            picture = Image.open(downloadFolder + filename)
            picture.save( downloadFolder + "compressed_"+filename, optimize= True, quality = 60 )