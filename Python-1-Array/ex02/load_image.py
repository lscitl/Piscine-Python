#!/usr/bin/python3

import sys
from PIL import Image
import numpy as np
import os


def get_cur_dir() -> str:
    """Get the absolute path of the current directory.

Returns absolute path of the current directory."""

    abs_path = os.path.abspath(__file__)
    cur_dir = os.path.dirname(abs_path)
    return cur_dir


def ft_load(path: str) -> np.ndarray:
    """def ft_load(path: str)

Returns numpy array of the image."""

    try:
        if not isinstance(path, str):
            raise AssertionError("invalid input type")

        if not path:
            raise ValueError("invalid input value")

        if not os.path.isabs(path):
            path = get_cur_dir() + '/' + path

        image = Image.open(path)
        data = np.asarray(image)

        print("The shape of image is:", data.shape)
        return data

    except AssertionError as e:
        print("AssertionError:", e, file=sys.stderr)

    except ValueError as e:
        print("ValueError:", e, file=sys.stderr)

    except Exception as e:
        print("Error:", e, file=sys.stderr)


if __name__ == "__main__":
    print(ft_load.__doc__)
    print(get_cur_dir.__doc__)
