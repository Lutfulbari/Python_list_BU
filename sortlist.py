numbers = [4,5,1,2,10,100]
#[1,2,3,4,5,6,7,8,9,100]
fruits = ["banana","mango","orange","apple"]
#sort
numbers.sort()
fruits.sort()



print(numbers)
print(fruits)
print()

numbers.sort(reverse=True)
fruits.sort(reverse=True)
print(numbers)
print(fruits)

# sorted()

another_numbers = [4,3,5,10,100]
sorted_numbers = sorted(another_numbers)

sorted_numbers_des = sorted(another_numbers, reverse=True)


print(another_numbers)
print(sorted_numbers)
print(sorted_numbers_des)
