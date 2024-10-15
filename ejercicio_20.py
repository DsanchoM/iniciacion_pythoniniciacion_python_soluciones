import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def main():
    dict = {}
    filename = input("Enter a file name\n")
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('From '):
                day = line.split()[2]
                if day in dict:
                    dict[day] += 1
                else:
                    dict[day] = 1

    data = pd.DataFrame(data=dict.values(), index=dict.keys())
    sns.barplot(x=data.index, y=data[0])
    print(dict)
            
if __name__ == "__main__":
    main()# This is file ejercicio_10.py
