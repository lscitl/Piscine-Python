from setuptools import setup, find_packages

"""
setup.py will create package
"""

import toml


def main():
    # Load the data from the TOML file
    data = toml.load("config.toml")

    # Access the values from the data
    name: str = data["name"]
    version: str = data["version"]
    description: str = data["description"]
    url: str = data["url"]
    author: str = data["author"]
    author_email: str = data["author_email"]
    license: str = data["license"]

    setup(
        name=name,
        version=version,
        description=description,
        url=url,
        author=author,
        author_email=author_email,
        license=license,
        packages=find_packages(),
    )


if __name__ == "__main__":
    main()
