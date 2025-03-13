fam = ["emma", 1.66, "Jake", 1.80]
print(type(fam))
print(fam)

hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50
areas = [hall, kit, liv, bed, bath]
print(areas)

areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom",bed, "bathroom", bath]
print(areas)

# practice slicing
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
print(fam)
print(fam[3:5]) # the start index is inclusive, the last index is not
print(fam[1:4])
print(fam[:4])
print(fam[2:])

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# Print out second element from areas
print(areas[1])
# Print out last element from areas
print(areas[-1])
# Print out the area of the living room
print(areas[5])

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# Use slicing to create downstairs
downstairs = areas[:6]
# Use slicing to create upstairs
upstairs = areas[6:]
# Print out downstairs and upstairs
print(downstairs)
print(upstairs)
