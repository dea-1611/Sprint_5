import random
import string

class Generator:
    name = 'ekaterina'
    surname = 'demidenko'
    cohort_number = '23'
    domain = 'yandex.ru'

    @staticmethod
    def random_digits(length=3):
        return ''.join(random.choices(string.digits, k=length))

    @classmethod
    def generate_email(cls):
        generated_email = f"{cls.name}{cls.surname}{cls.cohort_number}{cls.random_digits()}@{cls.domain}"
        return generated_email

    @staticmethod
    def generate_password(length=6):
        generated_password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        return generated_password