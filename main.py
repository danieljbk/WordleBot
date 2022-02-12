from assign_letter_values import letter_values
from suggest_best_word import suggest_best_word
from read_words import wordle_words, wordus_words
from analyze_result import analyze_result_and_update_database


spacer = "\n\n" + "-" * 80 + "\n\n"
print(spacer)
print("Welcome to WordleSolver! I will suggest the best word for you to try.")

word_database = wordle_words + wordus_words

for attempt in range(6):
    best_word = suggest_best_word(
        attempt,
        word_database,
        wordle_words,
        letter_values,
    )

    print(spacer + "\n" + "** The Best Word to Try: " + "'" + best_word + "'")

    used_word = input(
        spacer
        + "\n"
        + "What Word Did You Use? Type your answer in lowercase.\n"
        + "\n"
        + f"[Example: '{best_word}']"
        + "\n"
        + "- "
    )

    result = input(
        spacer
        + "\n"
        + "And, What Was The Result?\n"
        + "\n"
        + "Type 'x' for grey (wrong),\n"
        + "     'p' for orange (possible),\n"
        + " and 'o' for green (correct).\n"
        + "\n"
        + "[Example: 'oxpxo']\n"
        + "- "
    )

    if result == "ooooo":  # YOU WON!
        print(spacer)
        print("We did it!")
        print("\n")
        break

    word_database = analyze_result_and_update_database(
        used_word,
        result,
        word_database,
    )

    # separate word_database into wordle words and wordus words (for printing only)
    from_wordle, from_wordus = [], []
    for word in word_database:
        if word in wordle_words:
            from_wordle.append(word)
        elif word in wordus_words:
            from_wordus.append(word)

    print(spacer)
    print("REMAINING WORDS:")
    print()
    print("- From Wordle:", from_wordle)
    print()
    print("- From Wordus:", from_wordus)

    if attempt == 5:  # if you reach this point on the last attempt, YOU LOST!
        print(spacer)
        print("I'm sorry... My failure rate is around 1%.")
        print("\n")
        break
