sahi_pass = "1234"
user_pass =  "1234"

while user_pass != sahi_pass:
    user_pass = input("Password dalo: ")
    
    if user_pass == sahi_pass:
        print("Sahi hai bhai! Welcome.")
    else:
        print("Galat hai, firse koshish karo.")
