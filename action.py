import os
import random
import string

def stop():                                                     #actions
    os.system('clear')
    print("See you soon!")
    
def get_captcha():                                              #actions
    pool = string.ascii_lowercase + string.digits
    random_chars = random.choices(pool, k=4)
    return "".join(random_chars)