def main():
    hours = float(input("How many hours did you work?\n"))
    rate = float(input("What is the rate?\n"))

    # We can achieve same behavior using if/else statements
    print(f'You should receive {(min(hours, 40)*rate)+(max((hours-40), 0)*(rate*1.5))}')
if __name__ == "__main__":
    main()