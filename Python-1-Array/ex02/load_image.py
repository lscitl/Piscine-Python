#!/usr/bin/python3

import sys
from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    """
    def ft_load(path: str)

    load image(jpg, jpeg) to numpy array
    """

    try:
        image = Image.open(path)
        data = np.asarray(image)
        print("The shape of image is:", data.shape)
        return data
    except Exception as e:
        print("Error:", e, file=sys.stderr)


if __name__ == "__main__":
    print(ft_load.__doc__)
