import numpy
n_row,m_row,p_col = input().split()
l1 = []
l2 = []
for _ in range(int(n_row)):
    l1.append(input().split())
for _ in range(int(m_row)):
    l2.append(input().split())

array_1 = numpy.array(l1,int)
array_2 = numpy.array(l2,int)

print(numpy.concatenate((array_1,array_2),axis=0))
