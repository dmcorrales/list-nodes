# A test object


if __name__ == '__main__':
    import pickle

    f = open("pickled.txt", "wb")
    dct = {"name": "Rajeev", "age": 23, "Gender": "Male", "marks": 75}
    pickle.dump(dct, f)
    f.close()

    f = open("pickled.txt", "rb")
    d = pickle.load(f)
    print(d)
    f.close()

    dct = {"name": "Rajeev", "age": 23, "Gender": "Male", "marks": 75}
    new = pickle.dumps(dct)
    print(new)

    new_new = pickle.loads(new)
    print(new_new)
