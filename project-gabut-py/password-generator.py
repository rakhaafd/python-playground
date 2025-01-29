import random
import string

def generate(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choices(characters, k=length))
    return password

user_length = int(input('masukkan mau ada berapa huruf: '))
run = generate(user_length)
print(run)