from ftplib import FTP
import os

class myftp:
    ftp=FTP()

    def __init__(self,host,port=21):
        self.ftp.connect(host,port)

    def login(self,username,pwd):
        self.ftp.set_debuglevel(2)
        self.ftp.login(username,pwd)
        print(self.ftp.welcome)

    def oslist():
        

    def close(self):
        self.ftp.set_debuglevel(0)
        self.ftp.quit()


if __name__ == '__main__':
    ftp=myftp('host')
    ftp.login('','')
    ftp.