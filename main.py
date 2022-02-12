from assign_letter_values import letter_values
from suggest_best_word import suggest_best_word
from read_words import wordle_words, wordus_words
from analyze_result import analyze_result_and_update_database


print()
print("Welcome to WordleSolver! This Program will suggest the best word to use.")
print()

word_database = wordle_words + wordus_words

for attempt in range(6):
    best_word = suggest_best_word(
        attempt,
        word_database,
        wordle_words,
        letter_values,
    )
    print("the best word to try is: " + best_word)
    print()

    word_database = analyze_result_and_update_database(
        input("what word did you use?: "),
        input("what was the result?: "),
        word_database,
    )

    # separate word_database into wordle words and wordus words (for printing only)
    from_wordle, from_wordus = [], []
    for word in word_database:
        if word in wordle_words:
            from_wordle.append(word)
        elif word in wordus_words:
            from_wordus.append(word)

    print()
    print(from_wordle)
    print(from_wordus)
    print()
