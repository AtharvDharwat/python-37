s = input("Enter a sentence: ")

words = s.split()

if len(words) > 0:
    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    print("Longest word:", longest)
else:
    print("No words found")