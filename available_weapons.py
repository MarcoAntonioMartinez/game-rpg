from weapons_class import Weapons

# weaponName, weaponDmg, weaponType, weaponRarity
old_rusty_knife = Weapons('Old Rusty Knife', 10, 'Melee', 1)

wooden_staff = Weapons('Wooden Staff', 5, 'Magic', 1)

wooden_bow = Weapons('Wooden Bow', 10, 'Range', 1)

#these are good as placeholder but
#possibly just have a weapons list access it like weapons_list[0] and have it
# be filled from text file
# read the file add it to the list
# might have to have multiple lists for the different weapon types
# one for range, one for melee, one for magic, one for range, etc.