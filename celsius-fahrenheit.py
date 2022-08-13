celsius = input ("what is the tempreture? \n")

fahrenheit = []

for temp in celsius.split():
    fahrenheit.append((9/5)*float(temp) + 32)

print (f"The tempreture is {fahrenheit[0]}°F")

#or this method

celsius = input ("what is the tempreture? \n")

fahrenheit = [((9/5)*float(temp) + 32) for temp in celsius.split()]

print (f"The tempreture is {fahrenheit[0]}°F")
