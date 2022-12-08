# ######import argv#########
# from sys import argv
# ######### Import exists###########
# from os.path import exists
# ####### ###########
# script,from_file,to_file = argv 
# print(f'Copying from {from_file} to {to_file}')

# #we could do these two on line,how?
# in_file = open(from_file)
# indata = in_file.read()

# print(f'The input file is {len(indata)} bytes long')


# print(f'Does the output file exists?{exists(to_file)}')
# print('Ready,hit RETURN to continue,CRTL-C to abort.')
# input()

# out_file = open(to_file,'w')
# out_file.write(indata)

# print('Alright,all done.')

# out_file.close()
# in_file.close()


# ##########Another methods#########
# file1 = open('ext16_sample.txt','r')
# file2 = open('ext17_sample.txt','w')
# s = file1.read()
# w = file2.write(s)
# file1.close()
# file2.close()


# ##########Another methods#########
import os
os.system('copy ext16_sample.txt ext17_sample.txt')
