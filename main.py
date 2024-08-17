choise = input('Выберите букву: ')
if choise == 'а':
    '''А'''
    for i in range(6):
        for j in range(6, i, -1):
            print("*", end="")
        print()
        for k in range(i):
            print(" ", end="")
elif choise == 'б':
    '''Б'''
    for i in range(0, 6):
        print('*' * i, end='\n')
elif choise == 'в':
    for i in range(14):
        for j in range(14):
            print("*" if (j > i and j < 14 - i - 1) else " ", end="")
        print()
elif choise == 'г':
    for i in range(14):
        for j in range(14):
            print("*" if (j < i and j > 14 - i - 1) else " ", end="")
        print()
elif choise =='д':
    for i in range(6):
        for j in range(6):
            print("*" if (j >= i and j < 6 - i) or (j <= i and j >= 6 - i - 1) else " ", end="")
        print()
elif choise == 'е':
    for i in range(14):
        for j in range(14):
            print(" " if (j > i and j < 14 - i - 1) or (j < i and j >= 14 - i) else "*", end="")
        print()
elif choise == 'ж':
    for i in range(1, 8):
        print("*" * i)
    for i in range(6, 0, -1):
        print("*" * i)
elif choise == 'з':
    for i in range(1, 8):
        print(" " * (7 - i) + "*" * i)
    for i in range(6, 0, -1):
        print(" " * (7 - i) + "*" * i)
elif choise == 'и':
    for i in range(6, 0, -1):
        print('*' * i)
elif choise == 'к':
    for i in range(6):
        for j in range(6, i + 1, -1):
            print(" ", end="")
        for j in range(i + 1):
            print("*", end="")
        print()
    print("\n")
