posts = [
    {"id": 1, "title": "Python"},
    {"id": 2, "title": "Django"},
    {"id": 3, "title": "Flask"}
]

likes = [
    {"post_id": 1},
    {"post_id": 1},
    {"post_id": 1},
    {"post_id": 2},
    {"post_id": 1},
    {"post_id": 3},
    {"post_id": 3},
    {"post_id": 3},
    {"post_id": 2}
]

result = {}

for like in likes:
    post_id = like['post_id']
    if post_id in result:
        result[post_id] += 1
    else:
        result[post_id] = 1

full_result = []

for post in posts:
    post_id = post['id']
    
    likes_count = result.get(post_id, 0)

    full_result.append({
        "id": post_id,
        "title": post["title"],
        "likes": likes_count
    })

# print(full_result)

list_sort = sorted(full_result, key=lambda x: x['likes'], reverse=True)
# print(list_sort[0:2])

result = full_result[0]['likes']

for post in full_result:
    likes = post['likes']
    if likes < result:
        result = likes
# print(post)
min_post = full_result[0]

for post in full_result:
    if post['likes'] < min_post['likes']:
        min_post = post

# print(min_post)

sum_likes = 0
for number in full_result:
    sum_likes += number['likes']
sum_likes /= len(full_result)
print(sum_likes)

max_likes = []
for like in full_result:
    if like['likes'] > 2:
        max_likes.append(like)

# print(max_likes)

popular = []
unpopular = []
for like in full_result:
    if like['likes'] >= sum_likes:
        popular.append(like)
    else:        
        unpopular.append(like)
    
result = {
    "popular": popular,
    "unpopular": unpopular
}   


if result['popular']:
    print(max(result['popular'], key=lambda x: x['likes']))
else:
    print("Список popular пуст")



