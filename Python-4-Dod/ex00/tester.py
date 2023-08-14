#!/usr/bin/python3

from statistics import ft_statistics


if __name__ == "__main__":
    ft_statistics(
        1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile"
    )
    print("-----")
    ft_statistics(
        5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var"
    )
    print("-----")
    ft_statistics(
        5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem"
    )
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")
    print("-----")
    ft_statistics(6, 7, 15, 36, 39, 40, 41, 42, 43, 47, 49, a="quartile")
    ft_statistics(7, 15, 36, 39, 40, 41, a="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, "a", hello="std", world="var")
    print("-----")
    ft_statistics(5, hello="std", world="var")
