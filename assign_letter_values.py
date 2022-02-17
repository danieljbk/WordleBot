import string


def assign_letter_values(word_database):
    letter_frequency = [[0] * 26] * 5

    # examine the total letter_frequency of each letter
    for word in word_database:  # based on the specific words left in database
        for i in range(len(word)):
            for j in range(26):
                if word[i] == string.ascii_lowercase[j]:
                    letter_frequency[i][j] += 1

    # rank each letter by how many times it appears
    letter_values = []
    for i in range(5):
        letter_values_for_each_place = []
        for each_place in letter_frequency:
            for number in each_place:
                letter_values_for_each_place.append(number / max(each_place))
        letter_values.append(letter_values_for_each_place)

    return letter_values
