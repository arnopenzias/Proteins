def count_char(text, char):
	count = 0
	for c in text:
		if c == char:
			count += 1
	return count

file = open("newfile.txt", "w")
file.write("""MQKISKY... 
HTVGDRYEMA*
""")

file.close()
filename = "newfile.txt"
with open(filename) as f:
	text = f.read()

	
for char in "ACDEFGHIKLMNPQRSTVYW":
	counting_aminoacids = count_char(text, char)
	print("{0} - {1}".format(char, counting_aminoacids))


counting_all = 0
for char in "ACDEFGHIKLMNPQRSTVYW":
	counting_all += count_char(text, char)
	print(counting_all)
