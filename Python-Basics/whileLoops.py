user_input = input("Do you wish to run the program? (yes/no): ")

while user_input == "yes" :
    print("we're Running!")
    user_input = input("Do you wish to run the program? (yes/no): ")

print("we stopped running the program.")

user_input = input("Please Enter 'p' or 'q' : ")

while user_input != 'q' :
    if user_input == 'p' :
        print("Hello")
    user_input = input("Please Enter 'p' or 'q' : ")

number = 7

while True :
    user_input = input("Would you like to play?(Y/n): ")

    if user_input == "n":
        break

    user_number = int(input("Guess your number : "))
    if user_number == number :
        print("you guessed it correctly!")
    elif abs(number - user_number) == 1 :
        print("you were off by one.")
    else :
        print("Sorry, it's wrong!")
