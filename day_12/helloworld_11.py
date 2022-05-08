# Exercises: Level 1


# 1. Writ a function which generates a six digit/character random_user_id.
  # print(random_user_id());
  # '1ee33d'

from email import header
from math import factorial
from os import lseek
import random
import string
from traceback import print_tb 

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

# Exercises: Level 2


# 1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. 
# Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

def list_of_hexa_colors(num1,num2):

    for i in range(1, num2+1):

        hexadecimal_colors = "#"+''.join([random.choice('0123456789ABCDEF') for i in range(num1)])
        print("these are your hexadecimal colors", hexadecimal_colors)

list_of_hexa_colors(6, int(input("Please input how many hexadecimal numbers you want:")))

# 2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

def list_of_rgb_colors():

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_color = (r, g, b)
    print(rgb_color)
    
list_of_rgb_colors()


# 3. Write a function generate_colors which can generate any number of hexa or rgb colors.
   #generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
   #generate_colors('hexa', 1) # ['#b334ef']
   #generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
   #generate_colors('rgb', 1)  # ['rgb(33,79, 176)']

def generate_colors(choice, num2):

    while True:
        if choice == 'hexa':

            hexadecimal_colors_2 = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]) for i in range(num2)]
            print("Your hexa colors are", hexadecimal_colors_2)
            break

        elif choice == 'rgb':

            random.randint(0, 255) 
            random.randint(0, 255)
            random.randint(0, 255)
            rgb_color_2 = ["rgb"+''.join(str((random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))) for i in range(num2))]
            print("Your rgb colors are", rgb_color_2)
            break

        else: print("Please enter valid color choices hexa or rgb")
        generate_colors(str(input("Please choose between color choices hexa or rgb:")), int(input("Please enter the number of colors you want:")))
        break
    False
        
generate_colors(str(input("Please choose between color choices hexa or rgb:")), int(input("Please enter the number of colors you want:")))

# Exercises: Level 3


# 1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

def shuffle_list(list):
    
    return random.shuffle(list)

a = str(input("Please enter a item you like:"))
b = str(input("Please enter another item you like:"))
c = str(input("Please enter one more item you like:"))
list_abc = [a,b,c] 

shuffle_list(list_abc)

# 2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

# What does unique mean?
