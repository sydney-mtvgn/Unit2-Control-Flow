# First Way
height = int(input("Height in inches: "))
print(f"Your height: {height} inches")
if height >= 72:
    print(f"You are tall.")
if height >= 60 and height <= 71:
    print(f"You are average height.")
if height < 60:
    print(f"You are short.")

# Second way
height = int(input("Height in inches: "))
print(f"Your height: {height} inches")

if height >= 72:
    print("You are tall!")
else:
    if height >= 60:
        print("You are average height")
    else:
        print("You are short!")