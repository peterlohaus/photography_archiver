import shutil
import os
import settings
import filetype


def moveFilesToArchive():
    basePath = './input_files/'
    fileNames = os.listdir(basePath)
    destination = ''
    for fileName in fileNames:
        kind = filetype.guess(basePath + fileName)
        if kind.extension in settings.SUPPORTED_IMAGE_EXTENSIONS:
            destination = settings.PHOTOGRAPHY_ARCHIVE_FOLDER_NAME
        elif kind.extension in settings.SUPPORTED_VIDEO_EXTENSIONS:
            destination = settings.VIDEO_ARCHIVE_FOLDER_NAME

        if destination:
            shutil.move('./' + settings.INPUT_FOLDER_NAME + '/' + fileName,
                        './' + destination + '/' + fileName)
