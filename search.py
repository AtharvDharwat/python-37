import re

text = "Python is easy to learn"
pattern = "easy"

result = re.search(pattern, text)

if result:
    print("Pattern found:", result.group())
else:
    print("Pattern not found")