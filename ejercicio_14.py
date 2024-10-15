def extract_confidence(line):
    return float(line[line.find(':')+1:len(line)-1])

def main():
    total = 0
    count = 0
    with open('./input/mbox-short.txt', 'r') as file:
        for line in file:
            if(line.startswith("X-DSPAM-Confidence")):
                total+=extract_confidence(line=line)
                count+=1
    print(f'Average spam confidence: {total/count} (Total msg: {count})')
            
if __name__ == "__main__":
    main()# This is file ejercicio_10.py
