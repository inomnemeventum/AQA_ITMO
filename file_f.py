# def is_even(num: int) -> bool: 
#     return num % 2 ==0

# def greeting(name):
#     print(f"Hi,{name}")
    
'''
    Faker — библиотека для генерации фейковых данных в Python. Позволяет создавать реалистичные данные для различных целей, например: 
tutorialspoint.com
dev.to
habr.com
Тестирование программного обеспечения — Faker используется для тестирования smoke и заполнения баз данных поддельными данными, чтобы тестировать различные сценарии.
Веб-разработка — библиотека помогает создавать базу данных с профилями пользователей, комментариями и публикациями, что помогает визуализировать, как приложение ведёт себя в реальных сценариях.
Наука о данных — Faker генерирует выборочные наборы данных, помогающие обучать и тестировать модели, если реальные наборы данных недоступны или ограничены.
    Библиотека Faker не является стандартной библиотекой Python,
    её нужно установить с помощью pip. Команда: pip install Faker. 
    
    from faker import Faker  
fake = Faker()  
print(fake.name())  # Генерирует случайное имя  
print(fake.address())  # Генерирует случайный адрес  
print(fake.email())  # Генерирует случайный адрес электронной почты  
``` [3](https://dev.to/ankitmalikg/python-generate-fake-data-with-faker-1ecj)  
    '''
    
from faker import Faker
    
    # import random 
    
    # dice = random.randit(1, 6}
    
    # worlds = ["Hi","python"]
    
    # print(dice)
    
    # print(random.choice(worlds))
    
fake = Faker()
# fake_name = fake.name()
# print(fake_name)


for _ in range(11):
    print(fake.phone_number())
    
    
    
# pip list вывод списка библиотек
# pip freeze > requirements    создание файла с библиотеками