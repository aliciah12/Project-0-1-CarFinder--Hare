# Define the dataset
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

# Function to display menu
def display_menu():
    while True:
        print("\n********************************")
        print("AutoCountry Vehicle Finder v0.1")
        print("********************************")
        print("Please Enter the following number below from the following menu:\n")
        print("1. PRINT all Authorized Vehicles")
        print("2. SEARCH for a Vehicle")
        print("3. Exit")
        
        # Get user choice
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
            for vehicle in AllowedVehiclesList:
                print(f"- {vehicle}")
        elif choice == "2":
            search_vehicle = input("Enter the name of the vehicle to search: ")
            if search_vehicle in AllowedVehiclesList:
                print(f"{search_vehicle} is in the authorized vehicles list.")
            else:
                print(f"{search_vehicle} is NOT in the authorized vehicles list.")
        elif choice == "3":
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Main entry point
if __name__ == "__main__":
    display_menu()