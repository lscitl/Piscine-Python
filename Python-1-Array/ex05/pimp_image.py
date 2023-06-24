#!/usr/bin/python3

from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_original(array) -> np.array:
    '''
    plt show original image
    '''
    plt.imshow(array)
    plt.axis("off")
    plt.title("Original")
    plt.show()
    return array


def ft_invert(array) -> np.array:
    '''
    Inverts the color of the image received and show image.
    '''
    plt.imshow(~array)
    plt.axis("off")
    plt.title("Invert")
    plt.show()
    return ~array


def ft_red(array) -> np.array:
    '''
    Filter the red color of the image received and show image.
    '''
    plt.imshow(array & np.full(array.shape, (255, 0, 0)))
    plt.axis("off")
    plt.title("Red")
    plt.show()
    return array & np.full(array.shape, (255, 0, 0))


def ft_green(array) -> np.array:
    '''
    Filter the green color of the image received and show image.
    '''
    plt.imshow(array & np.full(array.shape, (0, 255, 0)))
    plt.axis("off")
    plt.title("Green")
    plt.show()
    return array & np.full(array.shape, (0, 255, 0))


def ft_blue(array) -> np.array:
    '''
    Filter the blue color of the image received and show image.
    '''
    plt.imshow(array & np.full(array.shape, (0, 0, 255)))
    plt.axis("off")
    plt.title("Blue")
    plt.show()
    return array & np.full(array.shape, (0, 0, 255))


def ft_grey(array) -> np.array:
    '''
    Convert to grey color of the image received and show image.
    '''
    plt.imshow(np.mean(array, axis=2), cmap='gray')
    plt.axis("off")
    plt.title("Grey")
    plt.show()
    return np.mean(array, axis=2)


def main():
    """
    load landscape.jpeg to numpy array.
    convert to invert, red, green, blue, and grey image.
    """

    array = ft_load("../landscape.jpeg")
    ft_original(array)
    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)
    print(ft_invert.__doc__)


if __name__ == "__main__":
    main()
