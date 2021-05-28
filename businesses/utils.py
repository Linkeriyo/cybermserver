import random
import string

def create_new_business_id():
    return "".join(random.choices(string.ascii_letters + string.digits, k=10))