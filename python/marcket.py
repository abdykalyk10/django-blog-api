def square(x):
    return x ** 2

# print(square(4))

names = "leo,alex,john"
name = names.split(',')
list_comprehension = [i.capitalize() for i in name]
# print(list_comprehension)

try:
    user = {"id": 1, "name": "Leo"}
    print(user['age'])
except KeyError:
    print("Возраст не указан")

import json

users = [
    {"id": 1, "name": "Leo"},
    {"id": 2, "name": "Alex"},
]

with open('users.json', 'w') as file:
    file.write(json.dumps(users))

with open('users.json', 'r') as file:
    line = file.read()
print(line)


words = ['Leo', 'Alex']
with open('test.txt', 'w') as file:
    file.write('\n'.join(words))

with open('test.txt', 'r') as file:
    content = file.read()
# print(content)

with open("test.txt", "r") as file:
    lines = file.readlines()  # ["Leo\n", "Alex\n"]

# убрать \n с каждой строки
lines = [line.strip() for line in lines]  # ["Leo", "Alex"]

# print(lines)



def numbers(*args):
    return [num for num in args if num % 2 ==0]

# print(numbers(1, 2, 3, 4, 5, 6))