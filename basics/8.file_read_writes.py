# File reads and writes

‘r+’	open file for reading and writing. Raises an I/O error if the file does not exist.
‘w’	    open file for writing. Truncates the file if it already exists. Creates a new file if it does not exist.
‘w+’	open file for reading and writing. Truncates the file if it already exists. Creates a new file if it does not exist.
‘a’	    open file for writing. The data being written will be inserted at the end of the file. Creates a new file if it does not exist.
‘a+’	open file for reading and writing. The data being written will be inserted at the end of the file. Creates a new file if it does not exist.
‘rb’	open file for reading in binary format. Raises an I/O error if the file does not exist.
‘rb+’	open file for reading and writing in binary format. Raises an I/O error if the file does not exist.
‘wb’	open file for writing in binary format. Truncates the file if it already exists. Creates a new file if it does not exist.
‘wb+’	open file for reading and writing in binary format. Truncates the file if it already exists. Creates a new file if it does not exist.
‘ab’	open file for appending in binary format. Inserts data at the end of the file. Creates a new file if it does not exist.
‘ab+’	open file for reading and appending in binary format. Inserts data at the end of the file. Creates a new file if it does not exist.


f = open("test.txt", "r")
f = open("test.txt", "w")
f = open("test.txt", "a")
f = open("test.txt", "r+")
print(f.name)
print(f.mode)
f.close()


with open("test.txt", "r") as f:
    pass
print(f.mode)

with open("test.txt", "r") as f:
	f_contents = f.read()
	print(f_contents)

with open("test.txt", "r") as f:
	f_contents = f.readlines()
	print(f_contents)

with open("test.txt", "r") as f:
	f_contents = f.readline()
	print(f_contents)

with open("test.txt", "r") as f:
	for line in f:
		print(line, end = '')

with open("test.txt", "r") as f:
	f_contents = f.read(100)
	print(f_contents, end = '')

with open("test.txt", "r") as f:

	size = 100
	f_contents = f.read(size)
	while len(f_contents) > 0:
		print(f_contents)
		f_contents = f.read(size)

with open("test.txt", "r") as f:

	f.seek(10)
	f_contents = f.read(100)
	print(f_contents, end = '')

with open("test2.txt", "w") as f:
	pass

with open("test2.txt", "w") as f:
	f.write("Test")
	f.seek(2)
	f.write("Test")

with open("test.txt", "r") as rf:
	with open("test_copy.txt", "w") as wf:
		for line in rf:
			wf.write(line)
            
# TODO : advaced data dumps

# pickle
# sqlite
# json/yaml