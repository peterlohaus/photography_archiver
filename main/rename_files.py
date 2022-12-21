import os
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime
import settings

def renameFiles():
    basePath = './' + settings.INPUT_FOLDER_NAME + '/'
    fileNames = os.listdir(basePath)
    for fileName in fileNames:
        image = Image.open(basePath + fileName)
        exif = image.getexif()
        image.close()
        timestamp = datetime.strptime(exif.get(306), '%Y:%m:%d %H:%M:%S')
        make = exif.get(271)
        model = exif.get(272)
        fileBaseName, fileExtension = os.path.splitext(fileName)
        newFileName = timestamp.strftime(settings.TIMESTAMP_FORMAT_CODE) + '_' + make.replace(
            ' ', '_') + '_' + model.replace(' ', '_') + fileExtension
        try:
            os.rename(basePath + fileName, basePath + newFileName)
        except:
            pass
