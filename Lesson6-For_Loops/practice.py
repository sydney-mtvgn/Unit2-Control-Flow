number = 5
for i in range(1,11):
    result = number * i
    print(f"{number} * {i} = {result}")

word = "Python"
reversed_word = ""

for char in word:
    reversed_word = char + reversed_word

print(reversed_word)

#11
for char in range (10,0,-1):
    print(char)

print(f"Blast off!")

#12
text = "Hello World"
count = 0
for char in text:
    if char.lower() == 'o':
        count += 1
print(count)

#13
password = "Pass123"
uppercase = False
lowercase = False
digits = False

for char in password:
    if 'A' <= char <= 'Z':
        uppercase = True
    elif 'a' <= char <= 'z':
        lowercase = True
    elif '0' <= char <= '9':
        digits = True

valid = len(password) >= 8 and uppercase and lowercase and digits
print(f"Is a Valid Password: {valid}")

#14
sum = 0
for char in range(1,101):
    sum += char
print(sum)

#15
text = "abc123xyz456"
digits = ""

for char in text:
    if '0' <= char <= '9':
        digits += char
print(digits)