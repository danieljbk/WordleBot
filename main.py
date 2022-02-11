from letter_value import alphabet, letter_values_for_wordle_and_wordus


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

    print("best word to try: " + best_word)
    print()


print()
print("Welcome to WordleSolver!")
print()

with open("assets/answers.txt", "r") as answers:
    # store the possible answers into a list
    wordle_words = answers.read().splitlines()

with open("assets/allowed_guesses.txt", "r") as allowed_guesses:
    # add the allowed guesses into the list (because Wordus supports these words)
    wordus_words = allowed_guesses.read().splitlines()

word_database = wordle_words + wordus_words

valid_letters = []
answer_found = False

for attempt in range(6):
    if answer_found:
        break

    suggest_best_word(word_database, wordle_words)

    used_word = input("enter used word: ")
    result = input("enter result: ")

    for i in range(5):
        letter = used_word[i]
        outcome = result[i]
        if outcome != "x":
            valid_letters.append(letter)

    for i in range(5):
        letter = used_word[i]
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

    # separate word_database into wordle words and wordus words (for printing only)
    from_wordle = []
    from_wordus = []
    for word in word_database:
        if word in wordle_words:
            from_wordle.append(word)
        elif word in wordus_words:
            from_wordus.append(word)

    print()
    print(from_wordle)
    print(from_wordus)
    print()
