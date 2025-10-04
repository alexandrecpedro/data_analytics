# 1. FUNCTION
def display_hyphens():
    print('-----')

# 2. MAIN PROGRAM
def main():
    print("Start of the program")
    list_obj = [10, 20, 30, 40]
    for item in list_obj:
        print(item)
        display_hyphens()
    print('End of the program')

if __name__ == '__main__':
    main()