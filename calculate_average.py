import random
from assign_letter_values import letter_values
from suggest_best_word import suggest_best_word
from read_words import wordle_words, wordus_words


total_guesses = 0
failed_games = 0
times_repeated = 100

for loop in range(times_repeated):
    print("Running:", loop + 1, end="\r")

    # guess from wordus words as well as wordle words
    word_database = wordle_words + wordus_words

    # run my code against the official wordle game, not the wordus game
    word_of_the_day = random.choice(wordle_words)

    valid_letters = []
    for attempt in range(6):
        current_word = suggest_best_word(
            attempt,
            word_database,
            wordle_words,
            letter_values,
        )

        # calculate results for the guessed word
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

        for i in range(5):
            letter = current_word[i]
            outcome = result[i]
            if outcome != "x":
                valid_letters.append(letter)

        for i in range(5):
            letter = current_word[i]
            outcome = result[i]
            duplicated_word_database = word_database.copy()

            # if the letter was in the word and in the right place...
            if outcome == "o":
                for word in duplicated_word_database:
                    if word[i] != letter:
                        if word in word_database:
                            word_database.remove(word)

            # if the letter was in the word but in the wrong place...
            elif outcome == "p":
                for word in duplicated_word_database:
                    # if the word doesn't have this letter...
                    if letter not in word:
                        if word in word_database:
                            word_database.remove(word)
                    # if the word has this letter in the specific location...
                    if word[i] == letter:
                        if word in word_database:
                            word_database.remove(word)

            # if the letter was not in the word...
            elif outcome == "x":
                for word in duplicated_word_database:
                    # if the letter is a duplicate,
                    # remove words with this letter in this specific place
                    if letter in valid_letters:
                        if word[i] == letter:
                            if word in word_database:
                                word_database.remove(word)
                    elif letter in word:
                        if word in word_database:
                            word_database.remove(word)

        if attempt == 5:  # if you reach this point on attempt #5, YOU LOST!
            failed_games += 1

# Ignore the times the algorithm failed
print("Average:", round(total_guesses / (times_repeated - failed_games), 2))
print("Failed:", failed_games, "times")
