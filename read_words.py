import os


def absolute_path(path):
    dirname = os.path.dirname(__file__)

    return os.path.join(dirname, path)


with open(absolute_path("assets/answers.txt"), "r") as answers:
    # store the possible answers into a list
    wordle_words = answers.read().splitlines()

with open(absolute_path("assets/allowed_guesses.txt"), "r") as allowed_guesses:
    # add the allowed guesses into the list (Wordus supports these words)
    wordus_words = allowed_guesses.read().splitlines()
