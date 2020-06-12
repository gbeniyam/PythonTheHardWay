# Names, variables, Code, Functions

# like argv script


def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)


# ^ pointless to do it that way, alternative:
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)


# this takes one argument
def print_one(arg1):
    print "arg1 : %r" % arg1


# this one takes no arguments
def print_none():
    print "I got nothin'."


print_two("One1", "Two2")
print_two_again("One11", "Two22")
print_one("First!")
print_none()
