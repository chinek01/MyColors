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


def rgb_to_hex(r,
               g,
               b):

    if r is None:
        raise ValueError("The r value must be set!")

    if g is None:
        raise ValueError("The g value must be set!")

    if b is None:
        raise ValueError("The b value must be set!")

    ans = "{:X}{:X}{:X}".format(r, g, b)

    while len(ans) < 6:
        ans = "0" + ans

    return "#" + ans


def hex_to_rgb(h):

    if h is None:
        raise ValueError("The hex_list value must be set!")

    rgb = []

    for i in (0, 2, 4):
        decimal = int(h[i:i + 2], 16)
        rgb.append(decimal)

    return tuple(rgb)


def get_top_10(hex_list):
    hex_frequency = {}

    for item in hex_list:
        if item in hex_frequency:
            hex_frequency[item] += 1
        else:
            hex_frequency[item] = 1

    sorted_hex = dict(sorted(hex_frequency.items(), key=lambda element: element[1]))

    return list(sorted_hex.keys())[-10:][::-1]


class ImgColor:

    def __init__(self):
        self.image_file = None
        self.image_array = None
        self._shape = None
        self._hex_list = []
        self._top_10_hex_list = []
        self._hex_frequency = {}
        self._hex_frequency_top_10 = {}
        self._hex_frequency_top_10_fit = {}

    def open_img_file(self,
                      path):

        if path is None:
            raise ValueError("The path value must be set!")

        if not isinstance(path, str):
            raise TypeError("The path value must be str type!")

        self.image_file = Image.open(path)
        self.image_array = np.array(self.image_file)

        self._shape = self.image_array.shape

        x = self._shape[0]
        y = self._shape[1]

        for x in range(x):
            for y in range(y):
                rgb = self.image_array[x, y, :]

                r = rgb[0]
                g = rgb[1]
                b = rgb[2]

                self._hex_list.append(rgb_to_hex(r, g, b))

        self._top_10_hex_list = get_top_10(self._hex_list)

        return self._top_10_hex_list

    def color_percent_top_10(self):
        """
        calculate color percent in image for top 10 values
        :return:
        """

        self.color_percent_all()

        for item in self._top_10_hex_list:
            self._hex_frequency_top_10[item] = self._hex_frequency[item]

        return self._hex_frequency_top_10

    def color_percent_top_10_fit(self):
        """
        fit data
        :return:
        """

        self.color_percent_top_10()

        for key, value in self._hex_frequency_top_10.items():
            c, p = value
            self._hex_frequency_top_10_fit[key] = p

        return self._hex_frequency_top_10_fit

    def color_percent_all(self):
        """
        calculate color percent in image for all values
        :return:
        """

        if len(self._hex_list) <= 0:
            raise ValueError("The Hex list is empty!")

        my_len = len(self._hex_list)

        hex_frequency = {}

        for item in self._hex_list:
            if item in hex_frequency:
                hex_frequency[item] += 1
            else:
                hex_frequency[item] = 1

        self._hex_frequency = {key: [value, round((value * 100) / my_len, 5)] for key, value in hex_frequency.items()}

        return self._hex_frequency


# some tests
if __name__ == '__main__':
    x = ImgColor()
    print(x.open_img_file('example_img.jpg'))
    x.open_img_file('example_img.jpg')
    # x.color_percent_all()
    print(x.color_percent_top_10())
    print(x.color_percent_top_10_fit())
