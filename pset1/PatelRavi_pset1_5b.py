#!/usr/bin/env python

nums = []
print "Enter each number separately. Terminate by entering '.' (without quotes)"
print
while True:
	tmp = raw_input("Enter number: ")
	if tmp == '.':
		break
	try:
		nums.append(float(tmp))
	except ValueError:
		print "Invalid number. Try again"
		continue

print
print "The sum of your numbers: {}".format(sum(nums))

def chunk_nums(nums):
	for i in range(0, len(nums), 2):
		yield nums[i:i+2]

for chunk in chunk_nums(nums):
	if len(chunk) == 2:
		print "{} times {} is: {}".format(chunk[0], chunk[1], chunk[0]*chunk[1])
	else:
		print "{}: A product requires at least two numbers.".format(chunk[0])
	
