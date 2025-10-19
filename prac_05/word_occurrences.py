"""
CP1404 Practical - Word Occurrences
Estimate: 15 minutes
Actual: 12 minutes
"""

words_to_count = {}

text = input("Text: ")
# text = "this is a collection of words of nice words this is a fun thing it is"
words = text.split()
for word in words:
    try:
        words_to_count[word] += 1
    except KeyError:
        words_to_count[word] = 1

max_length = max(len(word) for word in words)

for word in sorted(words_to_count):
    print(f"{word:{max_length}} : {words_to_count[word]}")


