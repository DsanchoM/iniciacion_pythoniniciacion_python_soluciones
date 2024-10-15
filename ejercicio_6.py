def main():
    exit = False
    while(not exit):
        try:
            hours = float(input("How many hours did you work?\n"))
            rate = float(input("What is the rate?\n"))

            print(f'You should receive {(min(hours, 40)*rate)+((max(hours-40, 0))*(rate*1.5))}')
            exit=True
        except:
            print("Error, Please enter a numeric value\n")
            exit=False
            
if __name__ == "__main__":
    main()