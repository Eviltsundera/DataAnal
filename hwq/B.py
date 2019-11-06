def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    
    b = []
    for i in range(n):
        tmp = tuple(str(a[i]))
        s = 0
        for c in tmp:
            s += int(c)
        b.append((s, a[i]))
    b.sort()
    
    for i in range(n):
        print(b[i][1], end = ' ')

if __name__ == '__main__':
    main()