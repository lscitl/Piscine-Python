#!/usr/bin/python3

import sys
from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


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
    
    p = [100, 450]
    # p = [767, 1023]
    zoom_size = [400, 400]
    
    # 400 x 400
    try:
        zoomed_img = image[p[0]:p[0] + zoom_size[0], p[1]:p[1] + zoom_size[1]]
        if zoomed_img.size == 0:
            raise AssertionError("Nothing to zoom.")
    except Exception as e:
        print("Error:", e, file=sys.stderr)
        return

    # expand dimension
    reshape_img = np.expand_dims(zoomed_img, axis=-1)

    size1 = str(reshape_img.shape)
    size2 = str(zoomed_img.shape)
    
    print("New shape after slicing:", size1, "or", size2)
    print(reshape_img)
    plt.imshow(reshape_img, 'gray')
    plt.show()
    # Image.fromarray(zoomed_img).show()
    

if __name__ == "__main__":
    main()
