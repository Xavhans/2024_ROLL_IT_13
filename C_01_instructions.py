# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        want_instructions = input(question)


    if want_instructions == "yes" or want_instructions == "y":
        return "yes"
    elif want_insrtuctions == "no" or want_instructions == "n":
        return "no"
    else:
        print("You did not chose a valid response")

#main
while True:
    want_instructions = yes_no("Do you want to read the instructins")
    print(f"you chose {want_instructions}")
    


