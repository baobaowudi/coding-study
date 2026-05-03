"""Fill-in-the-blanks exercises.

Keep TODO markers until you finish them yourself.
Run this file after each change:

    .\\.venv\\Scripts\\python.exe study-workspace\\exercises\\python-foundation-bridge\\fill-in-blanks.py
"""


def double_numbers(numbers):
    """Return a new list where every number is doubled."""
    result = []
    for number in numbers:
        # TODO: append number * 2 to result
        pass
    return result


def count_words(text):
    """Return a dict of word counts."""
    counts = {}
    words = text.split()
    for word in words:
        # TODO: update counts[word]
        pass
    return counts


def keep_positive(numbers):
    """Return only positive numbers."""
    result = []
    for number in numbers:
        # TODO: if number > 0, append it to result
        pass
    return result


def total_score(score_dict):
    """Return sum of all scores in a dictionary."""
    total = 0
    for name, score in score_dict.items():
        # TODO: add score to total
        pass
    return total


if __name__ == "__main__":
    print("double_numbers:", double_numbers([1, 2, 3]))
    print("count_words:", count_words("python python data"))
    print("keep_positive:", keep_positive([-2, 0, 3, 5]))
    print("total_score:", total_score({"Alice": 90, "Bob": 80}))
