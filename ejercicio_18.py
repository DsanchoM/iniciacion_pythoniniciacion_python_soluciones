def main():
    elements = []
    while(str(next := input("Enter a number\n")).lower()!='done'):
        try:
            elements.append(float(next))
        except:
            print(f"Invalid number {next}\n")
    print(f'Sumary\n\tMin: {min(elements)}\n\tMax: {max(elements)}\n\t')
            
if __name__ == "__main__":
    main()# This is file ejercicio_10.py
