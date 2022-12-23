import os
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime
import settings
import filetype
import uuid


def renameFiles():
    basePath = './' + settings.INPUT_FOLDER_NAME + '/'
    fileNames = os.listdir(basePath)
    for fileName in fileNames:
        filePath = basePath + fileName
        kind = filetype.guess(filePath)
        newFileName = fileName
        if kind.extension in settings.SUPPORTED_IMAGE_EXTENSIONS:
            image = Image.open(filePath)
            exif = image.getexif()
            image.close()
            timestamp = datetime.strptime(exif.get(306), '%Y:%m:%d %H:%M:%S')
            make = exif.get(271)
            model = exif.get(272)
            newFileName = timestamp.strftime(settings.TIMESTAMP_FORMAT_CODE) + '_' + make.replace(
                ' ', '_') + '_' + model.replace(' ', '_') + '.' + kind.extension
        elif kind.extension in settings.SUPPORTED_VIDEO_EXTENSIONS:
            newFileName = uuid.uuid4().hex + '.' + kind.extension
        else:
            return
        try:
            os.rename(filePath, basePath + newFileName)
        except:
            pass
