import settings
import shutil
from get_timestamp import getTimestamp


def createZipArchive():
    sourcePath = './' + settings.INPUT_FOLDER_NAME
    destinationPath = './' + settings.BACKUP_FOLDER_NAME + '/' + getTimestamp()
    shutil.make_archive(destinationPath, settings.ARCHIVE_FORMAT, sourcePath)
