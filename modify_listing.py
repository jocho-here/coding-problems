import os

cpp = os.listdir('c++')
java = os.listdir('java')
python = os.listdir('python')

new_readme = open('README.md', 'w')

new_readme.write("# Coding Problems\n")
new_readme.write("\n")

new_readme.write("## C++\n")
for i in xrange(0, len(cpp)):
	new_readme.write(str(i + 1) + '. ')

	for word in (cpp[i][:-4]).split('_'):
		new_readme.write(word + ' ')
	new_readme.write('\n')
new_readme.write("\n")

new_readme.write("## Java\n")
for i in xrange(0, len(java)):
	new_readme.write(str(i + 1) + '. ' + java[i][:-5] + '\n')
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
