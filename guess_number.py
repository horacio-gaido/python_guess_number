import random
import os
os.system("cls")

def play_game():
    """Main function that runs the game"""
    attempts = 0
    secret_number = generate_secret_number()
    while True:
        attempts += 1
        guess = get_user_guess()
        if guess == secret_number:
            print(f'Congratulations! You guessed the secret number in {attempts} attempts.\n')
            break
        else:
            print(get_hint_message(guess, secret_number))


def generate_secret_number():
    """Function that generates the secret number"""
    return random.randint(1, 100)


def get_user_guess():
    """Function that asks the user for their guess and validates the input"""
    while True:
        try:
            guess = int(input('\nEnter a number between 1 and 100: '))
            if guess < 1 or guess > 100:
                raise ValueError('The number must be between 1 and 100.')
            return guess
        except ValueError as e:
            print(e)


def get_hint_message(guess, secret_number):
    """Function that returns a message indicating if the guess is higher or lower than the secret number"""
    if guess < secret_number:
        return 'The secret number is higher.'
    else:
        return 'The secret number is lower.'


if __name__ == '__main__':
    play_game()
