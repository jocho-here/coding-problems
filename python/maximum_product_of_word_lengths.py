class Solution(object):
    def maxProduct(self, words):
	words.sort(key=len, reverse=True)
	actual_words = words[:]
	
	for i in xrange(0, len(words)):
		a = sorted(words[i])
		final = []
		
		for x in xrange(0, len(a)):
			if a[x] not in final:
				final.append(a[x])

		words[i] = ''.join(final)
		
	possible_solutions = []
	possible_solutions.append(0)

	for a_i in xrange(0, len(words)):
		for b_i in xrange(a_i + 1, len(words)):
			match = 0

			for c_i in xrange(0, len(words[b_i])):
				if words[b_i][c_i] in words[a_i]:
					match = 1
					break
					
			if not match:
				possible_solutions.append(len(actual_words[b_i]) 
																	* len(actual_words[a_i]))
	
	possible_solutions.sort(reverse=True)
	return possible_solutions[0]