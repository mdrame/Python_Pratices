#---- Instruction --------

# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input),
#  compare them, print out a message of congratulations
#   to the winner, and ask if the players want to start a new game)
#
# Remember the rules:
#
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

def user(playerOneInput, playerTwoInput):
    if playerOneInput ==  playerTwoInput:
        return "Draw"
    elif playerOneInput == "rock" and playerTwoInput == "paper":
        return " playerTwo wins"
    elif playerOneInput == "rock" and playerTwoInput == "scissors":
        return " playerTwo wins"
    elif playerOneInput == "rock" and playerTwoInput == "paper":
