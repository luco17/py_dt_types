import pandas as pd, numpy as np, matplotlib.pyplot as plt

#Containers hold types of data, they can be mutable (list, set) or immutable (tuple)
##Lists
#Mutable, indexed and can be combined

#Basic list ops
baby_names = ['Ximena', 'Aliza', 'Ayden', 'Calvin']

#Extending
baby_names.extend(['Rowen', 'Sandeep'])
print(baby_names)

#Using index positioning
position = baby_names.index('Aliza')

# Remove itmes from a list
baby_names.pop(position)
print(baby_names)

#Reading in records and running them in a loop
records = pd.read_csv('baby_names.csv')
records_list = records.values.tolist()
# Create an empty list: baby_names
baby_names = []
# Loop over records
for row in records_list:
    # Add the name to the list
    baby_names.append(row[3])
# Sort the names in alphabetical order
for name in sorted(baby_names):
    print(name)

##Tuples
#Ordered, indexable, but immutable and more memory efficient
#Tuples are unpackable, meaning you can expand them into names variables that represent the elements.
girl_names = records.loc[(records['GENDER'] == "FEMALE")]['NAME'].tolist()
boy_names = records.loc[(records['GENDER'] == "MALE")]['NAME'].tolist()

# Zipping and unpacking
pairs = zip(girl_names, boy_names)

# Iterate over pairs
for idx, pair in enumerate(pairs):
    # Unpack pair: girl_name, boy_name
    girl_name, boy_name = pair
    # Print the rank and names associated with each rank
    print('Rank {}: {} and {}'.format(idx, girl_name, boy_name))

    
