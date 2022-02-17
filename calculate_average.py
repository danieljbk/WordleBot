import random
from assign_letter_values import assign_letter_values
from suggest_best_word import suggest_best_word
from read_words import wordle_words, wordus_words
from analyze_result import analyze_result_and_update_database


total_guesses = 0
failed_games = 0
times_repeated = 100

for loop in range(times_repeated):
    print("Running:", loop + 1, end="\r")

    # guess from wordus words as well as wordle words
    word_database = wordle_words.copy()

    # run my code against the official wordle game, not the wordus game
    word_of_the_day = random.choice(wordle_words)

    for attempt in range(6):
        current_word = suggest_best_word(
            attempt, word_database, wordle_words, assign_letter_values(word_database),
        )

        # identify the result for the guessed word
        result = ""
        for i in range(5):
            letter = current_word[i]
            if letter == word_of_the_day[i]:
                result += "o"
            elif letter in word_of_the_day:
                result += "p"
            else:
                result += "x"

        if result == "ooooo":  # YOU WON!
            total_guesses += attempt + 1
            break

        word_database = analyze_result_and_update_database(
            current_word, result, word_database,
        )

        if attempt == 5:  # if you reach this point on the last attempt, YOU LOST!
            failed_games += 1
            break

# Calculate the average number of guesses while ignoring the times the algorithm failed
print("Average:", round(total_guesses / (times_repeated - failed_games), 2))
print("Failed:", failed_games, "times")
