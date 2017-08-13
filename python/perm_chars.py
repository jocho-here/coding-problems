# It returns permutaion of given string

# perm() receives a list of chars and manipulate permutation of 
# them recursively
def perm(chars):
	# Base case
	if len(chars) == 1:
		return chars
	else:
		# Recursive call on a list of smaller chars
		curr_char = chars.pop()
		perms = perm(chars)
		new_perms = []

		# Algorithm: when curr_char = 'b' and ['a'] was returned, 'b' would
		# 					 be inserted in front of 'a' and after 'a' 
		for word in perms:
			for index in range(0, len(word) + 1):
				new_perms.append(word[:index] + curr_char + word[index:])

		return new_perms

import sys, itertools

# Incorrect usage of this file
if len(sys.argv) != 2:
	print("usage: python perm_char.py <input_string>")
else:
	perms = perm(list(sys.argv[1]))
	answers = list(itertools.permutations(list(sys.argv[1])))
	answer = True 

	# Unit test with python's given library for permuatation generator
	for answer in answers:
		str_form = ''.join(answer)
		
		try:
			perms.index(str_form)
		except ValueError:
			answer = False
			print("False")
			print(str_form)
			print(perms.index(str_form))
	
	if answer and len(perms) == len(answers):
		print(perms)
	else:
		print("Wrong!")
		print("len(perms) = " + str(len(perms)))
		print("len(answers) = " + str(len(answers)))
		print(answers)
		print(perms)
