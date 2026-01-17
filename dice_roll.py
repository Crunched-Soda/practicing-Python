
# ask for rolling the dice
while True:
    dice_roll=input("Do you want to roll the dice? (yes/no): ").strip().lower()
    # if user agrees generare two random numbers between 1 and 6
    if dice_roll == "yes":
        import random
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"You rolled a {die1} and a {die2}.")
    #if user disagrees print a thank you message
    elif dice_roll == "no":
        print("Thank you!")
        break
    #any other input print invalid input message
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")