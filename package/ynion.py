def display_menu():
    while True:
        print("\nHello! My name is Ma. Bea Mae Ynion")
        print("1. Basic Info")
        print("2. Goals")
        print("3. Comments")
        print("4. Exit")
        
        choice = int(input("Enter your choice:"))

        match choice:
            case 1:
                print("\nDate of Birth : July 29, 2004")
                print("\nAge : 20")
            case 2:
                print("\nGoals: To learn more about programming languages and improve my problem-solving skills.")
            case 3:
                print("\nComments")
                #TODO DELIMA
                #TODO RELENTE
                #TODO QUIAMBAO
                #TODO CITRON
            case 4:
                print("\nExiting the menu.")
                return