# Общаяя сумма 
nums = [5, 10, 3, 8]

total  =  0

for num in nums:
    total += num

    
print(total)

# максимальная число 
nums = [-4, -150, -12, -7, -3, -15, -100]

maxs =  nums[0]

for num in nums:
    if maxs < num:
        maxs = num

print(maxs)

# четные числа
nums = [1,2,3,4,5,6,7,8]

num_all = []

for num in nums:
    if num % 2 == 0:
        num_all.append(num)

print(num_all)


# сколько бокав "n"
text = "python backend"

len_sim = 0

for sim in text:
    if sim == 'n':
        len_sim += 1

print(len_sim)

# написать текст на оборот 
text = "python"

txet_all = []

for i in  range(len(text)-1, -1, -1):
    txet_all.append(text[i])

print(''.join(txet_all))


# какое каличество 7?
nums = [3, 7, 2, 7, 9, 7, 1 ,7, 7,7]

n = 0 
 
for num in nums:
    if num == 7:
        n += 1
print(n)

#  минимальное число 
nums = [5, 2, 9, 1, 7]

n = nums[0]

for num in nums: 
    if n > num:
        n = num 
        
print(n)

text = "praaogramming"
glasnye = 'aeiou'

n = 0

for i in text:
    if i in glasnye:
        n += 1

print(n)
