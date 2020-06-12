# opening files!
from sys import argv
import time

named_tuple = time.localtime()  # get struct_time
local_time = time.strftime("%m/%d/%Y, %I:%M:%S %p")
print local_time

script, filename = argv
s = "Added text from ex15.py\n"

txt = open(filename, "a+")  # append+read/update access modifier

print "Here's your file %r: " % filename
print txt.read()

txt.close()  # close to re-open again with append+read/update permission

txt = open(filename, "a+")
#  debug printing
# f_text = "%s: %s" % (local_time, s)
# print "%s: %s" % (local_time, s)
txt.write("%s: %s" % (local_time, s))

txt.close()  # close to re-open again with read+update permission instead of write+update

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)  # read attribute mode is default/assumed if no 2nd parameter given

print txt_again.read()
txt.close()
