# Unit 2 Lesson 1 Homework: Weather Advisory System
# Name: Sydney Montevirgen
# Date: 09.19.25

print("Weather Advisory System")
print("=" * 23)

# Step 1: Get weather information from user
# TODO: Get temperature as integer
temperature = int(input("Temperature: "))

# TODO: Get sunny status and convert to boolean
status = (input("Is it sunny?: "))
if status == "Yes":
    is_sunny = True
else:
    is_sunny = False


# Step 2: Display weather report
print(f"\nWeather Report:")
# TODO: Show temperature and sunny status
print("-" * 18)

# Step 3: Temperature advice
# TODO: Use if-else to give clothing advice based on temperature
if temperature >= 75:
    print(f"Wear a t shirt and shorts")
else:
    if temperature >= 50:
        print(f"Wear a light jacket")
    else:
        print(f"Wear a coat and pants")


# Step 4: Activity suggestions  
# TODO: Use if-else to suggest activities based on sunny status
if is_sunny is True:
    print(f"Go to the beach with friends")
else:
    print(f"Stay inside and watch a movie")

if temperature > 80 and is_sunny is True:
    print(f"Wear sunscreen!")
else:
    if temperature < 50 and is_sunny is False:
        print(f"Stay warm with appropriate clothing!")
    else:
        print(f"Stay safe and have fun!")