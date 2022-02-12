def analyze_result_and_update_database(used_word, result, database):
    valid_letters = []
    for i in range(5):
        letter = used_word[i]
        outcome = result[i]
        if outcome != "x":
            valid_letters.append(letter)

    for i in range(5):
        letter = used_word[i]
        outcome = result[i]
        copied_database = database.copy()

        # if the letter was in the word and in the right place...
        if outcome == "o":
            for word in copied_database:
                if word[i] != letter:
                    if word in database:
                        database.remove(word)

        # if the letter was in the word but in the wrong place...
        elif outcome == "p":
            for word in copied_database:
                # if the word doesn't have this letter...
                if letter not in word:
                    if word in database:
                        database.remove(word)
                # if the word has this letter in the specific location...
                if word[i] == letter:
                    if word in database:
                        database.remove(word)

        # if the letter was not in the word...
        elif outcome == "x":
            for word in copied_database:
                # if the letter is a duplicate, remove words with this letter in this specific place
                if letter in valid_letters:
                    if word[i] == letter:
                        if word in database:
                            database.remove(word)

                # else, remove words with this letter
                elif letter in word:
                    if word in database:
                        database.remove(word)

    return database
