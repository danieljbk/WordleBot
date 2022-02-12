from assign_letter_values import letter_values
from suggest_best_word import suggest_best_word
from read_words import wordle_words, wordus_words


print()
print("Welcome to WordleSolver! This Program will suggest the best word to use.")
print()

valid_letters = []
answer_found = False
word_database = wordle_words + wordus_words

for attempt in range(6):
    if answer_found:
        break

    best_word = suggest_best_word(
        attempt,
        word_database,
        wordle_words,
        letter_values,
    )
    print("best word to try: " + best_word)
    print()

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
