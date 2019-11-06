import sys

def safe_input():
    try:
        return input()
    except EOFError:
        sys.exit(0)


def main():
    n = 100000
    sep = 10
    beg = 1
    while n > 1:
        for i in range(sep):
            print('? ' + str(beg + n // sep * i))
        print('+', flush = True)
        ans = []
        flag = 0
        for i in range(sep):
            ans.append(int(safe_input()))
        for i in range(sep):
            if ans[i] == 1:
                beg += (i - 1) * (n // sep)
                break
            elif i == sep - 1:
                beg += n // sep * (sep - 1)
            
        n = n // sep
    print('! ' + str(beg))
if __name__ == '__main__':
    main()