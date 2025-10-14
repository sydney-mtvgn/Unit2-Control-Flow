# While loop syntax
# count = 5 # 1 - Start/initialize
# while count > 0: # 2 - Check condition
#     print(count)
#     count -= 1 # 3 - Update
# print("Blast off!")

count = 1
while count < 11:
    print(count)
    count += 1

text = "Bergen Tech"
length = len(text)
i = 0
result = ''
# while i < len(text):
#     print(text[i])
#     i += 1
while i < len(text):
    char = text[i]
    if 'A' <= char <= 'Z':
        result += char
    i += 1
print(result)

# Age validator example
age = -1
while age < 0 or age > 120:
    age = int(input("Enter your age: "))
    if age < 0 or age > 120:
        print("Invalid! Try again.")

print(f"Your age is {age}.")