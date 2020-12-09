import sys
import shutil
import zipfile
from pathlib import Path

class ZipReplace:
	def __init__(self, zipname):
		self.zipname = zipname
		self.temp_directory = Path("unzipped-{}".format(
			zipname[:-4]))

	def process_zip(self):
		self.unzip_files()
		self.process_files()
		self.zip_files()

	def unzip_files(self):
		self.temp_directory.mkdir()
		with zipfile.ZipFile(self.zipfile) as zip:
			zip.extractall(str(self.temp_directory))

	def zip_files(self):
		with zipfile.ZipFile(self.zipname, 'w') as file:
			for filename in self.temp_directory.iterdir():
				file.write(str(filename), filename.name)
		shutil.rmtree(str(self.temp_directory))


if __name__ == "__main__":
	ZipReplace(*sys.argv[1:4]).zip_find_replace()