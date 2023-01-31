import time


def write():
    inicio = time.time()
    file = open("app.txt", "w")
    for i in range(1, 100000):
        file.write(str(i) + "\n")
    fin = time.time()
    print(fin - inicio)
    file.close()


if __name__ == '__main__':
    write()
