# 1. створити Клас Human, який створює dict human і задає йому адресу, телефон, професію та випадкову ЗП
from faker import Faker
from random import randint

class Human():
    def __init__(self):
        fake = Faker()
        self.dict_data = {}
        self.dict_data["address"] = fake.address()
        self.dict_data["phone_number"] = fake.phone_number()
        self.dict_data["job"] = fake.job()
        self.dict_data["salary"] = randint(1000, 5000)
        
    def make_row(self, text, key):
        try:
            return f"{text}: {self.dict_data[key]}\n"
        except KeyError:
            return f"{text}: unknown"
        
    def show_info(self):
        info = ""
        for key in self.dict_data.keys():
            info += self.make_row(key.capitalize(), key)
        return info