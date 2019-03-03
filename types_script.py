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
records = records.rename(columns = {'BRITH_YEAR': 'Birth_Year'})
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

#Working with sets
boy_set = set(records.loc[(records['GENDER'] == "MALE")]['NAME'].tolist())
girl_set = set(records.loc[(records['GENDER'] == "FEMALE")]['NAME'].tolist())

#find intersection
bg_intersect = boy_set.intersection(girl_set)

#Looking at how names have changed between 2011-2014
two11_two14 = records.loc[(records['Birth_Year'] == 2011) | (records['Birth_Year'] == 2014)].values.tolist()

baby_2011 = set()
baby_2014 = set()

for row in two11_two14:
    if row[0] == 2011:
        baby_2011.add(row[3])
    else:
        baby_2014.add(row[3])

len(baby_2011.difference(baby_2014))
#Dictionaries
##Unpacking a set into a dictionary
names = {}
for rank, name in enumerate(baby_2011):
    names[rank] = name

#Note the need to convert names in a list via the sorted call before being able to slice
for rank in sorted(names, reverse = True)[:10]:
    print(names[rank])

#Nuilding a nested dict
x = []
for i in zip(records['Birth_Year'], range(len(records)), records['NAME']):
    x.append(list(i))

y = {x[0][0]: {x[0][1]: x[0][2]}}
