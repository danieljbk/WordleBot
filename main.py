with open("answers.txt", "r") as answers:
    # store the possible answers into a list
    wordle_words = answers.read().splitlines()

with open("allowed_guesses.txt", "r") as allowed_guesses:
    # add the allowed guesses into the list (because Wordus supports these words)
    wordus_words = allowed_guesses.read().splitlines()

word_database = wordle_words + wordus_words
valid_letters = []

print("Suggested word: " + "crane")
print("Suggested word: " + "later")
print("Suggested word: " + "irate")

for _ in range(6):
    used_word = input("Enter used word: ")
    result = input("Enter result: ")

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

    print(word_database)

    # suggest a word to try
    count = 0
    for word in word_database:
        if count == 3:
            break

        if word in wordle_words:
            print("Suggested word (wordle): " + word)
            count += 1
            continue

    # if the word is not in the wordle database,
    # suggest a word from the wordus database instead
    # that does not have duplicate letters
    for word in word_database:
        if count == 3:
            break

        duplicate_letter_exists = False
        for letter in word:
            if word.count(letter) > 1:
                duplicate_letter_exists = True
                break

        if not duplicate_letter_exists or word == word_database[-1]:
            print("Suggested word (wordus): " + word)
            count += 1
            continue
