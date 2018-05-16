#!/usr/bin/python

import os
import subprocess

python = os.listdir('python')

new_readme = open('README.md', 'w')

new_readme.write("# Coding Problems\n")
new_readme.write("\n")

new_readme.write("## Python\n")
for i in xrange(0, len(python)):
	new_readme.write(str(i + 1) + '. ')

	for word in (python[i][:-3]).split('_'):
		new_readme.write(word + ' ')
	new_readme.write('\n')
new_readme.write("\n")

new_readme.write("### Let's solve problems!")
new_readme.write("\n")
new_readme.close()

subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '-m', 'Updated'])
subprocess.call(['git', 'push', 'origin', 'master'])
