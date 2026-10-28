import re
string = """My ticket Number is 1234567890 and my friend's ticket number is 7895641235"""

regex = '\d+'
matches = re.findall(regex, string)
print("All matches found:", matches)        