if __name__ == '__main__':
    with open("./file.txt") as file:
        for row in file:
            print(row)
        file.readline()