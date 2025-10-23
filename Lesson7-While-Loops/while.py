# # While loop syntax
# # count = 5 # 1 - Start/initialize
# # while count > 0: # 2 - Check condition
# #     print(count)
# #     count -= 1 # 3 - Update
# # print("Blast off!")

# count = 1
# while count < 11:
#     print(count)
#     count += 1

# text = "Bergen Tech"
# length = len(text)
# i = 0
# result = ''
# # while i < len(text):
# #     print(text[i])
# #     i += 1
# while i < len(text):
#     char = text[i]
#     if 'A' <= char <= 'Z':
#         result += char
#     i += 1
# print(result)

# # Age validator example
# age = -1
# while age < 0 or age > 120:
#     age = int(input("Enter your age: "))
#     if age < 0 or age > 120:
#         print("Invalid! Try again.")

# print(f"Your age is {age}.")

# while True:
#     answer = input("Continue? ")
#     if answer == "no":
#         break
#     print("Going...")

# print("Done!")

# # Skip to Next Iteration, continue statement
# count = 0
# while count < 5:
#     count += 1
#     if count == 3:
#         continue
#     print(count)

# number = 7
# while True:
#     guess = (int(input("Pick a Number: ")))
#     if guess < number:
#         print("Higher!")
#         continue
#     elif guess > number:
#         print("Lower!")
#         continue
#     else:
#         print("Correct!")
#         break

number = 0
sum = 0
while True:
    user_input = (int(input("Enter a number: ")))
    if user_input != number:
        sum += user_input
    else:
        break
print(f"Total Sum: {sum}")

# Alternative
total = 0
number = int(input("Enter a number(0 to stop): "))

while number != 0:
    total += number
    number = int(input("Enter a number (0 to stop): "))

print(f"Total Sum: {total}")
