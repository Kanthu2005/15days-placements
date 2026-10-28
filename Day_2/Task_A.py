# Task A — Coding: Write a function that removes duplicates from a list while preserving the
# first-seen order. Do not use a one-line shortcut. Include at least five test cases.
def remove_dup(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
print(remove_dup([1, 2, 3, 2, 1, 4]))