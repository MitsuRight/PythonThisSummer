# get data in and change it
print "How old are you?", 
age = raw_input()	#import any data from keyboard?
print "How tall are you?",#"," so next print doesn't start from a new line
height = raw_input()	  #"," would not act here!
print "How much do you weigh?",
weight = raw_input()
# %r so input 6'2" would output '6\'2"'!
print "So, you're %r years old, %rcm tall and %rKg heavy." %(
age, height, weight)  #broken line in a parenthess is alwright!

#Notice:
#D:\Programming\PythonThisSummer\src> python .\test11.py
#How old are you? \\\
#How tall are you? '"'"
#How much do you weigh?(tab key)
#So, you're '\\\\\\' years old, '\'"\'"'cm tall and '\t\t\t'Kg heavy.