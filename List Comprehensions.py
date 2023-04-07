if __name__ == '__main__':
    x = [int(_) for _ in range(int(input()) + 1)]
    y = [int(_) for _ in range(int(input()) + 1)]
    z = [int(_) for _ in range(int(input()) + 1)]
    n = int(input())

    lists = [[i, j, k] for i in x for j in y for k in z if i + j + k is not n]
    print(lists)

