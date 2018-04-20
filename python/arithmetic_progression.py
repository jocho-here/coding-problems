A = None

def find_missing(i, j):
	if i + 1 == j:
		return (A[i] + A[j]) / 2
	
	mid = int((j+i)/2)

	if A[mid] - A[i] < A[j] - A[mid]:
		return find_missing(mid, j)
	else:
		return find_missing(i, mid)

A = [0,1,3,5,7,11]
print(find_missing(1,5))
A = [0,1,3,4,5,6,7,8]
print(find_missing(1,7))
A = [0,1,4,7,13,16,19]
print(find_missing(1,6))
A = [0,1,3,4,5,6,7]
print(find_missing(1,6))
