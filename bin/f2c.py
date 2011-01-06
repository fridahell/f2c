#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys

def main():
	try:
		# If called without arguments, get temperature from standard input.
		if len(sys.argv) == 1:
			# Read string from standard input
			fahrenheit = float(raw_input("Enter temperature in fahrenheit: "))
		# Otherwise, make sure the program is called with exactly one argument.
		# sys.argv is the number of arguments + 1 because
		# the program's name is in sys.argv[0]
		elif len(sys.argv) == 2:
			# Set fahrenheit variable to first command line argument and convert
			fahrenheit = float(sys.argv[1])
		else:
			print "invalid args (%d), usage: %s [fahrenheit]" % (len(sys.argv), sys.argv[0])
			return 1


		# Set celsius variable to the calculated value
		# we get by converting fahrenheit into celsius using the formula
		# and round the result to two decimals
		celsius = round( (fahrenheit - 32) * 5/9, 2 )

		# Write celsius to standard output
		print celsius
		return 0
	except ValueError:
		print "input is not a valid float, usage: %s [fahrenheit]" % sys.argv[0]
		return 2
	except:
		print "unknown error, usage: %s [fahrenheit]" % sys.argv[0]
		return 3

sys.exit(main())
