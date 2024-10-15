def main():
    count = 0
    with open('./input/mbox-short.txt', 'r') as file:
        for line in file:
            if line.startswith('From '):
                print(line.split()[1])
                count+=1
    print(f'There were {count} lines in the file with the word From as the first word')
            
if __name__ == "__main__":
    main()# This is file ejercicio_10.py
