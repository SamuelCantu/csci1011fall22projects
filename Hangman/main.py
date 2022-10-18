import re

# Get the answer.
answer = "What's up, Doc?"

answer = answer.upper()

#Pre-game setup.
asnwer_guessed = []

for current_answer_character in answer:
    if re.search("^[A-Z]$", current_answer_character):
        asnwer_guessed.append(False)
    else:
        asnwer_guessed.append(True)

#Game logic.
num_of_incorrect_guesses = 5

current_incorrect_guesses = 0

letter_guessed = []

#User gameplay logic.
while current_incorrect_guesses < num_of_incorrect_guesses and False in asnwer_guessed:
    # Display game summary.
    print(f"number of incorrect guesses remaining: {num_of_incorrect_guesses - current_incorrect_guesses}")