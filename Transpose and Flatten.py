import numpy
n_row,m_col = input().split()
arr = numpy.array([input().split() for _ in range(int(n_row))],int)

print(numpy.transpose(arr))
print(arr.flatten())