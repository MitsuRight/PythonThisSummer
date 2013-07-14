#escape characters
escape1 = "This is a back-slash character:\\"
escape2 = "I'm 6'2\" tall."
escape3 = 'I\'m 6\'2" tall.\n'

print escape1
print escape2
print escape3

#common escapes
tabby_cat = "\tI'm a tabbed in."
persian_cat = "I'm a split\non a line.\n"
backslash_cat = "I'm \\ a \\cat."

fat_cat = ''' 
I'll do a list:
\t\t* Cat food
\t\t* Fishes
\t\t* Catnip\n\t\t* Grass
''' #sometimes ''' serves as """

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "Here's a funny test:"

while True:	#indent serves as the nested feature
	for i in ["/","-","|","\\","|"]:	#":" & \\
		print "%s\r" % i,	#overlap printing!