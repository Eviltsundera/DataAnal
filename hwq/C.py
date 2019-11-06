def main():
    inpt = input().split()
    n = int(inpt[0])
    k = int(inpt[1])

    flag = 0

    for i in range(n - k):
        if flag == 0:
            print(1, end = ' ')
            flag = 1
        else:
            print(2, end = ' ')
            flag = 0
    if flag == 0:
        for i in range(k):
            print(i + 1, end = ' ')
    else:
        for i in range(k):
            if i == 0:
                print(2, end = ' ')
            elif i == 1:
                print(1, end = ' ')
            else:
                print(i + 1, end = ' ')

if __name__ == '__main__':
    main()