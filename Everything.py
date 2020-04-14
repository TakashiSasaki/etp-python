import sys,subprocess,select,fcntl
from CommandIo.CommandIo import CommandIo

def lock():
    this_script_file = open(sys.argv[0], "r")
    this_script_fileno = this_script_file.fileno()
    fcntl.flock(this_script_fileno, fcntl.LOCK_EX)

lock()

class Everything(CommandIo):
  def __init__(self, host = "localhost", port = 21):
    CommandIo.__init__(self, ["nc", host, str(port)])

  def welcome(self):
    out = self.readlines(1, 10)
    print(out)
    if out[0] != b'220 Welcome to Everything ETP/FTP\r\n':
      raise RuntimeError("no welcome message")
  
  def login(self):
    self.write(b'USER\n')
    out = self.readlines(1, 10)
    print(out)
    if out[0] != b'230 Logged on.\r\n':
      raise RuntimeError("failed to log-in.")

  def case(self, b:bool):
    s = "EVERYTHING CASE {}\n".format("1" if b else "0") 
    b = s.encode("utf8")
    self.write(b)
    out = self.readlines(1, 10)
    print(out)

  def count(self, nCount):
    s = "EVERYTHING COUNT {}\n".format(nCount) 
    b = s.encode("utf8")
    self.write(b)
    out = self.readlines(1, 10)
    print(out)

  def pathColumn(self, b:bool):
    s = "EVERYTHING PATH_COLUMN {}\n".format("1" if b else "0")
    b = s.encode("utf8")
    self.write(b)
    out = self.readlines(1, 10)
    print(out)

  def dateCreatedColumn(self, b:bool):
    s = "EVERYTHING DATE_CREATED_COLUMN {}\n".format("1" if b else "0")
    b = s.encode("utf8")
    self.write(b)
    out = self.readlines(1, 10)
    print(out)
  
  def dateModifiedColumn(self, b:bool):
    s = "EVERYTHING DATE_MODIFIED_COLUMN {}\n".format("1" if b else "0")
    b = s.encode("utf8")
    self.write(b)
    out = self.readlines(1, 10)
    print(out)

  def attributesColumn(self, b:bool):
    s = "EVERYTHING ATTRIBUTES_COLUMN {}\n".format("1" if b else "0")
    b = s.encode("utf8")
    self.write(b)
    out = self.readlines(1, 10)
    print(out)

  def sizeColumn(self, b:bool):
    s = "EVERYTHING SIZE_COLUMN {}\n".format("1" if b else "0")
    b = s.encode("utf8")
    self.write(b)
    out = self.readlines(1, 10)
    print(out)

  def fileListFilenameColumn(self, b:bool):
    s = "EVERYTHING FILE_LIST_FILENAME_COLUMN {}\n".format("1" if b else "0")
    b = s.encode("utf8")
    self.write(b)
    out = self.readlines(1, 10)
    print(out)

  def dateModifiedDescending(self):
    s = "EVERYTHING SORT DATE_MODIFIED_DESCENDING\n"
    b = s.encode("utf8")
    self.write(b)
    out = self.readlines(1, 10)
    print(out)

  def search(self, s):
    s = "EVERYTHING SEARCH {}\n".format(s)
    b = s.encode("utf8")
    self.write(b)
    out = self.readlines(1, 10)
    print(out)

  def query(self):
    s = "EVERYTHING QUERY\n"
    b = s.encode("utf8")
    self.write(b)
    out = self.readlines(1, 1000)
    print(out)
    out = self.readlines(10000, 100)
    print(out)
  
  def wholeWord(self, b:bool):
    s = "EVERYTHING WHOLE_WORD {}\n".format("1" if b else "0")
    b = s.encode("utf8")
    out = self.readlines(1, 10)
    print(out)


if __name__ == "__main__":
  everything = Everything()
  everything.welcome()
  everything.login()
  everything.count(10)
  everything.pathColumn(True)
  everything.dateCreatedColumn(True)
  everything.dateModifiedColumn(True)
  everything.sizeColumn(True)
  everything.fileListFilenameColumn(True)
  everything.dateModifiedDescending()
  everything.search("id_rsa.pub")
  everything.case(False)
  everything.query()

