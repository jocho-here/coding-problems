def findWords(words):
	rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
	rtn_vals = []

	for word_i in xrange(0, len(words)):
		word = words[word_i].lower()
		i = 0
		possible = True 

		if word[0] in rows[1]:
			i = 1 
		elif word[0] in rows[2]:
			i = 2

		for letter in word[1:]:
			if letter not in rows[i]:
				possible = False
				break

		if possible == True:
			rtn_vals.append(words[word_i])

	return rtn_vals

print findWords(["Hello", "Alaska", "Dad", "Peace"])
