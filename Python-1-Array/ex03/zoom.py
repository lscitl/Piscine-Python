#!/usr/bin/python3

import sys
from load_image import ft_load
from PIL import Image
import numpy as np


def main():
    """
    load animal.jpeg to numpy array and zoom(slice) it to 400 x 400
    """

    try:
        image: np.array = ft_load("../animal.jpeg")
    except AssertionError as e:
        print("AssertionError:", e, file=sys.stderr)
        return
    except Exception as e:
        print("Error:", e, file=sys.stderr)
        return
    
    zoomed_img = image[50:50+400][500:900]
    Image.fromarray(zoomed_img).show()
    
    return


if __name__ == "__main__":
    main()
