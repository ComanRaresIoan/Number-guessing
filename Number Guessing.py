import random

# We define an interval with left and right borders
left = int(input("Please enter a number you want to be the left border of the interval: "))
right = int(input("Please enter a number you want to be the right border of the interval: "))

if left < right:
    interval = (left, right)
    print("The interval you have chosen is:", interval)
else:
    print("Error, the interval borders have to be in ascending order.")
    left, right = right, left

number = random.randint(left, right)

attempts = right - left + 1
print("You have a number of", attempts, "attempts. ")

while attempts != 0:
    try:
        guess = int(input(f"Guess the number between {left} and {right}: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if left <= guess <= right:
        if number < guess:
            print("The number is smaller.")
        elif number > guess:
            print("The number is greater.")
        else:
            print("Correct! You have guessed the number!")
            break
    else:
        print(f"Please enter a number within the range of {left} and {right}.")

    attempts -= 1

if attempts == 0:
    print("Sorry, you couldn't guess the number. The correct number was", number)

