x = "There are %d types of people" % 10
binary = "binare"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

#seperate usage!
name1 = 'Alice'
name2 = 'Bob'
hilarious = False
approval = True
joke_evaluation = "Isn't that joke so funny? %s say %r!" #only format indicator!
print joke_evaluation %(name1, hilarious) 
print joke_evaluation %(name2, approval)

#string concatenation
w = "This is the left side of..."
e = "a string with a right side."
print w + e

#"%" doesn't hava an escape symbol. What to display depends on later '%' as an indicator!
print "When using key symbols such as '%s'" #%"hello"
