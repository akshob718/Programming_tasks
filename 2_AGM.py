from itertools import combinations
import matplotlib.pyplot as plt
import math


def find_agm(each_pair):
    a = each_pair[0]
    b = each_pair[1]
    precision = 0.05
    agm = 0.0
    while abs(a - b) >= precision:
        am = (a + b) / 2
        gm = math.sqrt(a * b)
        a = am
        b = gm
        agm = a
    return agm


if __name__ == '__main__':
    lower_limit = 3
    upper_limit = 9
    numbers = []
    for i in range(lower_limit, upper_limit + 1):
        numbers.append(i)
        i += 1
    pairs = combinations(numbers, 2)
    pairs = list(pairs);
    x = []
    y = []
    num = 1
    for each_pair in pairs:
        agm = find_agm(each_pair)
        x.append(num)
        num += 1
        y.append(agm)
        print('AGM of', each_pair, 'is: ', agm)

    plt.plot(x, y, marker="o")
    plt.xlabel('Pairs')
    plt.ylabel('AGM')
    plt.xticks(x, pairs)
    plt.title('AGM for each pair in the given range')
    plt.show()
