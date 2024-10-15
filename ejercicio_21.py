def main():
    dict = {}
    # filename = input("Enter a file name")
    filename = './input/mbox-short.txt'
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('From '):
                email = line.split()[1]
                if email in dict:
                    dict[email] += 1
                else:
                    dict[email] = 1

    print(max(dict, key=dict.get))
            
if __name__ == "__main__":
    main()# This is file ejercicio_10.py
