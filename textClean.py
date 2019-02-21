import re
import os
import pandas as pd
import string
import random
import subprocess

DATA_PATH_1 = 'data/r/'
DATA_PATH_2 = 'data/d/'
columns = ['user', 'fullname', 'tweet-id', 'timestamp', 'url', 'likes', 'replies', 'retweets', 'text', 'html']

def clean_tweet(tweet):
    apply1 = re.sub(r'http\S+', '', tweet)
    apply2 = re.sub(r'pic.twitter.com\S+', '', apply1)
    apply3 = re.sub(r'@\S+', '', apply2)
    apply4 = re.sub(r'#', '', apply3)
    apply5 = re.sub(r'\n', ' ', apply4)
    apply6 = re.sub(r'[^\w\s]','',apply5)
    return apply6

n = 0
cleaned_data = open('prelim.txt', 'w')
republicans = os.listdir(DATA_PATH_1)
for i, input_file in enumerate(republicans):
    sheet = pd.read_csv(DATA_PATH_1 + input_file, header=0, names=columns)
    for index, row in sheet.iterrows():
        sample_tweet = str(row[columns[8]])
        line = '__label__' + 'r ' + clean_tweet(sample_tweet) + '\n'
        cleaned_data.write(line)
        n = n + 1

democrats = os.listdir(DATA_PATH_2)
for i, input_file in enumerate(democrats):
    sheet = pd.read_csv(DATA_PATH_2 + input_file, header=0, names=columns)
    for index, row in sheet.iterrows():
        sample_tweet = str(row[columns[8]])
        line = '__label__' + 'd ' + clean_tweet(sample_tweet) + '\n'
        cleaned_data.write(line)
        n = n + 1

with open('prelim.txt','r') as source:
    data = [ (random.random(), line) for line in source ]
data.sort()
with open('supervised.txt','w') as target:
    for _, line in data:
        target.write( line )

os.system('head -n ' + str(round(n*0.8)) + ' supervised.txt > supervised.train')
os.system('head -n ' + str(n -round(n*0.8)) + ' supervised.txt > supervised.valid')
subprocess.call(['rm', '-rf', 'prelim.txt'])
subprocess.call(['rm', '-rf', 'supervised.txt'])



