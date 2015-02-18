from sys import argv

script, filename = argv

# The variable txt runs a command to open the filename passed through the parameters (In this case called filename)
txt = open(filename)

#prints the line, and concatenates the filename.
print "Here's your file %r:" % filename
#prints contents of the file
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
