import random


def lotek():

    a_list = list(range(1, 50))
    random.shuffle(a_list)
    numbers = a_list[:6]
    numbers = sorted(numbers)
    return numbers


item = 0
user_list = []
random_list = lotek()

for item in range(6):
    guessed = False
    while not guessed:
        str_num = input("Enter number:")
        try:
            num = int(str_num)
        except ValueError:
            print("It's not a number!")
        else:
            if 0 < num < 50:
                if num not in user_list:
                    user_list.append(num)
                    break
                else:
                    print("You already have that one:)")
            else:
                print("number out of range")

user_list = sorted(user_list)
print(f"Computer drew {random_list}")
print(f"Your choice: {user_list}")

result_list = list(set(user_list) - set(random_list))
result = 6 - len(result_list)

print(f"You hit {result} numbers")
if result < 3:
    print("You loose. Maybe next time!")
elif result == 3:
    print("Congratualtions you get 3!")
elif result == 4:
    print("Congratualtions you get 4!")
elif result == 5:
    print("Congratualtions you get 5!")
elif result == 6:
    print("""You are master or cheater! 6/6
             Hey lucky gay,
             Try lotto in real life:)""")
