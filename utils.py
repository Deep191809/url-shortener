import string
import random

def generate_short_id(num_chars=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=num_chars))
