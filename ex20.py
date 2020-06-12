# Functions and Files

from sys import argv

script, input_file = argv


def print_all(f):
    print f.read()


def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print line_count, f.readline()


current_file = open(input_file)

print "First, let's print the whole file:\n"

print_all(current_file)

# print "Is the file Closed? %s " % current_file.closed # also doesn't work. maybe need to use `with` keyword
print "Let's print three lines:"

current_file = open(input_file)  # Need to re-open because python automatically closes file after f.read()
# print "Readable? ", current_file.readable  # Doesn't seem to work

# Loop da thing
current_line = 1
while current_line <= 3:
    print_a_line(current_line, current_file)
    current_line += 1

current_file.close()
