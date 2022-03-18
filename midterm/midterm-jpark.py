#!/usr/bin/env python3
print("Name:Meaghan Sass")

password_database = {"Username":"dnedry","Password":"please"}
command_database = {"reboot":"Ok. I will reboot all park systems","shutdown":"Ok. I will shut down all park systems","done":"I hate all this hacker stuff!"}
white_rabbit_object = 0
counter = 0

while counter < 3 and white_rabbit_object == 0:
    input_user = input("Enter Username:")
    input_password = input("Enter Password:")
    if input_user == password_database["Username"] and input_password == password_database["Password"]:
        white_rabbit_object == 1
        print(f"Hi, Dennis. You're still the best hacker in Jurassic Park!")
        user_command = input("Please enter a command:")
        if user_command == "reboot":
            print(command_database["reboot"])
        elif user_command == "shutdown":
            print(command_database["shutdown"])
        elif user_command == "done":
            print(command_database["done"])
        else :
            print("The Lysine Contingency has been put into effect.")
    elif input_user != password_database["Username"] and input_password != password_database["Password"]:
        counter += 1
        print("You didn't say the magic word!",{counter})
        if counter == 3:
            print("You didn't say the magic word!\nYou didn't say the magic word!\nYou didn't say the magic word!\nYou didn't say the magic word!\nYou didn't say the magic word!\nYou didn't say the magic word!\nYou didn't say the magic word!\nYou didn't say the magic word!\nYou didn't say the magic word!\nYou didn't say the magic word!\nYou didn't say the magic word!\nYou didn't say the magic word!\nYou didn't say the magic word!\nYou didn't say the magic word!\nYou didn't say the magic word!\nYou didn't say the magic word!\nYou didn't say the magic word!\nYou didn't say the magic word!\nYou didn't say the magic word!\nYou didn't say the magic word!\nYou didn't say the magic word!\nYou didn't say the magic word!\nYou didn't say the magic word!\nYou didn't say the magic word!\nYou didn't say the magic word!\n")
