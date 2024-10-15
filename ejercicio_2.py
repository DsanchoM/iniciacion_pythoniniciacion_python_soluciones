def main():
    hours = int(input("How many hours did you work?\n"))
    rate = int(input("What is the rate?\n"))

    print(f'You should receive {hours*rate}')

if __name__ == "__main__":
    main()