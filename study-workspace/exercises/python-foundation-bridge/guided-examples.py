"""Guided examples for rebuilding Python writing ability."""


def count_characters(text):
    """Count how many times each character appears."""
    counts = {}
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1
    return counts


def unique_keep_order(items):
    """Remove duplicate items while keeping first-seen order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result


def filter_even_numbers(numbers):
    """Return only even numbers."""
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens


def sort_scores(score_dict):
    """Sort a name-score dictionary from high score to low score."""
    return sorted(score_dict.items(), key=lambda item: item[1], reverse=True)


def mean(numbers):
    """Calculate average value."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    print("count_characters:", count_characters("banana"))
    print("unique_keep_order:", unique_keep_order(["a", "b", "a", "c", "b"]))
    print("filter_even_numbers:", filter_even_numbers([1, 2, 3, 4, 5, 6]))
    print("sort_scores:", sort_scores({"Alice": 90, "Bob": 75, "Cindy": 88}))
    print("mean:", mean([80, 90, 100]))
