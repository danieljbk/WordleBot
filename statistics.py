import random

failure = 0
total = 0
repeat = 50
for _ in range(repeat):
    with open("answers.txt", "r") as answers:
        # store the possible answers into a list
        word_database = answers.read().splitlines()

    word_of_the_day = random.choice(word_database)
    used_word = "crane"

    valid_letters = []
    for attempt in range(6):
        used_word = word_database[0]

        # create results for guess
        result = ""
        for i in range(5):
            letter = used_word[i]
            if letter == word_of_the_day[i]:
                result += "o"
            elif letter in word_of_the_day:
                result += "p"
            else:
                result += "x"

        # You Won!
        if result == "ooooo":
            total += attempt + 1
            break

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
        # You Lost!
        if attempt == 5:
            failure += 1

# Ignore the times the algorithm failed
print("Average:", round(total / (repeat - failure), 2))
print("Failed:", failure, "times")
