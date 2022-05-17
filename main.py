import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma and a space. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Get the total number of items in List.
num_items = len(names)

#Le resto 1 porque empieza en 0 el indice
random_choice = random.randint(0, num_items - 1)

print(f"The person who is going to pay is : {names[random_choice]}")
