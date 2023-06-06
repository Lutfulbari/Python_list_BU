countries = ["Bangladesh","India","USA","China", "Germany","Norway"]


# # using del statement 

# print(countries)

# del countries[1]
# #['Bangladesh', 'USA', 'China', 'Germany', 'Norway']
# del countries[3]
# del countries[-1]
# print(countries)

# print(countries)

# using pop method 

fruits = ["Banana", "Mango" ,"Apple","orange"]

print(fruits)
removed_item = fruits.pop()
print(removed_item)
print(fruits)
another_removed_item = fruits.pop(0)

# using removed method

vowels = ['a','e','i','o','u','i']
vowels.remove('i')
# vowels.remove('z')
print(vowels)