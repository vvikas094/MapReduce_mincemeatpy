#!/usr/bin/env python
import mincemeat
from sys import argv

script, filename = argv
file = open(filename, 'r')
data = list(file)
file.close()
length = len(data)
partition = length / 500
fin_list= [data[a:a+partition] for a in range(0,len(data), partition)]
datasource = dict(enumerate(fin_list))

def mapfn(k, v):
	for n in v:
		yield 'n', int(n)

def reducefn(k, vs):
	import math
	total = sum(vs)
	length=len(vs)
	sd=0
	for i in vs:
		sd+= ((int(i)-(total/length))**2)
	variance=sd/length
	res=math.sqrt(variance)
	return "  Count:   {0}\n    Sum:   {1}\nStd.dev:   {2}".format(length, total, res)

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print results['n']
