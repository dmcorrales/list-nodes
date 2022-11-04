import datetime

def dt():
    print(datetime.datetime.strptime("2016-04-15T08:27:18-0500", "%Y-%m-%dT%H:%M:%S%z"))

if __name__ == '__main__':
    dt()