import shutil
import os
import settings


def moveFilesToArchive():
    basePath = './input_files/'
    fileNames = os.listdir(basePath)
    for fileName in fileNames:
        shutil.move('./' + settings.INPUT_FOLDER_NAME + '/' + fileName,
                    './' + settings.ARCHIVE_FOLDER_NAME + '/' + fileName)
