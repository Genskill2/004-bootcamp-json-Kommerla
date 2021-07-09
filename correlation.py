# Add the functions in this file
import json
import math
from math import sqrt

def load_journal(json):
	f = open(json)
	correlation = json.load(f)
	return correlation

def compute_phi(correlation):
	a = 'squirrel'
	b = 'carrot'
	row = 0
	n11,n00,n10,n01 = 0,0,0,0
	n1_,n0_,n_1,n_0 = 0,0,0,0
	f = open(json)
	correlation = json.load(f)
	for c in correlation:
	    if a in c:
	        n1_ += 1
	        n10 += 1
	        n_0 += 1
	    elif a and b in c:
	        n11 += 1
	        n1_ += 1
	    elif b in c:
	        n_1 += 1
	        n01 += 1
	        n0_ += 1
	    else:
	        n00 += 1
	        n_0 += 1
	        n0_ += 1
	    return n11, n00, n10, n01, n1_, n0_, n_1, n_0
        row = (n11 * n00 - n10 * n01) / sqrt(n1_ * n0_ * n_1 * n_0)
	    return row

def compute_correlations(json):
	correlation = load_journal(json)
	e = {}
	for d in data:
		for event in d['event']:
			if e not in e.keys():
				e[event] = comput_phi(json)
	return e

def diagnose(json):
	e = compute_correlations(json)
	high_positive_correlate = max(e,key = e.get)
	high_negative_correlate = min(e,key = e.get)
	return high_positive_correlate,high_negative_correlate
