#dictionary to list conversion
my_dict = {
    "name": "Aanchal",
    "age": 30,
    "city": "New Delhi"
}
my_list = list(my_dict.items())
print("My list:", my_list)
# Convert the list into a dictionary with keys as the elements and values as None
my_dict2 = {element: None for element in my_list}
#direct conversion
my_dict3 = dict(my_list)
print("My dictionary with new keys:", my_dict2)
print("My dictionary:", my_dict3)