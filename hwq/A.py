def main():
    n = int(input())
    a = [int(i) for i in input().split()]

    i = 0
    while i < len(a):
        j = i + 1
        while j < len(a):
            if a[j] == a[i]:
                del a[j]
            else:
                j += 1
        i += 1

    for i in range(len(a)):
        print(a[i], end = ' ')
    print('\n', n - len(a), sep = '')
    
if __name__ == '__main__':
    main()