import pandas as pd
import numpy as np
import time
import argparse





def main():
    occurences = dict()

    occurences["<STOP>"] = 0
    occurences["<UNK>"] = 0
    f = open("/Users/jaypatel/Desktop/A2-Data/Assignment2/A2-Data/1b_benchmark.train.tokens", "r")
    for line in f:  
        for word in line.split():
            if word in occurences:
                occurences[word] += 1
            else:
                occurences[word] = 1
            
    for key in list(occurences.keys()):
        if occurences[key] < 3 and key != '<UNK>' and key != '<STOP>':
            occurences.pop(key)
            occurences["<UNK>"]+= 1
       
    print(len(occurences))






if __name__ == "__main__":
    main()
