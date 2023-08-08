#!/usr/bin/python3

import sys
from PIL import Image
import numpy as np
import os


def get_cur_dir() -> str:
    """def get_cur_dir() -> str:

get absolute path of current directory."""

    abs_path = os.path.abspath(__file__)
    cur_dir = os.path.dirname(abs_path)
    return cur_dir


def ft_load(path: str) -> np.ndarray:
    """def ft_load(path: str)

load image to numpy array"""

    try:
        if type(path) is not str:
            raise AssertionError("invalid input type")

        cur_dir = get_cur_dir()
        abs_path = cur_dir + '/' + path
        image = Image.open(abs_path)
        data = np.asarray(image)
        print("The shape of image is:", data.shape)
        print(data)
        # greyscale converting.
        data = np.asarray(image.convert("L"))
        return data
    except Exception as e:
        print("Error:", e, file=sys.stderr)


if __name__ == "__main__":
    print(ft_load.__doc__)
