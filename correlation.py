# Add the functions in this file
import json
import math
from math import sqrt

def load_journal(jsonfile):
    f = open(jsonfile)
    correlation = json.load(f)
    return correlation

def compute_phi(correlation):
    a = 'squirrel'
    b = 'carrot'
    row = 0
    n11,n00,n10,n01 = 0,0,0,0
    n1x,n0x,nx1,nx0 = 0,0,0,0
    f = open(json)
    correlation = json.load(f)
    for c in correlation:
        if a in c:
            n1x += 1
            n10 += 1
            nx0 += 1
        if b in c:
            nx1 += 1
            n01 += 1
            n0x += 1
        if a,b in c:
            n11 += 1
            n1x += 1
        else:
            n00 += 1
            nx0 += 1
            n0x += 1

        return n11,n00,n10,n01,n1x,n0x,nx1,nx0

     return row = ((n11*n00)-(n10*n01)) / sqrt(n1x*n0x*nx1*nx0)
