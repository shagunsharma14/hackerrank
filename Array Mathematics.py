import numpy

n, m = input().split()
a_arr = [input().split() for _ in range(int(n))]
b_arr = [input().split() for _ in range(int(n))]

a_arr = numpy.array(a_arr,int)
b_arr = numpy.array(b_arr,int)

print(numpy.add(a_arr,b_arr))
print(numpy.subtract(a_arr,b_arr))
print(numpy.multiply(a_arr,b_arr))
print(numpy.floor_divide(a_arr, b_arr))
print(numpy.mod(a_arr,b_arr))
print(numpy.power(a_arr, b_arr))


