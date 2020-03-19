import math
import os
import random
import re
import sys

from pip._vendor.distlib.compat import raw_input

if __name__ == '__main__':
    n = int(raw_input().strip())
    if n % 2 == 1 or n % 2 == 0 and n >= 6 and n <= 20:
        print ("Weird")
    else:
        print ("Not Weird")
