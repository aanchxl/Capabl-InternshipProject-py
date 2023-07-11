my_list=[1, "apple", True, 3.14]
print("My list:", my_list)
print("The second element of the list is:", my_list[1])
my_list[0]=2
print("My updated list:", my_list)
my_sublist=my_list[1:3]
print("My sublist:", my_sublist)
other_list=["banana", False]
concatenated_list=my_list + other_list
print("My concatenated list:", concatenated_list)