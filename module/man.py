# 2 . створити класи Woman і Man відповідно, успадковані від класу Human, які мають до human додати ім'я,
# прізвище
from module.human import Human
from faker import Faker

class Man(Human):
    def __init__(self):
        super().__init__()
        fake = Faker()
        self.dict_data["first_name"] = fake.first_name_male()
        self.dict_data["last_name"] = fake.last_name_male()
    
    def make_row(self, text, key):
        if not key in ("first_name", "last_name"):
            return super().make_row(text, key)
        else:
            return ""
    
    def show_info(self):
        return f"Name: {self.dict_data['first_name']} {self.dict_data['last_name']}\n" + super().show_info()