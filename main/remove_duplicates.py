from difPy import dif
from pathlib import Path
import settings


def removeDuplicates():
    # Remove duplicates new images in input folder
    dif(str(Path().absolute()) + '/' + settings.INPUT_FOLDER_NAME, None,
        'normal', 50, True, False, True, True)
    # Remove new images in inout folder, that duplicate archived images
    dif(str(Path().absolute()) + '/' + settings.PHOTOGRAPHY_ARCHIVE_FOLDER_NAME,
        str(Path().absolute()) + '/' + settings.INPUT_FOLDER_NAME,
        'normal', 50, True, False, True, True)
