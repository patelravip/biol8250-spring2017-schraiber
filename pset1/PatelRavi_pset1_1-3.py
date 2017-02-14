#!/usr/bin/env python

from __future__ import division	


while True:
	try:
		userNumber = float(raw_input("Enter a number: ")) ## Cast as float to ensure that it is a number, and for complex operations. Overkill, generally since it takes more memory, but quick-and-easy fix for ensuring numerical values. Also allows for non-integer inputs
	except ValueError:
		print "Invalid number. Try again."
		continue
	else:
		break

print "Twice {}: {}".format(userNumber, userNumber*2)
print "Half {}: {}".format(userNumber, userNumber/2)
print "{} plus 50: {}".format(userNumber, userNumber+50)
print "{} minus 50: {}".format(userNumber, userNumber-50)
print

numberList = []
while len(numberList) < 4:
	try:
		tmp = float(raw_input("Enter number {} of 4 for list: ".format(len(numberList)+1)))
	except ValueError:
		print "Invalid number. Try again.".format(tmp)
		continue
	else:
		numberList.append(tmp)

productList = [numberList[0]*numberList[1], numberList[2]*numberList[3]]
print numberList
print productList
print

friends = {} 
while len(friends) < 3:
	fName = raw_input("Enter friend's name: ")
	try:
		fAge = float(raw_input("How old is {}? ".format(fName)))
	except ValueError:
		print "Inavlid age. Try again.".format(fAge)
		continue
	else:
		friends[fName] = fAge

for f in friends:
	print "{fName} is {fAge} years old. In 5 years, {fName} will be {fAgeAddFive}".format(fName=f, fAge=friends[f], fAgeAddFive=friends[f]+5)
print

