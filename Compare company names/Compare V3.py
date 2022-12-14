from fuzzywuzzy import fuzz, process
import time
# Imports ^

with open('TCN.txt') as f:
    trackers = f.read().split('\n')
with open('CCC.txt') as f:
    company = f.read().split('\n')
# Reads both files and assigns arrays ^

whiletrue = False
counter = 0

while (whiletrue == False):
    companyname = str(company[counter])
    if company[counter] == 'END':
        whiletrue = True
        print('END')
    else:
        checkforrelevancy = process.extractOne(company[counter], trackers)
        print(companyname)
        print(checkforrelevancy)
        if checkforrelevancy[1] >= 90:
            print('Blatant, skipping field')
        else:
            with open('FINISH.txt', 'a') as f:
                f.write('------------------------------------')
                f.write('\n')
                f.write('With company name ' + companyname + ', there are 4 similarities: ')
                f.write('\n')
                f.write(str(process.extract(company[counter], trackers, limit = 4)))
                f.write('\n')
        counter = counter + 1