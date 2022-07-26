print("Welcome to Python Pizza Deliveries!\n")
size = input("What size pizza do you want? S, M, or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")

small_pepperoni = 2
big_pepperoni = 3
cheese = 1
total_price = 0

if size == "S":
    total_price = 15
    if add_pepperoni == "Y":
        total_price += small_pepperoni
    if extra_cheese == "Y":
        total_price += cheese
elif size == "M":
    total_price = 20
    if add_pepperoni == "Y":
        total_price += big_pepperoni
    if extra_cheese == "Y":
        total_price += cheese
elif size == "L":
    total_price = 25
    if add_pepperoni == "Y":
        total_price += big_pepperoni
    if extra_cheese == "Y":
        total_price += cheese

print(f"Your final bill is: $ {total_price}.")
