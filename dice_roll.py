import random
min = 1
max = 6

roll_again = input("Enter the choice")

while roll_again == "yes" or roll_again == "y":
    print("Rolling the dices....")
    print("The values are....")
    print(random.randint(min,max))
    print(random.randint(min,max))
    roll_again = input("Roll the dices again?")

