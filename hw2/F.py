def gen (n, counter_open, counter_close, ans):
    if counter_close + counter_open == 2 * n:
        yield ans
    if counter_open < n:
        yield from gen(n, counter_open + 1, counter_close, ans + '(')
    if counter_open > counter_close:
       yield from gen(n, counter_open, counter_close + 1, ans + ')')


def brackets(n):
    yield  from gen(n, 0, 0, '')

if __name__ == '__main__':
    n = int(input())
    for i in brackets(n):
        print(i)
