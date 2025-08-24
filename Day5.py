# Password Generator 

import random
import string

password=[]
allowed_symbol=["@","$","%","&","!"]

length_pass = int(input("\n[+] How many characters do you want your password to be? - "))
num_symbol = int(input("[+] How many symbols do you wish to have in your password? - "))
num_num = int(input("[+] How many numbers do you wish to have in your password? - "))

length_charac = length_pass - (num_num + num_symbol)

for i in range(0,num_num):
    password.append(str(random.randint(0,9)))

for i in range(0,num_symbol):
    password.append(str(allowed_symbol[random.randint(0,4)]))

for i in range(length_charac):
    password.append(random.choice(string.ascii_letters))

final_pass=""

random.shuffle(password)
final_pass = "".join(password)

print(f"\n>>> Your new password is - {final_pass}")