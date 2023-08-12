#!/usr/bin/python3

from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King class. first_name is required. is_alive is optional."""
    def __init__(self, first_name: str, is_alive: bool = True):
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def set_eyes(self, color: str):
        """set eyes color"""
        self.eyes = color

    def set_hairs(self, color: str):
        """set hairs color"""
        self.hairs = color

    def get_eyes(self):
        """return eyes color"""
        return self.eyes

    def get_hairs(self):
        """return hairs color"""
        return self.hairs

    def die(self):
        """Character state turns to die(is_alive == False)"""
        self.is_alive = False


if __name__ == '__main__':
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)
