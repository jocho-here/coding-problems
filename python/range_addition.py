def getModifiedArray(length, updates):
	rtn_list = [0] * (length + 1)

	for update in updates:
		rtn_list[update[0]] += update[2]
		rtn_list[update[1] + 1] -= update[2]

	for i in xrange(1, length):
		rtn_list[i] += rtn_list[i - 1]

	return rtn_list[:-1]

print(getModifiedArray(5, [[1,  3,  2],[2,  4,  3],[0,  2, -2]]))
#[
# [1,3,2],
# [2,4,3],
# [0,2,-2],
#]
