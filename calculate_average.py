import random
from assign_letter_values import assign_letter_values
from suggest_best_word import suggest_best_word
from read_words import wordle_words, wordus_words
from analyze_result import analyze_result_and_update_database
import multiprocessing


def calculate_average(word_of_the_day):
    total_guesses = 0
    failed_games = 0

    # guess from wordus words as well as wordle words
    word_database = wordle_words.copy()

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
            # print(word_of_the_day + ":", int(total_guesses), "guesses")
            break

        word_database = analyze_result_and_update_database(
            current_word, result, word_database,
        )

        if attempt == 5:  # if you reach this point on the last attempt, YOU LOST!
            failed_games += 1
            print(word_of_the_day + ":", "failed")
            break

    return total_guesses, failed_games


if __name__ == "__main__":
    how_many_times = 1000

    random_numbers = []
    for i in range(how_many_times):
        random_numbers.append(wordle_words[random.randint(0, len(wordle_words) - 1)])

    with multiprocessing.Pool(processes=8) as pool:
        results = pool.map(calculate_average, random_numbers)
    pool.close()

    total_guesses = 0
    failed_games = 0
    for loop in results:
        total_guesses += loop[0]
        failed_games += loop[1]

    # Calculate the average number of guesses while ignoring the times the algorithm failed
    print("Average:", round(total_guesses / (how_many_times - failed_games), 2))
    print("Failed:", failed_games, "times")
