import random

def get_hint(secret, guess):
    correct_digits = sum(1 for s, g in zip(secret, guess) if s == g)
    return f"{correct_digits} digits are correct."

def play_round(player_name, secret):
    attempts = 0
    while True:
        attempts += 1
        guess = input(f"{player_name}, enter your guess: ")
        if guess == secret:
            print(f"Congratulations, {player_name}! You guessed the number in {attempts} attempts.")
            return attempts
        else:
            print(get_hint(secret, guess))

def mastermind_game():
    print("Welcome to the Mastermind Game!")

    secret1 = input("Player 1, set your multi-digit number (no spaces): ")
    while not secret1.isdigit():
        print("Invalid input. Please enter a valid multi-digit number.")
        secret1 = input("Player 1, set your multi-digit number (no spaces): ")

    
    print("\nPlayer 2, it's your turn to guess.")
    attempts_player2 = play_round("Player 2", secret1)

    
    secret2 = input("Player 2, set your multi-digit number (no spaces): ")
   
    while not secret2.isdigit():
        print("Invalid input. Please enter a valid multi-digit number.")
        secret2 = input("Player 2, set your multi-digit number (no spaces): ")


    print("\nPlayer 1, it's your turn to guess.")
    attempts_player1 = play_round("Player 1", secret2)

   
    if attempts_player1 < attempts_player2:
        print("\nPlayer 1 wins and is crowned Mastermind!")
    elif attempts_player2 < attempts_player1:
        print("\nPlayer 2 wins and is crowned Mastermind!")
    else:
        print("\nIt's a tie! Both players are equally Mastermind!")


if __name__ == "__main__":
    mastermind_game()
