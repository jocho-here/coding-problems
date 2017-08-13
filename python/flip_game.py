def generate_possible_next_moves(s):
	"""
	:type s: str
	:rtype: List[str]
	"""
	rtn_list = []
	i = 0

	while i < len(s) - 1:
		if s[i] == '+' and s[i] == s[i+1]:
			new_s = s[:i] + '--' + s[i+2:]
			rtn_list.append(new_s)
		
		i += 1
	
	return rtn_list

s = "-++-"
print(generate_possible_next_moves(s))
