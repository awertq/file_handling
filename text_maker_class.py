class Text_editor:

	def __init__(self,file_name):
		self.file_name = file_name



	def file_maker(self,file_name):
		file = open(self.file_name,"w")    #making text file
		file.close()

	def add_line(self):
		while True:

			append_line = input("-> ")

			with open(self.file_name,"a") as file:
				file.write(append_line+"\n")             #this variable initialised in programme

			if append_line == "~q":
				break

	def readline(self,line_list):

		line_list = []

		with open(self.file_name) as file_name:
			for l in file_name:
				line_list.append(l)
		return list(line_list)





'''function that reads and print content of file '''

def line_printer(file_path):

	with open(file_path):
		content = file_path.read()
		print(content)
