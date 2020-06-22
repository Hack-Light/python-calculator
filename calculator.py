import re

print("Our awesome Calculator")
print("Type quit to exit")

previous = 0
run = True


def calculate():

    global previous
    global run

    expression = input("Type in your equation here ")

    if (expression == "Quit" or expression == "quit"):
        print("Goodbye, friend")
        run = False
    else:
        
        expression = re.sub("[a-zA-Z,:()" "]"," ", expression)
        result = eval(expression)
        print(result)
    

while run:
    calculate()    