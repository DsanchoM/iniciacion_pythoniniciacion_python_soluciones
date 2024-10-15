def chop(elements):
    elements = elements[1:-1]
    print(f'Chopping list {elements} (not very useful)')
def middle(elements):
    chop(elements=elements)
    return elements[1:-1]


def main():
    print(middle([1, 2, 3, 4]))
            
if __name__ == "__main__":
    main()# This is file ejercicio_10.py
