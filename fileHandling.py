import os

# ####### How to Read from a File
# # Open file
# file = open('example.txt', 'r')

# # Read file
# content = file.read()

# print(content)

# # Close file
# file.close()

# ########### How to Write to a file
# file = open('createExample.txt', 'a')

# file.writelines(['\nNew Line1','\nNew Line2','\nNew Line3'])
# # file.write('This is a test.\n')

# # print(file.mode)
# file.close()

########### How to Read and Write to a file
# with open('createExample.txt', 'r+') as file:

#     file.write('This is a test5.\n')

#     # print(file.mode)
#     file.close()

# folder = open('example.txt', 'r') 
file = 'example.txt'

if os.path.exists(file):
    os.remove(file)
    print(f'{file} is removed!')
else:
    print(f'{file} exist!')