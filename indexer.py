#!/usr/bin/env python
from util import get_data_without_tags, parse_data_into_words, store_to_ds, store_to_file
from bs4 import BeautifulSoup
import sys
import os
import re
import pickle


map = {}
def main():
    # TODO: complete to generate a index and write to a file index.dat
    # Remember index.dat should be reloadable
    # for each file in target dir
    if len(sys.argv) != 3:
        print "Wrong info passed"
        sys.exit(1)

    global map
    target_dir = sys.argv[1]
    result = sys.argv[2]
    files = os.listdir(target_dir)

    for file in files:     
    	## get the file data without tags
        with open(target_dir + '/' + file,"r") as f:
            data = get_data_without_tags("\n".join(f.readlines()[2:]))
            words =  parse_data_into_words(data)
            store_to_ds(words, file, map)
    store_to_file(result, map)
  

if __name__ == "__main__":
    main()
