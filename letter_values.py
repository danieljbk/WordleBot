import string
from absolute_path import absolute_path


with open(absolute_path("assets/answers.txt"), "r") as answers:
    # store the possible answers into a list
    wordle_words = answers.read().splitlines()

with open(absolute_path("assets/allowed_guesses.txt"), "r") as allowed_guesses:
    # add the allowed guesses into the list (because Wordus supports these words)
    wordus_words = allowed_guesses.read().splitlines()

word_database = wordle_words + wordus_words

frequency = [0] * 26

# examine all letters for all words
for word in wordle_words:  # calculating based on wordle words only!
    for letter in word:
        for i in range(26):
            if letter == string.ascii_lowercase[i]:
                frequency[i] += 1

# rank each letter by how many times it appears
letter_values = []
for num in frequency:
    letter_values.append(num / max(frequency))
