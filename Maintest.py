def foo():
    return 'F:foo'


LOGO = "This is Globals name"
namelist = ['jac', 'duck', 'kriit']
PI = 3.14


def change():
    namelist.pop()
    LOGO = "RUN Faster!"
    print(LOGO)


print(namelist)
print(LOGO)
###############################


def outer(num):
    def innerHandler():
        if num > 0:
            print((list(range(num))))
        else:
            print((list(range(abs(num)))))

    return innerHandler


def one(*args):
    print(args)


one()
one(1, 2, 3, 4)


def two(x, y, *args):
    print(x, y, args)


two(3, 40, 4334, 3, 3, 4)


def three(**keyword):
    print(keyword)


three()
three(name='alex', age=25)


def logger(func):
    def inner(*args, **kwargs):
        print("Args:: {0} {1}".format(args, kwargs))
        return func(*args, **kwargs)
    return inner


@logger
def mymul(x, y=2):
    return x * y


@logger
def myconst():
    return 100


mymul(8, y=3)
myconst()
