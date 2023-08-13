#!/usr/bin/python3

from abc import ABC, abstractmethod


class Character(ABC):
    """Character class. abstract method: die"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Character ABC initialization."""
        self.first_name = first_name
        self.is_alive = is_alive
        # print("Character initializer called.")

    @abstractmethod
    def die(self):
        """Character die abstactmethod."""
        self.is_alive = False


class Stark(Character):
    """Stark Family class. first_name is required. is_alive is optional."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Stark Family class initialization."""
        super().__init__(first_name, is_alive)
        # print("Stark initializer called.")

    def die(self):
        """Character state turns to die(is_alive == False)"""
        super().die()


if __name__ == "__main__":
    print(Character.__doc__)
    print(Stark.__doc__)
