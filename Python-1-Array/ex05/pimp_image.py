#!/usr/bin/python3

import sys
from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_original(array) -> np.ndarray:
    '''plt show original image'''
    try:
        if len(array.shape) == 3 and array.shape[-1] == 1:
            plt.imshow(array, "gray")
        elif len(array.shape) == 3 and array.shape[-1] == 3:
            plt.imshow(array)
        else:
            raise AssertionError("Invalid array format.")

        plt.axis("off")
        plt.title("Original")
        plt.show()

        return array

    except AssertionError as e:
        print("AssertionError:", e, file=sys.stderr)

    except Exception as e:
        print("Error:", e, file=sys.stderr)


def ft_invert(array) -> np.ndarray:
    '''Inverts the color of the image received and show the image.'''
    try:
        invert_img = 255 - array
        if len(array.shape) == 3 and array.shape[-1] == 1:
            plt.imshow(invert_img, "gray")
        elif len(array.shape) == 3 and array.shape[-1] == 3:
            plt.imshow(invert_img)
        else:
            raise AssertionError("Invalid array format.")

        plt.axis("off")
        plt.title("Invert")
        plt.show()

        return invert_img

    except AssertionError as e:
        print("AssertionError:", e, file=sys.stderr)

    except Exception as e:
        print("Error:", e, file=sys.stderr)


def ft_red(array) -> np.ndarray:
    '''Filter the red color of the image received and show the image.'''
    try:
        if len(array.shape) == 3 and array.shape[-1] == 3:
            red_img = np.array([1, 0, 0]) * array
            plt.imshow(red_img)
        else:
            raise AssertionError("Invalid array format.")

        plt.axis("off")
        plt.title("Red")
        plt.show()

        return red_img

    except AssertionError as e:
        print("AssertionError:", e, file=sys.stderr)

    except Exception as e:
        print("Error:", e, file=sys.stderr)


def ft_green(array) -> np.ndarray:
    '''Filter the green color of the image received and show the image.'''
    try:
        if len(array.shape) == 3 and array.shape[-1] == 3:
            red_blue_img = array.copy()
            red_blue_img[:, :, 1] = 0
            green_img = array - red_blue_img
            plt.imshow(green_img)
        else:
            raise AssertionError("Invalid array format.")

        plt.axis("off")
        plt.title("Green")
        plt.show()

        return green_img

    except AssertionError as e:
        print("AssertionError:", e, file=sys.stderr)

    except Exception as e:
        print("Error:", e, file=sys.stderr)


def ft_blue(array) -> np.ndarray:
    '''Filter the blue color of the image received and show the image.'''
    try:
        if len(array.shape) == 3 and array.shape[-1] == 3:
            blue_img = array.copy()
            blue_img[:, :, :2] = 0
            plt.imshow(blue_img)
        else:
            raise AssertionError("Invalid array format.")

        plt.axis("off")
        plt.title("Blue")
        plt.show()

        return blue_img

    except AssertionError as e:
        print("AssertionError:", e, file=sys.stderr)

    except Exception as e:
        print("Error:", e, file=sys.stderr)


def ft_grey(array) -> np.ndarray:
    '''Convert to grey color of the image received and show the image.'''
    try:
        if len(array.shape) == 3 and array.shape[-1] == 1:
            grey_img = array.copy()
            plt.imshow(grey_img, cmap='gray')
        elif len(array.shape) == 3 and array.shape[-1] == 3:
            grey_img = np.sum(array, axis=2) / 3
            plt.imshow(grey_img, cmap='gray')
        else:
            raise AssertionError("Invalid array format.")

        plt.axis("off")
        plt.title("Grey")
        plt.show()

        return grey_img

    except AssertionError as e:
        print("AssertionError:", e, file=sys.stderr)

    except Exception as e:
        print("Error:", e, file=sys.stderr)


def main():
    """load landscape.jpeg to numpy array.
convert to invert, red, green, blue, and grey image."""

    try:
        array = ft_load("landscape.jpeg")

        # reshape if image
        if len(array.shape) == 2:
            array = array.reshape((array.shape[0], array.shape[1], 1))

        if np.issubdtype(array.dtype, np.floating):
            array = array * 255
            array = array.astype(int)

        ft_original(array)
        ft_invert(array)
        ft_red(array)
        ft_green(array)
        ft_blue(array)
        ft_grey(array)

    except AssertionError as e:
        print("AssertionError:", e, file=sys.stderr)

    except Exception as e:
        print("Error:", e, file=sys.stderr)

    print(ft_invert.__doc__)


if __name__ == "__main__":
    main()
