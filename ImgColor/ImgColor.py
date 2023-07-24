"""

Portfolio: MyColors
#100DaysOfCode with Python
Day: 91
Date: 2023-07-23
Author: MC

ImgColor Class
Source code:
https://levelup.gitconnected.com/reading-and-analyzing-image-file-data-and-colors-with-python-from-matrices-to-web-applications-d18010f8966f

"""

from PIL import Image
import numpy as np


class ImgColor:

    def __init__(self):
        self.image_file = None
        self.image_array = None
