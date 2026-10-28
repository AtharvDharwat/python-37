import re

text = "a+b*c"
result = re.escape(text)

print(result)