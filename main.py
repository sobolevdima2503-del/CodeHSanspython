def retrieve_positive_number():
    while True:
        user_input = input("Enter a positive number: ")
        try:
            num = int(user_input)
            if num > 0:
                return num
            else:
                print("That wasn't a positive number. Try again.")
        except ValueError:
            print("That wasn't an integer. Try again.")

print(retrieve_positive_number())
