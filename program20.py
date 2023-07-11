# Create a dictionary with nested keys to represent a 2D matrix
my_dict = {
    "row1": {
        "col1": 1,
        "col2": 2,
        "col3": 3
    },
    "row2": {
        "col1": 4,
        "col2": 5,
        "col3": 6
    },
    "row3": {
        "col1": 7,
        "col2": 8,
        "col3": 9
    }
}

# Print the dictionary
print("My dictionary:", my_dict)

# Access a value using nested keys
print("The value at row1, col2 is:", my_dict["row1"]["col2"])

# Change a value using nested keys
my_dict["row2"]["col3"] = 10
print("My updated dictionary:", my_dict)

# Add a new row to the dictionary
my_dict["row4"] = {
    "col1": 11,
    "col2": 12,
    "col3": 13
}
print("My dictionary with a new row:", my_dict)