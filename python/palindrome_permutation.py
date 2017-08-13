def can_permute_palindrome(s):
	"""
	:type s: str
	:rtype: bool
	"""
	letters = {}

	for letter in s:
		if letters.has_key(letter):
			letters[letter] += 1
		else:
			letters.setdefault(letter, 1)
	
	odd_allowed = True

	for key in letters:
		if letters[key] & 1 == 1:
			if len(s) & 1 == 0:
				return False
			elif odd_allowed:
				odd_allowed = False
			else:
				return False
	
	return True

print can_permute_palindrome("carerac")
