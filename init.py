import os
import main.settings as settings


def createFolders():
    folders = [settings.INPUT_FOLDER_NAME,
               settings.BACKUP_FOLDER_NAME,
               settings.PHOTOGRAPHY_ARCHIVE_FOLDER_NAME,
               settings.VIDEO_ARCHIVE_FOLDER_NAME]
    for folder in folders:
        if not os.path.exists('./' + folder):
            os.mkdir(folder)

createFolders()