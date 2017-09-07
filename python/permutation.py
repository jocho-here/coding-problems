# Stacks up permutations of given character list
def permutation(list_char, curr_str, perm_list):
	# Leaf part of permutation tree
	if len(list_char) == 1:
		curr_str += list_char[0]
		perm_list.append(curr_str)
	
	else:
		# Go through chars and recursively call the function again
		# then take the current char from curr_str and go on to the next one
		for x in xrange(0, len(list_char)):
			curr_str += list_char[x]
			popped = list_char.pop(x)
			permutation(list_char, curr_str, perm_list)
			curr_str = curr_str[:-1]
			list_char.insert(x, popped)

import sys, itertools

# Incorrect usage of this file
if len(sys.argv) != 2:
	print("usage: python permutation.py <input_chars>")
else:
	perms = []
	permutation(list(sys.argv[1]), '', perms)
	answers = list(itertools.permutations(list(sys.argv[1])))
	answer = True

	# Unit test with python's given library for permutation generator
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
		print("Correct!")
		print(perms)
	else:
		print("Wrong!")
		print("len(perms) = " + str(len(perms)))
		print("len(answers) = " + str(len(answers)))
		print(answers)
		print(perms)
