def main():
    score = float(input("Enter your Score (between 0.0 and 1.0)"))
    if score < 0 or score > 1:
        print(f'{score} is not a valid input, please try again')
    elif score >= 0.9:
        print('A')
    elif score >= 0.8:
        print('B')
    elif score >= 0.7:
        print('C')
    elif score >= 0.6:
        print('D')
    else:
        print("F")
            
if __name__ == "__main__":
    main()