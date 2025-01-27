#!/usr/bin/python3

import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """return random generated id"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Student dataclass. id should not given."""
    name: str = field()
    surname: str = field()
    active: bool = field(default=True)
    login: str | None = field(default=None)
    id: str | None = field(default=None)

    def __post_init__(self):
        if (
            not isinstance(self.name, str) or
            not isinstance(self.surname, str) or
            not isinstance(self.active, bool)
        ):
            raise TypeError("Please check input type.")

        if self.login is not None:
            m = "Student.__init__() got an unexpected keyword argument 'login'"
            raise TypeError(m)

        if self.id is not None:
            m = "Student.__init__() got an unexpected keyword argument 'id'"
            raise TypeError(m)

        if not (self.name and self.surname):
            raise ValueError("Please check input value.")

        self.login = self.name[0] + self.surname
        self.id = generate_id()


if __name__ == "__main__":
    print(generate_id.__doc__)
    print(Student.__doc__)
