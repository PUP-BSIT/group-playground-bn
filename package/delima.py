print("Mabuhay, I am Justine Delima")
user_choice = 0

while user_choice != 4:
    user_choice = int(input("Enter your choice: "))

    match user_choice:
        case 1: #  Basic Info
            print('Age: 19')
            print('Birthdate: February 24, 2005')
            print('Current Education: Polytechnic of the Philippines-Taguig')
        case 2: # Goal
            print('Goal: To have a stable life.')
        case 3: # Comments
            print('Comment mo bading - Name')
            # TODO Ynion
            # TODO Patricia Joy
            # TODO Patricia Anne
            # TODO Kath
        case 4: # Exit
            print('Goodbye bading.')
    