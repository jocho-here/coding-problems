def is_ver_1_bigger(v_1, v_2):
	version_1 = v_1.split('.')
	version_2 = v_2.split('.')
	shorter_len = 0
	longer_ver = 0
	rem = []

	if len(version_1) < len(version_2):
		shorter_len = len(version_1)
		longer_ver = 2
		rem = version_2
	else:
		shorter_len = len(version_2)
		longer_ver = 1
		rem = version_1

	for n in range(0, shorter_len):
		subt = int(version_1[n]) - int(version_2[n])

		if subt > 0:
			return 1
		elif subt < 0:
			return -1

	for i in range(shorter_len, len(rem)):
		if int(rem[i]) > 0:
			if longer_ver == 1:
				return 1
			else:
				return -1

	return 0

def is_valid_ver(ver):
	ver_arr = ver.split(".")
	
	for n in range(0, len(ver_arr)):
		if not ver_arr[n].isdigit():
			return(False)
	
	return(True)

import sys

if len(sys.argv) == 3:
	ver_1 = sys.argv[1]
	ver_2 = sys.argv[2]

	if not is_valid_ver(ver_1) or not is_valid_ver(ver_2):
		print("usage: python version_control.py [version_1] [version_2]: versions should contain dots separating sequences of numbers")
		exit(1)

	print(is_ver_1_bigger(ver_1, ver_2))

elif len(sys.argv) == 1:
	ver_1 = raw_input()
	ver_2 = raw_input()

	if not is_valid_ver(ver_1) or not is_valid_ver(ver_2):
		print("usage: python version_control.py [version_1] [version_2]: versions should contain dots separating sequences of numbers")
		exit(1)
		
	print(is_ver_1_bigger(ver_1, ver_2))
else:
		print("usage: python version_control.py [version_1] [version_2]: versions should contain dots separating sequences of numbers")
