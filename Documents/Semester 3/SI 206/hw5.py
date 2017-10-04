import operator
import re

inp = open("regex_sum_35647.txt" , 'r')
stringline = []

for line in inp:
	newline = re.findall('[0-9]+' , line)
	if len(newline) != 0 :
		stringline = stringline + newline

for i in range(len(stringline)):
	stringline[i] = int(stringline[i])

print(sum(stringline))



