import re as re
from functools import reduce

def solution1(arg):
    #return [int(re.sub('[,./-]', '', st)[::-1]) for st in arg]
    return list(map(lambda x: int(re.sub('[,./-]', '', x)[::-1]), arg))

def solution2(arg):
    #return [a * v for a, v in arg]
    return list(map(lambda x: x[0] * x[1], arg))

def solution3(arg):
    #return[a for a in arg if not a % 6 == 1 and not a % 6 == 3 and not a % 6 == 4]
    return list(filter(lambda a:not a % 6 == 1 and not a % 6 == 3 and not a % 6 == 4, arg))

def solution4(arg):
    #return[a for a in arg if bool(a)]
    return list(filter(lambda x: x, arg))

def solution5(arg):
    return list(map(lambda d: d.__setitem__('square', d['width'] * d['length']), arg))

def solution6(arg):
    return list(map(lambda d: dict(d, square=d['width']*d['length']), arg))

def solution7(arg):
    return reduce(lambda x, y: x & y, arg)

def solution8(arg):
    return reduce(lambda x, y: x.__setitem__(y, 1 if y not in x else x[y] + 1)  or x, arg, {})

def solution9(arg):
    return [x['name'] for x in list(filter(lambda x: x['gpa'] > 4.5, arg))]

def solution10(arg):
    return list(filter(lambda x: sum([int(a) for a in x][::2]) == sum([int(a) for a in x][1::2]), arg))

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

rooms = [
    {"name": "комната1", "width": 2, "length": 4},
    {"name": "комната2", "width": 2.5, "length": 5.6},
    {"name": "кухня", "width": 3.5, "length": 4},
    {"name": "туалет", "width": 1.5, "length": 1.5},
]

students = [
    {'name': 'Alina', 'gpa': 4.57},
    {'name': 'Sergey', 'gpa': 5.0},
    {'name': 'Nastya', 'gpa': 4.21},
    {'name': 'Valya', 'gpa': 4.72},
    {'name': 'Anton', 'gpa': 4.32},
]

#print(solution8([1, 2, 1, 1, 3, 2, 3, 2, 4, 2, 4]))
#x = {1 : 2}
#print(x[1])