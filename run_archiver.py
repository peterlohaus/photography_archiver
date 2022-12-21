import sys

sys.path.insert(1, './main')

from main.rename_files import renameFiles
from main.move_files_to_archive import moveFilesToArchive
from main.remove_duplicates import removeDuplicates
from main.create_zip_archive import createZipArchive

# Backup input data before processing
createZipArchive()

# Remove images that are duplicates in input folder and archive folder
removeDuplicates()

# Rename input files on basis of exif data
renameFiles()

# Move files from input folder to archive folder
moveFilesToArchive()
