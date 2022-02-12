import string


# attempt to only suggest official wordle words
def filter_wordle_words(database, copied_database, wordle_words):
    for word in database:
        if word not in wordle_words:
            copied_database.remove(word)

    if len(copied_database) > 0:  # update the database
        database = copied_database.copy()
    else:  # if there are no wordle words, revert
        copied_database = database.copy()

    return database, copied_database


# assign each word a value based on its letters
def assign_word_values(database, letter_values):
    word_values = []
    for word in database:
        value = 0
        for letter in word:
            value += letter_values[string.ascii_lowercase.index(letter)]
        word_values.append(value)

    return word_values


def suggest_best_word(attempt, database, wordle_words, letter_values):
    # suggest the best word to use
    best_word = "crane"
    if attempt > 0:
        copied_database = database.copy()

        database, copied_database = filter_wordle_words(
            database, copied_database, wordle_words
        )

        # get rid of words with duplicate letters and save to copied_database
        for word in database:
            for letter in word:
                if word.count(letter) > 1:
                    copied_database.remove(word)
                    break

        word_values = assign_word_values(copied_database, letter_values)

        # if there are words remaining, choose the best word to use
        if len(copied_database) > 0:
            best_word = copied_database[word_values.index(max(word_values))]

        else:  # if all words have duplicate letters, suggest the word with the least duplicate letters
            copied_database = database.copy()

            database, copied_database = filter_wordle_words(
                database, copied_database, wordle_words
            )

            duplicate_counts = []
            for word in database:
                duplicate_count = 0
                for letter in word:
                    if word.count(letter) > 1:
                        duplicate_count += 1
                duplicate_counts.append(duplicate_count)
            for word in database:
                duplicate_count = 0
                for letter in word:
                    if word.count(letter) > 1:
                        duplicate_count += 1
                if duplicate_count != min(duplicate_counts):
                    copied_database.remove(word)

            word_values = assign_word_values(copied_database, letter_values)
            best_word = copied_database[word_values.index(max(word_values))]

    return best_word
