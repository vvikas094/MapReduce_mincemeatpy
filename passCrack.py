#!/usr/bin/env python
import mincemeat
import string
import itertools as it
import passg as passw
from sys import argv
script, hashcode = argv
data = passw.passwordgenerator()
length = len(data)
partitionLength = length /500
fin_List = [{'sets': data[i:i+partitionLength],'hashcode': hashcode} for i in range(0,len(data), partitionLength)]
datasource = dict(enumerate(fin_List))

def mapfn(k, v):
	import hashlib
	for word in v['sets']:
		hashword = hashlib.md5(word).hexdigest()[0:5]
		hashcode = v['hashcode']
		if hashword == hashcode:
			yield hashcode, word

def reducefn(k, vs):
	return vs
s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print results



