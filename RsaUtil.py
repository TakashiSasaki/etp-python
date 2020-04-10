from CommandIo import CommandIo
import os

class RsaUtil(CommandIo):
  def __init__(self):
    pass

  def getPublicKey(self, path):
    commandIo = CommandIo(["ssh-keygen", "-e", "-f" , path, "-m", "pkcs8"])
    out, err = commandIo.communicate(None, 1000)
    return out

if __name__ == "__main__":
  path = os.path.expanduser("~/.ssh/id_rsa.pub")
  rsaUtil = RsaUtil()
  publicKey = rsaUtil.getPublicKey(path)
  print(publicKey)
