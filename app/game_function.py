
from random import choice



def determine_winner(user_choice, computer_choice):

    """
    This function test which player wins the game.
    The param of this function are two strings of "rock", "paper", "scissors".
    This function will return which choice wins.
    Example of invoking the function.

    Invoke like this: determine_winner(paper, scissors)
    """

    #return "paper"

    winners = {
        "rock": {
            "rock": None,
            "paper": "paper",
            "scissors": "rock",
        },
        "paper": {
            "rock": "paper",
            "paper": None,
            "scissors": "scissors",
        },
        "scissors": {
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,
        }
    }
    winning_choice = winners[user_choice][computer_choice]
    return winning_choice
    #return "OOPS"