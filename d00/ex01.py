import sys


def concArgvs():
    new = 'x '.join(sys.argv[1:len(sys.argv)])
    return new[::-1].swapcase()


print(concArgvs())
