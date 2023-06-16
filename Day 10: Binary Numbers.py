#!/bin/python3
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    print(max([len(i) for i in format(int(input().strip()),"b").split("0")]))
