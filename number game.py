import random
import time

print("--- 🎮 NUMBER MAGIC v1.0 🎮 ---")
print("Maine 1 se 50 ke beech ek number chhipaya hai...")
time.sleep(1)

secret_no = 35
lifelines = 5

while lifelines > 0:
    try:
        print(f"\nRemaining Lifelines: {lifelines}")
        guess = int(input("Apna andaza lagao (1-50): "))
        
        if guess < secret_no:
            print("❌ Thoda BADA number socho bhai!")
            lifelines -= 1
        elif guess > secret_no:
            print("❌ Thoda CHHOTA number dalo!")
            lifelines -= 1
        else:
            print(f"\n🎉 JABARDAST! Aapne sahi pakda!")
            print(f"Asli number {secret_no} hi tha.")
            break
            
    except:
        print("[!] Sirf Number dalo bhai!")

if lifelines == 0:
    print("\n" + "="*25)
    print("      凸(-_-)凸      ")
    print("   GAME OVER BETA!    ")
    print(f"  Sahi number {secret_no} tha.")
    print("   LOLLYPOP KHAO!    ")
    print("="*25)

print("\nKhel khatam!")
