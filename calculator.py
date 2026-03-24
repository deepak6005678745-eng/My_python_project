print("===============================")
print("        BARISH KA EET            ")
print("===============================")

# 1. Fars ka calculation
fars    = float(input("Fars ka number daalein: "))
lines   = float(input("Lines kitni hain: "))
extra   = float(input("Extra eet kitni hain: "))

multiply = fars * lines + extra

print("-" * 25)

# 2. Khadi eet ka calculation
khadi_eet = float(input("Khadi eet ka number daalein: "))
uchai     = float(input("Uchai kitni hai: "))

result = khadi_eet * uchai

# 3. Final Total
final_result = multiply + result

print("\n===============================")
print(f"Fars ka eet    : {multiply}")
print(f"Khadi eet      : {result}")
print("-" * 25)
print(f"TOTAL BRICKS   : {final_result}")
print("===============================")
