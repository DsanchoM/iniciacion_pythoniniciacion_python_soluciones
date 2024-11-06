with open('../resources/fileToRead.txt','r') as file:
    content = file.read()

print(content.upper())