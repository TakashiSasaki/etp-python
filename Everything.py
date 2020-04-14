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
    out, err = self.communicate(None, 1000)
    print(out)
    if out[0] != b'220 Welcome to Everything ETP/FTP\r\n':
      raise RuntimeError("no welcome message")
  
  def login(self):
    out, err = self.communicate(b'USER\n', 100)
    print(out)
    if out[0] != b'230 Logged on.\r\n':
      raise RuntimeError("failed to log-in.")

  def case(self, b = False):
    s = "EVERYTHING CASE {}\n".format("1" if b else "0") 
    b = s.encode("utf8")
    out, err = self.communicate(b, 100)
    print(out)

  def count(self, nCount):
    s = "EVERYTHING COUNT {}\n".format(nCount) 
    b = s.encode("utf8")
    out, err = self.communicate(b, 100)
    print(out)

  def pathColumn(self):
    s = "EVERYTHING PATH_COLUMN 1\n"
    b = s.encode("utf8")
    out, err = self.communicate(b, 100)
    print(out)

  def dateCreatedColumn(self):
    s = "EVERYTHING DATE_CREATED_COLUMN 1\n"
    b = s.encode("utf8")
    out, err = self.communicate(b, 100)
    print(out)
  
  def dateModifiedColumn(self):
    s = "EVERYTHING DATE_MODIFIED_COLUMN 1\n"
    b = s.encode("utf8")
    out, err = self.communicate(b, 100)
    print(out)

  def attributesColumn(self):
    s = "EVERYTHING ATTRIBUTES_COLUMN 1\n"
    b = s.encode("utf8")
    out, err = self.communicate(b, 100)
    print(out)

  def sizeColumn(self):
    s = "EVERYTHING SIZE_COLUMN 1\n"
    b = s.encode("utf8")
    out, err = self.communicate(b, 100)
    print(out)

  def fileListFilenameColumn(self):
    s = "EVERYTHING FILE_LIST_FILENAME_COLUMN 1\n"
    b = s.encode("utf8")
    out, err = self.communicate(b, 100)
    print(out)

  def dateModifiedDescending(self):
    s = "EVERYTHING SORT DATE_MODIFIED_DESCENDING\n"
    b = s.encode("utf8")
    out, err = self.communicate(b, 100)
    print(out)

  def search(self, s):
    s = "EVERYTHING SEARCH {}\n".format(s)
    b = s.encode("utf8")
    out, err = self.communicate(b, 100)
    print(out)

  def query(self):
    s = "EVERYTHING QUERY\n"
    b = s.encode("utf8")
    out, err = self.communicate(b, 4000)
    print(out)


if __name__ == "__main__":
  everything = Everything()
  everything.welcome()
  everything.login()
  everything.count(1000)
  everything.pathColumn()
  everything.dateCreatedColumn()
  everything.dateModifiedColumn()
  everything.sizeColumn()
  #everything.fileListFilenameColumn()
  everything.dateModifiedDescending()
  everything.search("hello txt")
  everything.case(False)
  everything.query()

