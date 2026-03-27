import json
users = [
    {"name": "Leo", "age": 25},
    {"name": "Alex", "age": 15},
    {"name": "John", "age": 20},
]

def age(users):
    return [user for user in users if user['age'] > 17]

user = age(users)
# print(user)

with open('users.json', 'r') as file:
    users = json.load(file)
    max_len_name = max(users, key=lambda x: len(x['name']))

print(max_len_name)