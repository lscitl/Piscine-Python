#!/usr/bin/python3

from abc import ABC, abstractmethod


class Character(ABC):
    """Character class. abstract method: die"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def die(self):
        """Character die abstactmethod."""
        pass


class Stark(Character):
    """Stark Family class. first_name is required. is_alive is optional."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Stark Family class initialization."""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Character state turns to die(is_alive == False)"""
        self.is_alive = False


if __name__ == "__main__":
    print(Character.__doc__)
    print(Stark.__doc__)
