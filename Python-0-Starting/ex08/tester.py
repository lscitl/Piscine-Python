#!/usr/bin/python3

"""
tester for ft_tqdm from Loading.py
"""


from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()

for elem in tqdm(range(333)):
    sleep(0.005)
print()

for elem in ft_tqdm(range(10)):
    sleep(1)
print()

for elem in tqdm(range(10)):
    sleep(1)
print()
