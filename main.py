# create word suggestion algorithm that puts a value on each word based on how popular its letters are

with open("answers.txt", "r") as answers:
    # store the possible answers into a list
    wordle_words = answers.read().splitlines()

with open("allowed_guesses.txt", "r") as allowed_guesses:
    # add the allowed guesses into the list (because Wordus supports these words)
    wordus_words = allowed_guesses.read().splitlines()

word_database = wordle_words + wordus_words
valid_letters = []
answer_found = False

print()
print("Welcome to WordleSolver!")
print()
print("Best starter - crane")
print("Best follow-up - sloth")
print()

for _ in range(6):
    if answer_found:
        break

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

    # separate word_database into wordle words and wordus words (for printing only)
    from_wordle = []
    from_wordus = []
    for word in word_database:
        if word in wordle_words:
            from_wordle.append(word)
        elif word in wordus_words:
            from_wordus.append(word)

    print(from_wordle)
    print(from_wordus)
    print()

    # suggest a word to try
    count = 0
    for word in word_database:
        if count == 2:
            break

        if word == word_database[-1]:
            print("    The Answer is", word)
            answer_found = True
            break

        duplicate_letter_exists = False
        for letter in word:
            if word.count(letter) > 1:
                duplicate_letter_exists = True
                break

        if not duplicate_letter_exists:
            # prioritize words used by wordle
            if word in wordle_words:
                print("    Suggestion", count + 1, "-", word)
            elif word in wordus_words:
                print("    Suggestion", count + 1, "-", word)
            count += 1
            continue
    print()
