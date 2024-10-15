def main():
    words = []
    with open('./input/romeo.txt', 'r') as file:
        for line in file:
            # Better use a set
            for word in line.split():
                if word not in words:
                    words.append(word)
    words.sort()        
    print(words)
            
if __name__ == "__main__":
    main()# This is file ejercicio_10.py
