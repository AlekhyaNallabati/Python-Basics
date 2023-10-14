friend = "Rolf"
user_name = input("Enter your name: ")

if user_name == friend :
    print("Hello, friend!")
else :
    print("Hello, Stranger!")

friends = ["Rolf", "Bob", "Anne"]
family = ["Jen", "Charlie"]

user_name = input("Enter your name : ")

if user_name in friends:
    print("Hello, friend!")
elif user_name in family:
    print("Hello, family!")
else :
    print("I don't know you.")

number = 7
user_input = input("Enter 'y' if would like to play: ").lower()

if user_input == "y" :
    user_number = int(input("Guess your number : "))
    if user_number == number :
        print("you guessed it correctly!")
    elif abs(number - user_number) == 1 :
        print("you were off by one.")
    else :
        print("Sorry, it's wrong!")