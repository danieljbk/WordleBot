import string


def suggest_best_word(attempt, database, wordle_words, letter_values):
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
                value += letter_values[string.ascii_lowercase.index(letter)]
            word_values.append(value)

        if len(copied_database) > 0:
            # choose the best word to use that doesn't have duplicate letters
            best_word = copied_database[word_values.index(max(word_values))]

        else:  # if all words have duplicate letters, re-do the process with the full database
            word_values = []
            for word in database:
                value = 0
                for letter in word:
                    value += letter_values[string.ascii_lowercase.index(letter)]
                word_values.append(value)
            best_word = database[word_values.index(max(word_values))]

    return best_word
