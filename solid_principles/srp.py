# Single Responsibility Principle

# Problem : A class handling multiple responsibilities.

from pathlib import Path

class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        """ Method to read the file """

    def write(self, data, encoding="utf-8"):
        """ Method to write the file """

    def compress(self):
        """ Method to compress the file """

    def decompress(self):
        """ Method to de-compress the file """


# Solution: Split into multiple classes, each with a single responsibility.

# Solution: Split into multiple classes, each with a single responsibility.

from pathlib import Path


class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        """ Method to read the file """

    def write(self, data, encoding="utf-8"):
        """ Method to write the file """





class ZipFileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def compress(self):
        """ Method to compress the file """
        self.func1()

    def decompress(self):
        """ Method to de-compress the file """
        self.func2()

    def func1(self):
        """" this does something specific to ZIP compressions"""

    def func2(self):
        """" this does something specific to ZIP decompressions"""


class RARFileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def compress(self):
        """ Method to compress the file """
        self.func1()

    def decompress(self):
        """ Method to de-compress the file """
        self.func2()

    def func1(self):
        """" this does something specific to RAR compressions"""

    def func2(self):
        """" this does something specific to RAR decompressions"""


if file.type == "Zip":
    zip = ZipFileManager()
