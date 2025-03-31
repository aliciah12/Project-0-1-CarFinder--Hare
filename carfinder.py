# Define the dataset
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

# Define a function to display the menu and handle user input

def display_menu():
    while True:
        print("/n=== CarFinder MENU ===/n")
        print("1. PRINT all Allowed Vehicles")
        print ("2. EXIT")

    # Get the user's choice
        choice = input("Enter your choice (1-2): ")
        if choice == '1':
            print("/nAllowed Vehicles:")
            for vehicle in AllowedVehiclesList:
                    print (f"- {vehicle}")
        elif choice == '2':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Main program execution
if __name__ == "__main__":
    display_menu()