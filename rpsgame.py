import random

while True:
    choices = ["R","P","S"]

    cpu = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock(R), paper(P), or scissors(S)?: ").upper()
    print ("You entered a Wrong Command, Try Again!")

    if player == cpu:
        print("Player " ,'(',player,')',':',"CPU " ,'(',cpu,')')
        print("Tie!")


    elif player == "R":
        if cpu == "P":
            print( "cpu: ", cpu)
            print("player: ", player)
            print("You lose!")
        if cpu == "scissors":
            print( "cpu: ", cpu)
            print("player: ", player)
            print("You win!")

    elif player == "S":
        if cpu == "R":
            print( "cpu: ", cpu)
            print("player: ", player)
            print("You lose!")
        if cpu == "P":
            print( "cpu: ", cpu)
            print("player: ", player)
            print("You win!")

    elif player == "P":
        if cpu == "S":
            print( "cpu: ", cpu)
            print("player: ", player)
            print("You lose!")
        if cpu == "R":
            print( "cpu: ", cpu)
            print("player: ", player)
            print("You win!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Bye!")