# Concatenate an integer and a string
age = 20
name = "Alice"
print(name + " is " + str(age) + " years old")

# Remove extra spaces (beginning and end use strip, middle use split+join)
txt = "      Hello,       Uganda!       "
print(txt.strip())                        # removes leading/trailing spaces
print(" ".join(txt.split()))              # removes ALL extra spaces

# Convert to uppercase
print(txt.upper())

# Replace 'U' with 'V'
print(txt.replace("U", "V"))

# Return characters at positions 2, 3, 4 (index 1 to 4)
y = "I am proudly Ugandan"
print(y[1:4])  # " am"

# Fix the quote error using escape characters
x = "All \"Data Scientists\" are cool!"
print(x)