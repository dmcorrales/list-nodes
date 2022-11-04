class MyContextManager():

    def __init__(self):
        print("init method called")

    def __enter__(self):
        print("Joined to this")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_val, exc_tb)
        return self

    def open_my_self(self):
        print("CAL INTERNAL FUNCTION")
        return self


if __name__ == '__main__':
    with MyContextManager() as f:
        f.open_my_self()
        print(f)