class Post:
    def __init__ (self, title, likes):
        self.title = title
        self.likes = likes

    def describe(self):
        return f'Пост:{self.title}, лайков: {self.likes}'

post1 = Post('Python', 15)
print(post1.describe())


class User:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f'{self.name} , {self.age} лет'

class Admin(User):
    def ban(self):
        return f'{self.name} заблокирован'

user1 = User("Leo", 25)
admin1 = Admin("Alex", 30)

print(user1.info())   # что выведет?
print(admin1.info())  # что выведет?
print(admin1.ban())   # что выведет?


def timer(func):
    def wrappa(*args, **kwargs): # этого я не понял что нужно добавить *args, **kwargs посказал ии 
        print("Функция начала работу")
        result = func(*args, **kwargs) # этого я не понял что нужно добавить *args, **kwargs посказал ии 
        print("Функция закончила работу")
        return result
    return wrappa

@timer
def calculate(n):
    return n * 2

number = calculate(10)
print(number)


def squares(n):
    for i in range(1, n+1):
        yield i ** 2  # квадрат числа — ты это уже знаешь!

for num in squares(5):
    print(num)  # 1, 4, 9, 16, 25


    