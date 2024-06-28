"""
Word Occurrences
Estimate: 20 minutes
Actual: 29 minutes
"""
word_to_count = {}
text_line = input("Enter a line of text: ")
words = text_line.split()
words.sort()

for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
print("Word Counts")
for word, count in word_to_count.items():
    print(f"{word:<10} : {count}")
