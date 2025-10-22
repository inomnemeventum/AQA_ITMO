# ; '''
# ; Тестовое задание: Проверить:
# ;   1. Обычный email: create_email("ivan", "test.com") → "ivan@test.com"
# ;   2. Email с цифрами: create_email("user123", "mail.ru") → "user123@mail.ru"

# ; '''
from create_email import create_email


def test_create_email_ordinary():
    assert create_email("ivan", "test.com") 

def test_create_email_numbers():
    assert create_email(("user123", "mail.ru"))