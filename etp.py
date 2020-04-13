import sys,subprocess,select,fcntl
from CommandIo.CommandIo import CommandIo
print(CommandIo)

def lock():
    this_script_file = open(sys.argv[0], "r")
    this_script_fileno = this_script_file.fileno()
    fcntl.flock(this_script_fileno, fcntl.LOCK_EX)

lock()

class Etp(CommandIo):
  def __init__(self, host = "localhost", port = 21):
    CommandIo.__init__(self, ["nc", host, str(port)])

  def welcome(self):
    out, err = self.communicate(None, 100)
    print(out)
    if out[0] != b'220 Welcome to Everything ETP/FTP\r\n':
      raise RuntimeError("no welcome message")
  
  def login(self):
    out, err = self.communicate(b'USER\n', 100)
    print(out)
    if out[0] != b'230 Logged on.\r\n':
      raise RuntimeError("failed to log-in.")

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
  
  def search(self, s):
    s = "EVERYTHING SEARCH {}\n".format(s)
    b = s.encode("utf8")
    out, err = self.communicate(b, 100)
    print(out)

  def query(self):
    s = "EVERYTHING QUERY\n"
    b = s.encode("utf8")
    out, err = self.communicate(b, 5000)
    print(out)

etp = Etp()
etp.welcome()
etp.login()
etp.count(1000)
etp.pathColumn()
etp.search("*.ini")
etp.query()

