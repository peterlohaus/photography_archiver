# Photography_Archiver

## Requirements

```
pip install difPy
pip install filetype
```

## Configuration

Parameters are defined in [settings.py](./main/settings.py).
This includes i.a. folder names and datetime format.

## Preparation

First create folder structure by running

```
python init.py
```

## Run archiver

Paste files in folder [input_files](./input_files/)
Run

```
python run.py
```

Supported files are

```
.jpg
.mp4
.nef
```
See [settings.py](./main/settings.py).
Unsupported files are ignored and left in folder [input_files](./input_files/).

## Resources

- https://www.freecodecamp.org/news/freecodecamp-python-courses-ranked-from-best-to-worst/
- https://www.freecodecamp.org/news/tag/python/
- https://www.freecodecamp.org/news/learning-python-from-zero-to-hero-120ea540b567/
- https://www.freecodecamp.org/news/python-programming-course/
- https://realpython.com/working-with-files-in-python/
- https://www.learnpython.org/en/Basic_String_Operations
- https://www.programiz.com/python-programming/variables-constants-literals
- https://stackoverflow.com/questions/123198/how-to-copy-files
- https://www.geeksforgeeks.org/how-to-create-a-duplicate-file-of-an-existing-file-using-python/
- https://docs.python.org/3/library/shutil.html
- https://www.geeksforgeeks.org/python-shutil-copy-method/
- https://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory
- https://www.freecodecamp.org/news/python-functions-define-and-call-a-function/
- https://www.freecodecamp.org/news/how-to-get-the-current-time-in-python-with-datetime/
- https://strftime.org/
- https://www.geeksforgeeks.org/python-call-function-from-another-function/
- https://towardsdatascience.com/finding-duplicate-images-with-python-71c04ec8051
- https://github.com/elisemercury/Duplicate-Image-Finder
- https://pypi.org/project/difPy/
- https://github.com/elisemercury/Duplicate-Image-Finder/wiki/difPy-Usage-Documentation
- https://note.nkmk.me/en/python-script-file-path/
- https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory
- https://stackoverflow.com/questions/52825134/convert-windowspath-to-string
- https://stackoverflow.com/questions/8858008/how-to-move-a-file-in-python
- https://www.thepythoncode.com/article/extracting-image-metadata-in-python
- https://medium.com/geekculture/extract-exif-data-from-photos-using-python-440e598274f1
- https://pillow.readthedocs.io/en/stable/installation.html
- https://exiv2.org/tags.html
- https://www.digitalocean.com/community/tutorials/python-string-to-datetime-strptime
- https://stackoverflow.com/questions/64633441/how-to-not-change-the-file-extension-while-changing-a-filename
- https://stackoverflow.com/questions/19887353/attributeerror-str-object-has-no-attribute-strftime
- https://www.geeksforgeeks.org/python-string-replace/
- https://www.freecodecamp.org/news/with-open-in-python-with-statement-syntax-example/
- https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory
- https://realpython.com/python-data-types/
- https://www.digitalocean.com/community/tutorials/python-add-to-list
- https://learnpython.com/blog/python-list-loop/
- https://pynative.com/python-rename-file/
- https://www.digitalocean.com/community/tutorials/get-file-extension-in-python
- https://stackoverflow.com/questions/31751464/how-do-i-close-an-image-opened-in-pillow
- https://pythonbasics.org/try-except/
- https://stackoverflow.com/questions/574730/python-how-to-ignore-an-exception-and-proceed
- https://stackoverflow.com/questions/4383571/importing-files-from-different-folder
- https://docs.python.org/3/library/imghdr.html
- https://stackoverflow.com/questions/889333/how-to-check-if-a-file-is-a-valid-image-file
- https://stackoverflow.com/questions/6640605/detecting-if-a-file-is-an-image-in-python
- https://stackoverflow.com/questions/266648/python-check-if-uploaded-file-is-jpg
- https://peps.python.org/pep-0594/#imghdr
- https://pypi.org/project/filetype/
- https://www.programiz.com/python-programming/if-elif-else
- https://www.thepythoncode.com/article/extract-media-metadata-in-python
- https://github.com/kkroening/ffmpeg-python
- https://stackoverflow.com/questions/71498298/is-there-a-python-library-to-extract-video-metadata-such-as-title-description
- https://stackoverflow.com/questions/11474532/how-to-change-metadata-with-ffmpeg-avconv-without-creating-a-new-file
- https://stackoverflow.com/questions/51342429/how-to-extract-metadata-of-video-files-using-python-3-7
- https://www.programcreek.com/python/example/117482/ffmpeg.probe
- https://www.programcreek.com/python/?code=kkroening%2Fffmpeg-python%2Fffmpeg-python-master%2Fffmpeg%2Ftests%2Ftest_ffmpeg.py
- https://stackoverflow.com/questions/52593420/python-convert-windows-file-path-in-a-variable
- https://github.com/kkroening/ffmpeg-python/issues/145
- https://www.btelligent.com/en/blog/best-practice-working-with-paths-in-python-part-1/
- https://www.digitalocean.com/community/tutorials/python-raw-string
- https://stackoverflow.com/questions/18707338/print-raw-string-from-variable-not-getting-the-answers
- https://stackoverflow.com/questions/66982682/ffmpeg-winerror-2-the-system-cannot-find-the-file-specified
- https://pypi.org/project/python-ffmpeg/
- https://github.com/kkroening/ffmpeg-python/issues/367
- https://www.geeksforgeeks.org/access-metadata-of-various-audio-and-video-file-formats-using-python-tinytag-library/
- https://stackoverflow.com/questions/976577/random-hash-in-python
- https://docs.python.org/3/library/uuid.html
- https://kodify.net/python/if-else/if-conditions/
- https://www.geeksforgeeks.org/check-if-element-exists-in-list-in-python/
- https://www.tutorialspoint.com/How-can-I-create-a-directory-if-it-does-not-exist-using-Python
- https://www.geeksforgeeks.org/create-a-directory-in-python/
- https://www.geeksforgeeks.org/iterate-over-a-list-in-python/