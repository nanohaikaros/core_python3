import os
from distutils.log import warn as printf
import re

with os.popen('tasklist', 'r') as f:
    for eachLine in f:
        printf(re.split(r'\s\s+|\t', eachLine.strip()))