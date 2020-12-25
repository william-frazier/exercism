import re

class PhoneNumber:
    def __init__(self, number):
        number = re.sub("[^0-9]", "", number)
        if len(number) < 10:
            raise ValueError("This number is too short.")
        if len(number) >= 11 and number[0] != '1':
            raise ValueError("This number is too long.")
        if len(number) == 11:
            number = number[1:]
        if number[0] == '0' or number[0] == '1':
            raise ValueError("Invalid area code.")
        if number[3] == '0' or number[3] == '1':
            raise ValueError("Invalid exchange number.")
        self.number = number
        self.area_code = number[:3]
        
    def pretty(self):
        return f'({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}'
        

