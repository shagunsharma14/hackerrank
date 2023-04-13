import numpy

n = int(input())
arr = numpy.array([input().split() for _ in range(n)],float)
print(numpy.linalg.det(arr))
