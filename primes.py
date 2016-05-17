#!/usr/bin/env python
import mincemeat
numlist=list()
for i in range(2,10000001):
	numlist.append(i)

data= numlist
length = len(data)
chunkLength = length / 10000
Lists = [data[i:i+chunkLength] for i in range(0,len(data), chunkLength)]
datasource = dict(enumerate(Lists))

def mapfn(k,v):
	for i in v:
		numStrings = str(i)
		if numStrings == numStrings[::-1]:
			yield 'num', numStrings

def reducefn(k, v):
	def isPrime(num):
		import math
		if(num<=3):
			return True
		elif num%2==0:
			return False
		elif num%3==0:
			return False
		elif((num-1)%6!=0) or ((num-5)%6!=0):
			for i in range(5,int(math.ceil(math.sqrt(num)))+1,2):
				if(num%i==0):
					break
			else:
				return True
	output=list()
	for i in v: 
		number= int(i)
		if(isPrime(number)):
			output.append(number)
			

	outputSum = sum(output)
	return 'output: {0}\nlength: {1}\n   sum: {2}'.format(output, len(output), outputSum)

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results=s.run_server(password="changeme")
print results['num']
