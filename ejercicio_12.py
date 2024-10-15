def main():
    value = "str = 'X-DSPAM-Confidence: 0.8475="
    extract = float(value[value.find(':')+1:len(value)-1])
    print(f'Value: {extract} of type {type(extract)}')
                
if __name__ == "__main__":
    main()# This is file ejercicio_10.py
