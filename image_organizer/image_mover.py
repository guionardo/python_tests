import os
import piexif
from datetime import datetime
import shutil


class ImageMover:

    def __init__(self, filename):
        if not os.path.exists(filename):
            return

        self.filename = filename
        self.date = None
        self.filesize = 0
        self.imagedate = None
        self.exif = None

    def parse(self):
        if self.filename is None:
            return False
        try:
            self.date = os.path.getmtime(self.filename)
            self.filesize = os.path.getsize(self.filename)
            exif = piexif.load(self.filename)
            e0 = exif['Exif'][36867]
            self.imagedate = datetime.strptime(
                e0.decode('ascii'), '%Y:%m:%d %H:%M:%S')
            return True
        except Exception as e:
            print(e)

        return False

    def transfer(self, outputfolder, folderpattern, nomove):
        if self.filename is None or self.date is None:
            return False

        datefolder = self.imagedate.strftime(folderpattern)
        folder = os.path.join(outputfolder, datefolder)
        if not os.path.exists(folder):
            os.makedirs(folder)

        if nomove:
            shutil.copy2(self.filename, folder)
        else:
            shutil.move(self.filename, folder)

    def __str__(self):
        return f"{self.filename} ({self.filesize}) -> {self.date} : {self.imagedate}"
