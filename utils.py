# all about repr
class Represent(object):

    def __init__(self):
        self.x = 123

    def __repr__(self):
        return "REPRESENTATION!!!!!!!!"

    def __str__(self):
        return "OK!!!!"

if __name__ == '__main__':
    s = "HOLAA"
    print(repr(s))
    print(eval(repr(s)) == s)

    import datetime
    x = datetime.datetime.now()
    print(x)
    print(repr(x))
    print(repr(Represent()))
    print(str(Represent()))
 




