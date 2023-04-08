import numpy
one_d,two_d,three_d = input().split()
print(numpy.zeros(shape=(int(one_d),int(two_d),int(three_d)),dtype=int))
print(numpy.ones(shape=(int(one_d),int(two_d),int(three_d)),dtype=int))