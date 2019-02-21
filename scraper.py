import subprocess

republicans  = open('data/r.txt', 'r')
rList = republicans.readlines()
rCommands = open('rCommands.txt', 'w')
democrats  = open('data/d.txt', 'r')
dList = democrats.readlines()
dCommands = open('dCommands.txt', 'w')

for i in range(len(rList)):
    rList[i] = rList[i][:-1]
    name_of_file = 'data/r/' + rList[i] + '.csv'
    rCommands.write('twitterscraper -u ' + rList[i] + ' -l 500 -c -o ' + name_of_file + '\n')

for i in range(len(dList)):
    dList[i] = dList[i][:-1]
    name_of_file = 'data/d/' + dList[i] + '.csv'
    dCommands.write('twitterscraper -u ' + dList[i] + ' -l 500 -c -o ' + name_of_file + '\n')