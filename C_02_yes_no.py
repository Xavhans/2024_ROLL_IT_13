def yes_no(question):
    while True:
        response = input(question).lower()


        if response == "yes" or response == "y":
            print("You chose yes")
        elif response == "no" or response == "n":
            print("you chose no")
        else:
            print("You did not chose a valid response")


# Main
while True:
    want_instructions = yes_no("Do you want to read the instructins")
    print(f"you chose {want_instructions}")

