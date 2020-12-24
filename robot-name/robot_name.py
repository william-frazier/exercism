from Cryptodome.Hash import SHA256
import random

used_names = {}

class Robot:
    def __init__(self):
        self.name = gen_name()
    
    def reset(self):
        self.name = gen_name()
        
def gen_name():
    random.seed()
    first = chr(random.randint(65,90))
    second = chr(random.randint(65,90))
    num_one = str(random.randint(0,9))
    num_two = str(random.randint(0,9))
    num_three = str(random.randint(0,9))
    name = first + second + num_one + num_two + num_three
    if name not in used_names:
        used_names[name] = 1
        return name
    else:
        return gen_name()
