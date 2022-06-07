import random

while True:
    choices = ["R","P","S"]

    cpu = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock(R), paper(P), or scissors(S)?: ").upper()
    

    if player == cpu:
        print("Player " ,'(',player,')',':',"CPU " ,'(',cpu,')')
        print("Tie!")


    elif player == "R":
        if cpu == "P":
            print("Player " ,'(',player,')',':',"CPU " ,'(',cpu,')')
            print("You lose!")
        if cpu == "scissors":
            print("Player " ,'(',player,')',':',"CPU " ,'(',cpu,')')
            print("You win!")

    elif player == "S":
        if cpu == "R":
            print("Player " ,'(',player,')',':',"CPU " ,'(',cpu,')')
            print("You lose!")
        if cpu == "P":
            print("Player " ,'(',player,')',':',"CPU " ,'(',cpu,')')
            print("You win!")

    elif player == "P":
        if cpu == "S":
            print("Player " ,'(',player,')',':',"CPU " ,'(',cpu,')')
            print("You lose!")
        if cpu == "R":
            print("Player " ,'(',player,')',':',"CPU " ,'(',cpu,')')
            print("You win!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Bye!")