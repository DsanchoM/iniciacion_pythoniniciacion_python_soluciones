def main():
    count = 0
    total = 0
    while(str(next := input("Enter a number\n")).lower()!='done'):
        try:
            total+=float(next)
            count+=1
        except:
            print(f"Invalid number {next}\n")
    print(f'Sumary\n\tTotal: {total}\n\tCount: {count}\n\tMean: {total/count}')
            
if __name__ == "__main__":
    main()# This is file ejercicio_10.py
