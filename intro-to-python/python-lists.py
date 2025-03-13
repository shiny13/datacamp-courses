fam = ["emma", 1.66, "Jake", 1.80]
print(type(fam))
print(fam)
print('-------------------------------------------------------')

hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50
areas = [hall, kit, liv, bed, bath]
print(areas)
print('-------------------------------------------------------')

areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom",bed, "bathroom", bath]
print(areas)
print('-------------------------------------------------------')

# practice slicing
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
print(fam)
print(fam[3:5]) # the start index is inclusive, the last index is not
print(fam[1:4])
print(fam[:4])
print(fam[2:])
print('-------------------------------------------------------')

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# Print out second element from areas
print(areas[1])
# Print out last element from areas
print(areas[-1])
# Print out the area of the living room
print(areas[5])
print('-------------------------------------------------------')

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# Use slicing to create downstairs
downstairs = areas[:6]
# Use slicing to create upstairs
upstairs = areas[6:]
# Print out downstairs and upstairs
print(downstairs)
print(upstairs)
print('-------------------------------------------------------')

# Create the areas list
house = [["hallway", 11.25], ["kitchen", 18.0], ["living room", 20.0], ["bedroom", 10.75], ["bathroom", 9.50]]
# get the last subset with the first -1, then the second element with 1
print(house[-1][1])
print('-------------------------------------------------------')

# manipulating list slices
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
print(fam)
# the slice operation can be used and new value can be assigned to the slice
fam[2:4] = ["emma", 1.65]
print(fam)
fam_ext = fam + ["me", 1.70]
print(fam_ext)
print('-------------------------------------------------------')

# list y referencing list x
x = ["a", "b", "c"]
print(x)
y = x
# changing y will change x as it has the same reference
y[1] = "z"
print(x)
print('-------------------------------------------------------')

x = ["a", "b", "c"]
y = list(x)
z = x[:]
y[1] = "w"
z[1] = "e"
print(x)
print(y)
print(z)
print('-------------------------------------------------------')

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# Correct the bathroom area
areas[-1] = 10.5
# Change "living room" to "chill zone"
areas[4] = "chill zone"

# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]
# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]
# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]

areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]
# Delete the poolhouse items from the list
del areas[10:12]
# Print the updated list
print(areas)
print('-------------------------------------------------------')

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Create areas_copy
areas_copy = list(areas)
# Change areas_copy
areas_copy[0] = 5.0
# Print areas
print(areas)
print('-------------------------------------------------------')
