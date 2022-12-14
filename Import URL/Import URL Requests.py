from fileinput import filename
from ssl import SSLCertVerificationError, SSLError
import requests
import os.path


# folder = 'Import URL'
# filelocation = os.path.abspath(folder())
# print(filelocation)

# url = ''
# try:
#     req = requests.get(url, timeout=10)
#     print(req.ok, req.status_code)
# except requests.exceptions.ConnectTimeout:
#     print("timeout")

# textfile = 'BROKEN.txt'
# file = open(textfile, 'w')
# file.write('Line 1\n')
# file.write('Line 2\n')
# file.write('Line 3')


textfile = 'URL.txt'
textfile2 = 'BROKEN.txt'
textfile3 = 'WORK.txt'
counter = 0
whilecounter = False
readfile = open(textfile, 'r')
writefileBROKEN = open(textfile2, 'a')
writefileWORK = open(textfile3, 'a')
url = readfile.readlines()

while (whilecounter == False):
    if (url[counter] == 'END'):
        whilecounter = True
    elif whilecounter == False:
        try:
            req = requests.get(url[counter], verify = False, timeout=10)
            writefileWORK.write(url[counter])
            counter = counter + 1
            print('Request success')
        except:
            writefileBROKEN.write(url[counter])
            counter = counter + 1
            print('Timeout')
readfile.close()
writefileWORK.close()
writefileBROKEN.close()
print('END')
