import itertools
import string
import time

import os
real_path = os.path.dirname(os.path.realpath(__file__))

def common_guess(word: str) -> str | None:
    """Checks a file filled with common words"""

    with open(f'{real_path}\\passwords.txt', 'r') as words:
        word_list: list[str] = words.read().splitlines()

    for i, match in enumerate(word_list, start=1):
        if match == word:
            return f'Common match: {match} (#{i})'


# Goes through every combination of chars
def brute_force(word: str, length: int, digits=False, symbols=False) -> str | None:
    """Performs brute force on finding a word"""
    
    # Modify this for total symbols
    chars: str = string.ascii_lowercase

    if digits:
        chars += string.digits

    if symbols:
        chars += string.punctuation

    attempts: int = 0
    for guess in itertools.product(chars, repeat=length):
        attempts += 1
        guess: str = ''.join(guess)
        if guess == word:
            return f'"{word}" was cracked in {attempts:,} guesses.'
        # print(guess, attempts) # Comment this out when you're not testing


def main():
    password: str = input("Enter The Password more than 3 characters but less than 4")
    print('Searching...')
    

    # Get the start time
    start_time: float = time.perf_counter()

    # Search for common words before using the actual brute force
    if common_match := common_guess(password):
        print(common_match)
    else:
        for i in range(3,4):
            if cracked := brute_force(password, length=i, digits=False, symbols=False):
                print(cracked)
                break
            else:
                print('There was no match...')

    # Get the end time
    end_time: float = time.perf_counter()

    # Display the time it took
    print(round(end_time - start_time, 4), 's')


if __name__ == '__main__':
    main()