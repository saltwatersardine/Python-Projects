celsius = input ("what is the tempreture? \n").split()

fahrenheit = []

for temp in celsius:
    fahrenheit.append((9/5)*float(temp) + 32)

print (f"The tempreture is {fahrenheit[0]}°F")

#or this method

celsius = input ("what is the tempreture? \n").split()

fahrenheit = [((9/5)*float(temp) + 32) for temp in celsius]

print (f"The tempreture is {fahrenheit[0]}°F")
