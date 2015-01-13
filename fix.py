from tempfile import mkstemp
from shutil import move
from os import remove, close
import sys


if __name__ == "__main__":
  file_path = sys.argv[1]
  replaceAll(file_path,'EXDATE;"', 'EXDATE;TZID="')

# Inspired by:
# http://stackoverflow.com/questions/39086/search-and-replace-a-line-in-a-file-in-python
def replaceAll(file_path, pattern, substr):
  # Create temp file
  fh, temp_path = mkstemp()
  temp_file = open(temp_path, 'w')
  old_file = open(file_path)
  for line in old_file:
    temp_file.write(line.replace(pattern, substr))
  # Close temp file
  temp_file.close()
  close(fh)
  old_file.close()
  # Remove original file
  remove(file_path)
  # Move file
  move(temp_path, file_path)
