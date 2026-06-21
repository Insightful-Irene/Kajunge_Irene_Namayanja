# Create a list with 5 names
names = ["Alice", "Bob", "Carol", "David", "Eve"]

# Output the 2nd item (index 1)
print(names[1])  # Bob

# Change the first item
names[0] = "Anna"
print(names)

# Add a 6th item
names.append("Frank")
print(names)

# Add "Bathel" as the 3rd item (index 2)
names.insert(2, "Bathel")
print(names)

# Remove the 4th item (index 3)
names.pop(3)
print(names)

# Print the last item using negative indexing
print(names[-1])

# New list with 7 items, print 3rd, 4th, 5th (index 2 to 4)
fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
print(fruits[2:5])

# List of countries and make a copy
countries = ["Uganda", "Kenya", "Tanzania", "Rwanda", "Ethiopia"]
countries_copy = countries.copy()
print(countries_copy)

# Loop through the countries list
for country in countries:
    print(country)

# Animal names sorted ascending and descending
animals = ["zebra", "ant", "lion", "bear", "eagle"]
animals.sort()
print("Ascending:", animals)
animals.sort(reverse=True)
print("Descending:", animals)

# Print only animals with the letter 'a'
for animal in animals:
    if "a" in animal:
        print(animal)

# Join two lists
first_names = ["Alice", "Bob", "Carol"]
last_names = ["Smith", "Jones", "Brown"]
full_names = first_names + last_names
print(full_names)