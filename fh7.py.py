f = open("student.txt", "r")

data = f.read()

print("Total number of characters:", len(data))

f.close()