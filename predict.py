import os
import sys
import pandas as pd
import re
from pathlib import Path


def clean_tweet(tweet):
    apply1 = re.sub(r'http\S+', '', tweet)
    apply2 = re.sub(r'pic.twitter.com\S+', '', apply1)
    apply3 = re.sub(r'@\S+', '', apply2)
    apply4 = re.sub(r'#', '', apply3)
    apply5 = re.sub(r'\n', ' ', apply4)
    apply6 = re.sub(r'[^\w\s]','',apply5)
    return apply6

user = sys.argv[1]
data_path = 'data/predict/' + user + '.csv'
columns = ['user', 'fullname', 'tweet-id', 'timestamp', 'url', 'likes', 'replies', 'retweets', 'text', 'html']

#scraping for data
if not os.path.isfile(data_path):
    command = 'twitterscraper -u ' + user + ' -l 500 -c -o ' + data_path
    os.system(command)


#putting csv file into readable text file
input = open('input.txt', 'w')
n = 0
predict = pd.read_csv(data_path, header=0, names=columns)
for index, row in predict.iterrows():
    sample_tweet = str(row[columns[8]])
    line = clean_tweet(sample_tweet) + '\n'
    input.write(line)
    n = n + 1

#testing
os.system('./data/fastText/fasttext predict model/model.bin input.txt > determine.txt')
os.system('cd ../..')
determine = open('determine.txt', 'r')
result = determine.readlines()
r = float(0)
n = len(result)
for i in range(len(result)):
    if result[i] == '__label__r\n':
        r = r + 1
if(r/n > 0.5):
    print('This twitter leans right with ' + str(r/n) + ' certainty.')
else:
    print('This twitter leans left with ' + str(1 - r/n) + ' certainty.')
os.system('rm input.txt')
os.system('rm determine.txt')





