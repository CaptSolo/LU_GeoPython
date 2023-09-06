import random

skaitlis = random.randint(1, 6)

print()

a1 = input("Uzmini skaitli (no 1 līdz 6): ")
a1 = int(a1)

print()

if a1 == skaitlis:
    print("Uzminēji !!!")

else:
    print(f"Nē, pareizais skaitlis ir {skaitlis}")

print()

