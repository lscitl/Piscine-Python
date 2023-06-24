#!/usr/bin/python3

import sys
from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def main():
    """
    load animal.jpeg to numpy array and zoom(slice) and rotate 90 degree ccw.
    """

    try:
        image = ft_load("../animal.jpeg")
    except AssertionError as e:
        print("AssertionError:", e, file=sys.stderr)
        return
    except Exception as e:
        print("Error:", e, file=sys.stderr)
        return

    def onclick(event):
        '''
        matplot loop hook event function
        '''
        try:
            # Left mouse button
            if event.button == 1:
                x, y = int(event.xdata), int(event.ydata)

                try:
                    zoomed_img = image[y - 200:y + 200, x - 200:x + 200]
                    if zoomed_img.size == 0:
                        raise AssertionError("Invalid point.")

                    reshape_img = np.expand_dims(zoomed_img, axis=-1)

                    size1 = str(reshape_img.shape)
                    size2 = str(zoomed_img.shape)

                    print("New shape after slicing:", size1, "or", size2)
                    print(reshape_img)

                    rotated_img = np.zeros(
                            (len(zoomed_img[0]), len(zoomed_img))
                        )

                    for y, line in enumerate(zoomed_img.tolist()):
                        for x, p in enumerate(line):
                            rotated_img[x][y] = zoomed_img[y][x]

                    print("New shape after Transpose:", str(rotated_img.shape))

                    plt.figure()
                    plt.imshow(rotated_img, 'gray')
                    plt.show()

                except AssertionError as e:
                    print("AssertionError: ", e, file=sys.stderr)

                except Exception as e:
                    print("Error: ", e, file=sys.stderr)

        except Exception as e:
            print("Error: ", e, file=sys.stderr)

    plt.imshow(image, 'gray')
    cid = plt.gcf().canvas.mpl_connect("button_press_event", onclick)
    plt.show()

    plt.gcf().canvas.mpl_disconnect(cid)


if __name__ == "__main__":
    main()
