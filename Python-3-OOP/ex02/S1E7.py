#!/usr/bin/python3

from S1E9 import Character


class Baratheon(Character):
    '''Baratheon Family class. first_name is required. is_alive is optional.'''
    def __init__(self, first_name: str, is_alive: bool = True):
        '''Baratheon Family class initialization'''
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self):
        '''Baratheon Family class __str__ method'''
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        '''Baratheon Family class __repr__ method'''
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        '''Character state turns to die(is_alive == False)'''
        self.is_alive = False


class Lannister(Character):
    '''Lannister Family class. first_name is required. is_alive is optional.'''
    def __init__(self, first_name: str, is_alive: bool = True):
        '''Lannister Family class initialization'''
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def __str__(self):
        '''Lannister Family class __str__ method'''
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        '''Lannister Family class __repr__ method'''
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        '''Character state turns to die(is_alive == False)'''
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        '''create Lannister character'''
        return cls(first_name, is_alive)


if __name__ == "__main__":
    print(Baratheon.__doc__)
    print(Lannister.__doc__)