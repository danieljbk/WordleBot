import string


# only suggest words with the least amount of duplicate letters
def filter_words_with_duplicate_letters(database):
    copied_database = database.copy()

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

    return copied_database


# only suggest wordle words, unless there are no wordle words
def filter_wordle_words(database, wordle_words):
    copied_database = database.copy()

    for word in database:
        if word not in wordle_words:
            copied_database.remove(word)

    # if no wordle words exist, revert to the original database
    if not copied_database:
        return database

    # otherwise, return the new database
    return copied_database


# assign a value to each word based on its letters
def assign_word_values(database, letter_values):
    word_values = []
    for word in database:
        value = 0
        for i in range(len(word)):
            value += letter_values[i][string.ascii_lowercase.index(word[i])]
        word_values.append(value)

    return word_values


def suggest_best_word(attempt, database, wordle_words, letter_values):
    # suggest the best word to use
    if attempt == 0:
        best_word = "slane"
    else:
        database = filter_wordle_words(database, wordle_words)
        database = filter_words_with_duplicate_letters(database)
        word_values = assign_word_values(database, letter_values)
        best_word = database[word_values.index(max(word_values))]

    return best_word
