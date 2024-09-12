main.py

from character_classes import (Necromancer, Bard, Warrior, Thief, Mage, Paladin, Archer, Priest, MartialArtist)

def main():
    # Function to create a character based on user choice
    def create_character():
        print("Choose a character class:")
        print("1. Necromancer")
        print("2. Bard")
        print("3. Warrior")
        print("4. Thief")
        print("5. Mage")
        print("6. Paladin")
        print("7. Archer")
        print("8. Priest")
        print("9. Martial Artist")
        
        choice = input("Enter the number of your choice: ")
        
        if choice == '1':
            return Necromancer()
        elif choice == '2':
            return Bard()
        elif choice == '3':
            return Warrior()
        elif choice == '4':
            return Thief()
        elif choice == '5':
            return Mage()
        elif choice == '6':
            return Paladin()
        elif choice == '7':
            return Archer()
        elif choice == '8':
            return Priest()
        elif choice == '9':
            return MartialArtist()
        else:
            print("Invalid choice, creating default Warrior.")
            return Warrior()

    # Create a character based on user input
    character = create_character()
    
    while True:
        print("\nCurrent Stats:")
        print(character.display_stats())
        
        print("\nOptions:")
        print("1. Increase Stat")
        print("2. Level Up")
        print("3. Display Stats")
        print("4. Exit")
        
        option = input("Enter the number of your choice: ")
        
        if option == '1':
            try:
                amount = int(input("Enter the amount to increase: "))
                character.increase_stat(amount)
            except ValueError:
                print("Please enter a valid number.")
        
        elif option == '2':
            character.level_up()
        
        elif option == '3':
            print("\nCurrent Stats:")
            print(character.display_stats())
        
        elif option == '4':
            print("Exiting...")
            break
        
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()

