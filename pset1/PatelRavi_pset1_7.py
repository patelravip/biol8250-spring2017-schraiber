#!/usr/bin/env python

def first_last_product(nums):
	return nums[0]*nums[-1]

nums = []
while len(nums) < 5:
	try:
		tmp = float(raw_input("Enter number {} of 5 for list: ".format(len(numberList)+1)))
	except ValueError:
		print "Invalid number. Try again.".format(tmp)
		continue
	else:
		nums.append(tmp)

print "The product of the first number {} and last number {} is: {}".format(nums[0], nums[-1], first_last_product(nums))
