import random

random.seed()

names_in_string = input("Give me everybody's names, separated by a comma. ")
names_list = names_in_string.split(", ")

number_of_items = len (names_list)
random_person = random.randint(0, number_of_items -1)
who_pays = names_list[random_person]

print(who_pays + " is going to buy the meal today!")
