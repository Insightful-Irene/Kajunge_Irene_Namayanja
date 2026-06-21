# Create a set of beverages using set() constructor
beverages = set(["juice", "tea", "coffee"])
print(beverages)

# Add 2 more items using update()
beverages.update(["water", "milk"])
print(beverages)

# Check if "microwave" is in the set
mySet = {"oven", "kettle", "microwave", "refrigerator"}
print("microwave" in mySet)  # True

# Remove "kettle"
mySet.remove("kettle")
print(mySet)

# Loop through the set
for item in mySet:
    print(item)

# Add elements from a list into a set
my_set = {"apple", "banana", "cherry", "date"}
my_list = ["mango", "grape"]
my_set.update(my_list)
print(my_set)

# Join two sets
ages = {20, 21, 22}
first_names = {"Alice", "Bob"}
joined = ages.union(first_names)
print(joined)