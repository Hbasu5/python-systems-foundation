from basics import basics
from core_logic import core_logic

def main():
    while True:
        print("\n=====Python Foundation Menu=====")
        print("1. Basics")
        print ("2. Core Logic")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            basics.run()
        elif choice == "2":
            core_logic.run()
        elif choice == "3":
            print("Exiting the Python Foundation Course.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()