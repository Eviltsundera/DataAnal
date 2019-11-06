def solution1(arg):
    return [4 * i for i in arg]

def solution2(arg):
    return [(i + 1) * arg[i] for i in range(len(arg))]

def solution3(arg):
    return [i for i in arg if i % 3 == 0 or i % 5 == 0]

def solution4(arg):
    return [i for d in arg for i in d]

def solution5(arg):
    return [(c, b, a) for c in range(1, arg + 1) for b in range(c, arg + 1)
             for a in range(b, arg + 1) if a ** 2 == b ** 2 + c ** 2]

def solution6(arg):
    return [[a + b for b in arg[1]] for a in arg[0]]

def solution7(arg):
    return [[arg[i][j] for i in range(len(arg))] for j in range(len(arg[0]))]

def solution8(arg):
    return [[int(char) for char in str.split()] for str in arg]

def solution9(arg):
    return {chr(ord('a') + v) : v ** 2 for v in arg}

def solution10(arg):
    return set(name.capitalize() for name in arg if len(name) > 3)



solutions = {
    'solution1': solution1,
    'solution2': solution2,
    'solution3': solution3,
    'solution4': solution4,
    'solution5': solution5,
    'solution6': solution6,
    'solution7': solution7,
    'solution8': solution8,
    'solution9': solution9,
    'solution10': solution10,
}
