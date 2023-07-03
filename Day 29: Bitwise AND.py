#!/bin/python3
import math
import os
import random
import re
import sys
def bitwiseAnd(n,k):
    # Write your code here
    mx_bit = 0
    for i in range(1, n+1):
        for j in range(1, i):
            bit = i & j
            if mx_bit < bit < k:
                mx_bit = bit
                if mx_bit == k - 1:
                    return mx_bit
    return mx_bit
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        count = int(first_multiple_input[0])
        lim = int(first_multiple_input[1])
        res = bitwiseAnd(count, lim)
        fptr.write(str(res) + '\n')
    fptr.close()
