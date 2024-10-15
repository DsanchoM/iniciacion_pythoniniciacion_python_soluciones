def compute_pay(hours, rate):
    print(f'You should receive {(min(hours, 40)*rate)+(max((hours-40), 0)*(rate*1.5))}')



def main():
    compute_pay(10, 10)
    compute_pay(45, 10)
            
if __name__ == "__main__":
    main()