name = "Gavriel"
age = 29
height = 68
weight = 130
eyes = "brown"
teeth = "white"
hair = "dark brown"

print "Let's talk about %s" % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d, I get %d." % (age, height, weight, age + height + weight)
print "eye color using %%r: %r" % eyes

print "%%r uses repr(object)"
print """\nrepr(object)
goal of repr is to be unambiguous, such as show the data type (can be used for debugging). Str is meant to be readable.
https://www.youtube.com/watch?v=5cvM-crlDvg\n"""
