import itertools as it
import string


def passwordgenerator():
	str = string.ascii_lowercase + string.digits
	partitionList = list()
	word=list()
	partitionList.append(it.product(str,repeat=1))
	partitionList.append(it.product(str,repeat=2))
	partitionList.append(it.product(str,repeat=3))
	partitionList.append(it.product(str,repeat=4))

	
	for iterator in partitionList:
		for each in iterator:
			words = ''.join(each)
			word.append(words)
	return word

