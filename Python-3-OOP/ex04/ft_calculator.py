#!/usr/bin/python3

class calculator:
    """calculator class. Only accepts lists with int or float."""

    @classmethod
    def dotproduct(cls, V1: list[float], V2: list[float]):
        """Calculate dot product and print the result."""
        print(
            "Dot product is:",
            sum([v1 * v2 for v1, v2 in zip(V1, V2)])
        )

    @classmethod
    def add_vec(cls, V1: list[float], V2: list[float]):
        """Calculate of vector addition and print the result."""
        print(
            "Add Vector is:",
            [float(v1 + v2) for v1, v2 in zip(V1, V2)]
        )

    @classmethod
    def sous_vec(cls, V1: list[float], V2: list[float]):
        """Calculate of vector subtraction and print the result."""
        print(
            "Sous Vector is:",
            [float(v1 - v2) for v1, v2 in zip(V1, V2)]
        )


if __name__ == "__main__":
    print(calculator.__doc__)
    print(calculator.dotproduct.__doc__)
