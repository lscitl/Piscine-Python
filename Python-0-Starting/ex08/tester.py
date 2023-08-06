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

for i, elem in enumerate(ft_tqdm(range(10))):
    sleep(.08) if i % 2 == 0 else sleep(.17)
print()

for i, elem in enumerate(tqdm(range(10))):
    sleep(.08) if i % 2 == 0 else sleep(.17)
print()
