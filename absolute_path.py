import os


def absolute_path(path):
    dirname = os.path.dirname(__file__)

    return os.path.join(dirname, path)
