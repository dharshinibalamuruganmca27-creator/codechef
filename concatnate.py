import numpy

if __name__ == '__main__':
    n,m,p = list(map(int,input().split(' ')))
    l = []
    for i in range(n+m):
        ab = list(map(int,input().split(' ')))
        l.append(ab)
    array = numpy.array(l)
    print(array)
