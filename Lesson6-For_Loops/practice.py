number = 5
for i in range(1,11):
    result = number * i
    print(f"{number} * {i} = {result}")

word = "Python"
reversed_word = ""

for char in word:
    reversed_word = char + reversed_word

print(reversed_word)