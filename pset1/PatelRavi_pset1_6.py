#!/usr/bin/env python

print "Enter each number separately. Floating-point numbers will be rounded to integers. Terminate by entering '.' (without quotes)"
print
while True:
	tmp = raw_input("Enter number: ")
	if tmp == '.':
		break
	try:
		res = int(float(tmp)) ## Cast as float first, incase the user input a float, then "round" it to int.
		if res % 2 == 0:
			print "{} is EVEN. {}/2 is {}".format(res, res, res/2)
		else:
			print "{} is ODD. {}*2 is {}".format(res, res, res*2)
	except ValueError:
		print "Invalid number. Try again"
		continue
