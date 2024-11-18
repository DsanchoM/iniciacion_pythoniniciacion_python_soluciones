words = []
with open("../resources/romeo.txt", 'r') as file:
    for line in file:
        lineWords = line.split()
        for word in lineWords:
           if not word.lower() in words:
               words.append(word.lower())
words.sort()
print(words)