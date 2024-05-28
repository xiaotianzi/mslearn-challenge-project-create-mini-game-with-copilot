import random

def determine_winner(player1, player2):
    if player1 == player2:
        return "It's a tie!"
    elif (player1 == "rock" and player2 == "scissors") or (player1 == "scissors" and player2 == "paper") or (player1 == "paper" and player2 == "rock"):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"


def play_game():
    player_score = 0
    computer_score = 0
    play_again = True

    while play_again:
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        computer_choice = random.choice(["rock", "paper", "scissors"])

        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        result = determine_winner(player_choice, computer_choice)
        print(f"Player chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        print(result)

        if result == "Player 1 wins!":
            player_score += 1
        elif result == "Player 2 wins!":
            computer_score += 1

        play_again = input("Do you want to play again? (yes/no): ").lower() == "yes"

    print("Game over!")
    print(f"Player score: {player_score}")
    print(f"Computer score: {computer_score}")

play_game()
