# first check if path is actually a file
from os import path
if path.exists('housing.data'):
    print('I have a file to process')
else:
    print('Boo')

# now, read the dataset and print line by line
with open('housing.data') as f:
    boston_data = f.read()
    for line in boston_data:
        print(line, end='')

# now, read the dataset and print line by line but as a list
with open('housing.data') as f:
    for line in f:
        print(line.split())
