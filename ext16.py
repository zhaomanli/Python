####import argv#####
from sys import argv
####define variable####
script,filename = argv
######Print three lines to introduce the next option####
print(f'We\'re going to erase {filename}.')
print('If you don\'t want that,hit CTRL-C(^C).')
print('If you do you want that,hit RETURN.')
####make your choice if you want erase the file####
input('?')
######Open the file######
print('Opening the file...')
target = open(filename,'w')
######Erase th e file####
print('Truncating the file.Goodbye!')
target.truncate()
####You will input three lines write to the file####
print('Now I\'m going to ask you three lines.')

line1 = input('line1: ')
line2 = input('line2: ')
line3 = input('line3: ')

print('I\'m going to write these to the file.')

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')
######Close the file######
print('And finally,we close it.')
target.close()

#######Print the file to the screen#######
# target = open(filename,'w')
# txt = open(filename)
# print(f'Here\'s your new file {filename}')
# print(txt.read())
# print(txt.close())
# target.close()

