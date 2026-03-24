import time

print("--- SMART CALCULATOR v3.0 ---")

try:
    
    n1 = 99
    op = "*"
    n2 = 1

    if op == "+": res = n1 + n2
    elif op == "-": res = n1 - n2
    elif op == "*": res = n1 * n2
    elif op == "/": res = n1 / n2
    else: res = "Error"

    if n1 == 99 and op == "*" and n2 == 1:
        print("\n[!] SECRET VAULT DETECTED...")
        time.sleep(1)
        
        pass_key  = "REVUUFULL"
        
        if pass_key == "DEEPAK":
            print("\n--- ACCESS GRANTED ---")
            print("Bhai, saara data safe hai!")
        else:
            
            print("\n" + "="*25)
            print("      _  _  _      ")
            print("     | || || |     ")
            print("     | || || |     ")
            print("  _  | || || |  _  ")
            print(" | |_|      |_| |  ")
            print(" |    STOP!!!   |  ")
            print(" |______________|  ")
            print("\n  BAHUT SHANE BANTE HO?")
            print("   LOLLYPOP KHAO BETA!")
            print("="*25)
    else:
        print(f"\nResult: {res}")

except:
    print("\n[!] Input Galat Hai!")
