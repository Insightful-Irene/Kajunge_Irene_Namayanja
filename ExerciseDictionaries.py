Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

# Print the shoe size
print(Shoes["size"])  # 40

# Change "Nick" to "Adidas"
Shoes["brand"] = "Adidas"
print(Shoes)

# Add a new key/value pair
Shoes["type"] = "sneakers"
print(Shoes)

# Return all keys
print(list(Shoes.keys()))

# Return all values
print(list(Shoes.values()))

# Check if "size" key exists
print("size" in Shoes)  # True

# Loop through the dictionary
for key, value in Shoes.items():
    print(key, ":", value)

# Remove "color"
Shoes.pop("color")
print(Shoes)

# Empty the dictionary
Shoes.clear()
print(Shoes)  # {}

# Copy a dictionary
my_dict = {"name": "Bob", "age": 25}
my_dict_copy = my_dict.copy()
print(my_dict_copy)

# Nested dictionary
students = {
    "student1": {"name": "Alice", "age": 20},
    "student2": {"name": "Bob",   "age": 22}
}
print(students)
print(students["student1"]["name"])  # Alice