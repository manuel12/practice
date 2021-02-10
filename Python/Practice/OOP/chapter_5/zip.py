from zip_processor import ZipProcessor

class ZipReplace:
	def __init__(self, filename, search_string, 
		replace_string):
		super()._init__(filename)
		self.search_string = search_string
		self.replace_string = replace_string
		
	def process_file(self):
		'''Perform a search adn replace of all files in the
		temporary directory.'''
		for filename in self.temp_directory.iterdir():
			with filename.open() as file:
				contents = file.read()
			contents = contents.replace(
				self.search_string, self.replace_string)
			with filename.open("w") as file:
				file.write(contents)

if __name__ == "__main__":
	ZipReplace(*sys.argv[1:4]).zip_find_replace()