x = ("samsung", "iphone", "tecno", "redmi")

# Print favorite phone brand (index 0 = samsung)
print(x[0])

# 2nd last item using negative indexing
print(x[-2])  # tecno

# Update "iphone" to "itel" — convert to list, change, convert back
x_list = list(x)
x_list[1] = "itel"
x = tuple(x_list)
print(x)

# Add "Huawei" to the tuple
x = x + ("Huawei",)
print(x)

# Loop through the tuple
for phone in x:
    print(phone)

# Remove the first item
x_list = list(x)
x_list.pop(0)
x = tuple(x_list)
print(x)

# Create a tuple of Uganda cities using tuple() constructor
cities = tuple(["Kampala", "Gulu", "Mbarara", "Jinja", "Entebbe"])
print(cities)

# Unpack the tuple
city1, city2, city3, city4, city5 = cities
print(city1, city2, city3, city4, city5)

# Print 2nd, 3rd, 4th cities (index 1 to 3)
print(cities[1:4])

# Join two tuples
first_names = ("Alice", "Bob")
last_names = ("Smith", "Jones")
full_names = first_names + last_names
print(full_names)

# Multiply a tuple of colors by 3
colors = ("red", "blue", "green")
print(colors * 3)

# Count how many times 8 appears
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(thistuple.count(8))  