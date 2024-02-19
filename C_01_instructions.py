# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()


        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")

def instruction():
    print('''
    
***** Instructions *****
 
Do something 

    
    
    
    
    ''')




#main
print("Roll it 13")


want_instructions = yes_no("Do you want to read the instructions?\n")

if want_instructions == "yes":
    instruction()
print("Program continues ")

    


