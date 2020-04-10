import sys,subprocess,select,fcntl

def lock():
    this_script_file = open(sys.argv[0], "r")
    this_script_fileno = this_script_file.fileno()
    fcntl.flock(this_script_fileno, fcntl.LOCK_EX)

lock()

class Nc:
  def __init__(self, host, port):
    self.host = host
    self.port = port
    self.popen = subprocess.Popen(["nc", self.host, str(self.port)], 
    					stdin=subprocess.PIPE, 
					stdout=subprocess.PIPE,
					stderr=subprocess.PIPE)
    self.stdinPoll = select.poll()
    self.stdinPoll.register(self.popen.stdin, select.POLLOUT)
    self.stdoutPoll = select.poll()
    self.stdoutPoll.register(self.popen.stdout, select.POLLIN)
    self.stderrPoll = select.poll()
    self.stderrPoll.register(self.popen.stderr, select.POLLIN)
    
  def communicate(self, inBytes = None, timeout = 0):
    if inBytes is not None:
      if len(self.stdinPoll.poll(timeout)) > 0:
        self.popen.stdin.write(inBytes)
        self.popen.stdin.flush()
      
    readFromStdout = []
    while len(self.stdoutPoll.poll(timeout)) > 0:
      readFromStdout.append(self.popen.stdout.readline())

    readFromStderr = []
    while len(self.stderrPoll.poll(timeout)) > 0:
      readFromStderr.append(self.popen.stderr.readline())
    
    return (readFromStdout, readFromStderr)

class Etp(Nc):
  def __init__(self, host = "localhost", port = 21):
    Nc.__init__(self, host, port)

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

etp.welcome()
etp.login()
etp.count(1000)
etp.pathColumn()
etp.search("*.ini")
etp.query()

