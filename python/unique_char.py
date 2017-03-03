def unique_char(input_str):
	char_list = sorted(input_str)

	for n in range(0, len(char_list) - 1):
		if char_list[n] == char_list[n+1]:
			return False
	
	return True

import sys

if len(sys.argv) != 2:
	print("usage: python unique_char.py <input_string>")
else:
	print(str(unique_char(str(sys.argv[1]))))
