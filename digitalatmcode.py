import os

FILE_NAME = "balance_data.txt"

def load_balance():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return int(file.read())
    else:
        return 1000 

def save_balance(amount):
    with open(FILE_NAME, "w") as file:
        file.write(str(amount))

def atm_start():
    balance = load_balance()
    pin = "1234" 
    
    print("--- Bhai Ka Digital ATM ---")
    user_pin = input("Apna 4 digit PIN daalo: ")
    
    if user_pin == pin:
        while True:
            print("\n1. Balance Check\n2. Paise Nikalein\n3. Paise Jama Karein\n4. Bahar Nikalein")
            choice = input("Kya karna chahte ho? (1/2/3/4): ")
            
            if choice == "1":
                print(f"Apka balance hai: ₹{balance}")
            
            elif choice == "2":
                amount = int(input("Kitne paise nikalne hain? "))
                if amount <= balance:
                    balance -= amount
                    save_balance(balance)
                    print(f"₹{amount} nikal gaye. Naya Balance: ₹{balance}")
                else:
                    print("Bhai itne paise nahi hain!")
            
            elif choice == "3":
                amount = int(input("Kitne paise jama karne hain? "))
                balance += amount
                save_balance(balance)
                print(f"₹{amount} jama ho gaye. Naya Balance: ₹{balance}")
            
            elif choice == "4":
                print("ATM use karne ke liye shukriya!")
                break
            else:
                print("Galat option!")
    else:
        print("Galat PIN!")

atm_start()
