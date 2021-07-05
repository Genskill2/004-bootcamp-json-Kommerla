# Add the functions in this file
import json

def load_journal(json):
    f = open(json)
    correlation = json.load(f)
    return correlation

def compute_phi(correlation,carrot):
    row = 0
    n11,n00,n10,n01 = 0,0,0,0
    n1x,n0x,nx1,nx0 = 0,0,0,0
    f = open(json)
    correlation = json.load(f)
    for d in correlation:
        if event in d['events']:
            n1x +=1
