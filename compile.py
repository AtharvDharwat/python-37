import re

pattern = re.compile("Python")

text = "Python is easy to learn"

result = pattern.search(text)

if result:
    print("Pattern found:", result.group())
else:
    print("Pattern not found")