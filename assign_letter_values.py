import string


def assign_letter_values(word_database):
    letter_frequency = [0] * 26

    # examine the total letter_frequency of each letter
    for word in word_database:  # *calculating based on wordle words only!
        for letter in word:
            for i in range(26):
                if letter == string.ascii_lowercase[i]:
                    letter_frequency[i] += 1

    # rank each letter by how many times it appears
    letter_values = []
    for num in letter_frequency:
        letter_values.append(num / max(letter_frequency))

    return letter_values
