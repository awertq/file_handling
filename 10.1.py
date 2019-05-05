import text_maker_class as e

file_name = input("Enter filename :")

file1 = e.Text_editor(file_name)        #making file1 object

file1.add_line()                      #writing lines

#print lines in file_name three times by reading
print("\v")
print("1 :")
print()
with open(file_name) as fileq:
	content = fileq.read()
	print(content)

#print content by looping


print("\v")
print("2 :")
print()

with open(file_name):
	for lines in file_name:
		print(lines.strip())

#printing contect by storing it on a list and then printing it
print("\v")
print("3 :")
print()

list = file1.readline(list)

for element in list:
	print(element.strip())

print(list)

