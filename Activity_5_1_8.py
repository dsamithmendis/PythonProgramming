# Read new data point
new_temp = int(input(""))
new_humidity = int(input(""))

# Training data for RAIN and NO RAIN
rain_data = [(45,60), (55,65), (55,55)]
no_rain_data = [(35,45), (50,30), (40,35)]

# Function to compute Manhattan distance
def manhattan_distance(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

# Find the minimum distance to each class
min_rain_dist = min([manhattan_distance((new_temp,new_humidity), point) for point in rain_data])
min_no_rain_dist = min([manhattan_distance((new_temp,new_humidity), point) for point in no_rain_data])

# Assign label based on closest training example
if min_rain_dist < min_no_rain_dist:
    print("RAIN")
else:
    print("NO RAIN")
