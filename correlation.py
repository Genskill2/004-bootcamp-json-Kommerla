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
	n1_,n0_,n_1,n_0 = 0,0,0,0
	f = open(json)
	correlation = json.load(f)
	for c in correlation:
		if a in c:
			n1_ += 1
			n10 += 1
			n_0 += 1
			if b in c:
				n11 += 1
				n1_ += 1
		if b in c:
			n_1 += 1
			n01 += 1
			n0_ += 1
		else:
			n00 += 1
			n_0 += 1
			n0_ += 1

		return n11,n00,n10,n01,n1_,n0_,n_1,n_0
	 row = (n11*n00 - n10*n01)/sqrt(n1_ * n0_ * n_1 * n_0)
	 return row
