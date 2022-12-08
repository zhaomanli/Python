######### Import argv ###########
from sys import argv
########### Define the argument list ###########
script,input_file = argv
######### Define the function named print_all(f) with one parameter ########
def print_all(f):
    print(f.read())
######### Define the function named rewind(f) with one parameter, the default offset is 0 ########
def rewind(f):
    f.seek(0)
######### Define the function named print_a_line with two parameters ########
def print_a_line(line_count,f):
    print(line_count, f.readline())

########### Assign the 'current_file' parameter ###########
current_file = open(input_file)

print('First let\'s print the whole file:\n')
######## Call the 'print_all' function and the parameter is 'current_file'##########
print_all(current_file)

print('Now let\'s rewind,kind of like a tape.')
######## Call the 'rewind' function and the parameter is 'current_file'##########
rewind(current_file)

print('Let\'s print three lines:')
######## Call the 'print_a_line' function and print the first line of the 'current_file'##########
current_line = 1
print_a_line(current_line,current_file)

######## Call the 'print_a_line' function and print the first line of the 'current_file ##########
current_line = current_line + 1
print_a_line(current_line,current_file)

######## Call the 'print_a_line' function and assign parameter 'current_line' add 1 ##########
current_line = current_line + 1
print_a_line(current_line,current_file)
