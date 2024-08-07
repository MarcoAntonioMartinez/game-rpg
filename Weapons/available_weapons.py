import os

from weapons_class import Weapons

# weaponName, weaponDmg, weaponType, weaponRarity
# old_rusty_knife = Weapons('Old Rusty Knife', 10, 'Melee', 1)

#possibly just have a weapons list access it like weapons_list[0] and have it
# be filled from text file
# read the file add it to the list
# might have to have multiple lists for the different weapon types
# one for range, one for melee, one for magic, one for range, etc.

# set file size to variable
check_file = os.stat('Weapons/WeaponsData.txt').st_size

#make a list of objects with this data first make the objects
#then add them to a list
line = [] 
weapons_list = []
count = 0

# check if file is empty before using text file
if(check_file != 0):
    
    # open file, split by line and separate by comma
    with open('Weapons/WeaponsData.txt', 'r') as infile:
        
        data = infile.read().splitlines()
        data = [x.strip().split(',') for x in data]
        
        # loop through data to make weapons objects and add to list
        for i in data:
           weapons_list.append(Weapons(i[count], i[count+1], i[count+2], i[count+3]))
           
else:
    print('The file is empty')

 
