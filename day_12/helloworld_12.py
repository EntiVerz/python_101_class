# Exercises: Level 1


# 1. Writ a function which generates a six digit/character random_user_id.
  # print(random_user_id());
  # '1ee33d'

import random
import string 

def random_user_id(i):

    random_characters = string.ascii_letters + string.digits
    user_id = ''.join(random.choice(random_characters) for num in range(i))
    print("Your random user id has been generated too", user_id)

random_user_id(6)

# 2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs 
# using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
# print(user_id_gen_by_user()) # user input: 5 5
#output:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf
   
# print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr

def user_id_gen_by_user(num1, num2):

    random_characters = string.ascii_letters + string.digits
    for i in range(1, num2+1):
        user_id_gen_by_user = ''.join(random.choice(random_characters) for i in range(num1))
        print("You random user(s) id has been generated too", user_id_gen_by_user)
user_id_gen_by_user(int(input("Please input how many characters you want in your id:")), int(input("Please input how many id's you want:")))

# 3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
# print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form

def rgb_color_gen(color_1, color_2, color_3):

    print("rgb",(color_1, color_2, color_3))

rgb_color_gen(random.randint(0,255), random.randint(0,255), random.randint(0,255))

