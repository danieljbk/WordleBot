import os
import random
from letter_value import alphabet, wordle_words, letter_values_for_wordle_and_wordus


def absolute_path(path):
    dirname = os.path.dirname(__file__)

    return os.path.join(dirname, path)


def suggest_best_word(database, wordle_words):
    # suggest the best word to use
    best_word = "crane"
    if attempt > 0:
        word_values = []
        copied_database = database.copy()

        # only suggest official wordle words
        for word in database:
            if word not in wordle_words:
                copied_database.remove(word)
        if len(copied_database) > 0:
            database = copied_database.copy()
        else:
            copied_database = database.copy()

        # get rid of words with duplicate letters and save to copied_database
        for word in database:
            for letter in word:
                if word.count(letter) > 1:
                    copied_database.remove(word)
                    break

        # assign each word a value based on its letters
        for word in copied_database:
            value = 0
            for letter in word:
                value += letter_values_for_wordle_and_wordus[alphabet.index(letter)]
            word_values.append(value)

        if len(copied_database) > 0:
            # choose the best word to use that doesn't have duplicate letters
            best_word = copied_database[word_values.index(max(word_values))]
        else:  # if all words have duplicate letters
            # re-do the process using the actual database
            word_values = []
            for word in database:
                value = 0
                for letter in word:
                    value += letter_values_for_wordle_and_wordus[alphabet.index(letter)]
                word_values.append(value)
            best_word = database[word_values.index(max(word_values))]

    return best_word


total = 0
failure = 0
repeat = 100
for loop in range(repeat):
    print("Running:", loop + 1, end="\r")
    with open(absolute_path("assets/answers.txt"), "r") as answers:
        # store the possible answers into a list
        word_database = answers.read().splitlines()

    word_of_the_day = random.choice(word_database)

    valid_letters = []
    for attempt in range(6):
        current_word = suggest_best_word(word_database, wordle_words)

        # create results for guess
        result = ""
        for i in range(5):
            letter = current_word[i]
            if letter == word_of_the_day[i]:
                result += "o"
            elif letter in word_of_the_day:
                result += "p"
            else:
                result += "x"

        # You Won!
        if result == "ooooo":
            total += attempt + 1
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
        # You Lost!
        if attempt == 5:
            failure += 1

# Ignore the times the algorithm failed
print("Average:", round(total / (repeat - failure), 2))
print("Failed:", failure, "times")
