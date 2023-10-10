"""
Pseudocode
get user name
open file to write
store it in text file

open file to read
print the stored name
"""
DATA_FILE = "numbers.txt"
FILENAME = "name.txt"
name = input("Name: ")
out_file = open(FILENAME, 'w')
print(name, file=out_file)
out_file.close()

in_file = open(FILENAME, 'r')
text = in_file.read()
in_file.close()
print(text)
