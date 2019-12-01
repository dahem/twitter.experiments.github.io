import os
import time
from twitter import save_twiter_request 
import csv

def get_key_list():
    ans = []
    with open('./searchWords.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ans.append(row['keylist'])
    return ans

def main():
    key_list = get_key_list()
    len_keys = len(key_list)
    ind = 0 
    TIME_IN_SECONDS = 60
    while True:
        save_twiter_request(key_list[ind % len_keys])
        ind += 1 
        time.sleep(TIME_IN_SECONDS)


if __name__ == '__main__':
    main()