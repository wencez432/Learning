friends = ["Kevin", "Karen", "Jim", 3.5, False, "Oscar", "Oscar", "Oscar", "Toby"]

print(type(friends))
print(friends)
friends[3] = "Mike"
print(friends[0]) # Kevin
print(friends[1:]) # Karen, ...
print(friends[1:5]) # Karen, ... , False

# List functions

lucky_numbers = [4, 17, -3, 8, 15, 16, 23, 42]
friends.extend(lucky_numbers)
print(friends)
friends.append("Creed")
print(friends)
friends.insert(1, "Kelly")
print(friends)
friends.remove("Jim")
print(friends)
friends.pop()
print(friends)
print(friends.index("Mike"))
print(friends.count("Oscar")) # 3
lucky_numbers.sort()  # sort "lucky_numbers" in ascending order
print(lucky_numbers)
friends.reverse()
print(friends)
friends2 = friends.copy() # creates a copy, any changes made are independent
friends3 = friends # copy a variable, any changes made are dependent
print(friends2)
friends3.clear()
print(friends)
print(friends2)
print(friends3)