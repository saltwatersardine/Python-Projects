import random

names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_paying = names[random_choice]
#person_paying = random.choice(names) - this will do the same as line 6-8
print(person_paying + " is going to buy the meal today!")
