import matplotlib.pyplot as plt

def get_gray_code(n):
    if n <= 0:
        return
    result = []
    result.append("0")
    result.append("1")
    i = 2
    while True:
        if i >= 1 << n:
            break
        for j in range(i - 1, -1, -1):
            result.append(result[j])
        for j in range(i):
            result[j] = "0" + result[j]
        for j in range(i, 2 * i):
            result[j] = "1" + result[j]
        i = i << 1
    return result, len(result)


if __name__ == '__main__':
    n_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = []
    lengths = []
    for k in range(len(n_values)):
        result, length = get_gray_code(n_values[k])
        print('Gray code for', n_values[k], ':', result)
        lengths.append(length)
    #print(lengths)

    plt.plot(n_values, lengths)
    plt.xlabel('Index')
    plt.ylabel('Gray code')
    plt.title('Fixed point function')
    plt.show()