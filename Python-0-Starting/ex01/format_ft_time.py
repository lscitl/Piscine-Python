#!/usr/bin/python3

import time
from datetime import date

d = date.today()
t = time.time()  # seconds from 1970 Jan 1

print(
    "Seconds since January 1, 1970: "
    + "{:,}".format(t)
    + " or "
    + "{:.2e}".format(t)
    + " in scientific notation"
)
print(d.strftime("%B %d %Y"))
