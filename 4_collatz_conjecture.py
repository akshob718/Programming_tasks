import matplotlib.pyplot as plt


def collatz_conjecture(num):
    iterations = 0
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = 3 * num + 1
        iterations += 1

    return iterations


if __name__ == '__main__':
    result = {}
    lower_limit = 100
    upper_limit = 110

    for i in range(lower_limit, upper_limit+1):
        result[i] = collatz_conjecture(i)
    #print(result)
    x = sorted(result.keys())
    y = []
    for key in x:
        y.append(result[key])

    plt.plot(x, y, marker='o')
    plt.xlabel('Number')
    plt.ylabel('Iterations')
    plt.show()
    plt.bar(x, y)
    plt.xticks(x)
    plt.yticks(y)
    plt.xlabel('Number')
    plt.ylabel('Iterations')
    plt.show()