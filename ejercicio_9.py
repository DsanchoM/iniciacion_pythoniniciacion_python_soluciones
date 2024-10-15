def compute_grade(score):
    if score < 0 or score > 1:
        return(f'{score} is not a valid input, please try again')
    elif score >= 0.9:
        return('A')
    elif score >= 0.8:
        return('B')
    elif score >= 0.7:
        return('C')
    elif score >= 0.6:
        return('D')
    else:
        return("F")


def main():
    print(compute_grade(0.9))
    print(compute_grade(0.1))
            
if __name__ == "__main__":
    main()