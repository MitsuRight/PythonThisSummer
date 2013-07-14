#pass variables to a script
#Parameters, unpack and variables
from sys import argv
# not standard format, args names can be raplaced to any!
script, first, second, third = argv 

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third