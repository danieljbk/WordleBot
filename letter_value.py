# examine all letters for all words in word database
# rank each letter by how many times it appears

with open("assets/answers.txt", "r") as answers:
    # store the possible answers into a list
    wordle_words = answers.read().splitlines()

with open("assets/allowed_guesses.txt", "r") as allowed_guesses:
    # add the allowed guesses into the list (because Wordus supports these words)
    wordus_words = allowed_guesses.read().splitlines()

word_database = wordle_words + wordus_words

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
frequency = [0] * 26

for word in wordle_words:
    for letter in word:
        for i in range(26):
            if letter == alphabet[i]:
                frequency[i] += 1

letter_values_for_wordle_and_wordus = []
for num in frequency:
    letter_values_for_wordle_and_wordus.append(num / max(frequency))
