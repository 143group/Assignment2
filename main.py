# import pandas as pd
import numpy as np

def unigramPP(totalWords, occurences):
    file_path = "./A2-Data/1b_benchmark.train.tokens"
    f = open(file_path, "r", encoding="utf-8")
    PerPlexSize = 0
    total = 0
    # log probability for our unique words in dataset
    # totalWords is entire number of words in dataset including dupes
    for line in f:  
        sentence = list(line.split())
        sentence.append('<STOP>')
        for i in range(len(sentence)):
            PerPlexSize+= 1
            if sentence[i] in occurences:
                total += np.log2(occurences[sentence[i]]/ totalWords)
            else:
                total += np.log2(occurences["<UNK>"]/ totalWords)


    total = (-1 / PerPlexSize) * total
    total = 2 ** total
    return round(total)


def bigramPP(totalWords, bigram, occurences):

    file_path = "./A2-Data/1b_benchmark.train.tokens"
    f = open(file_path, "r", encoding="utf-8")
    PerPlexSize = 0
    
    total = 0
    occurences["<START>"] = occurences["<STOP>"]
    #log probability for our unique words in dataset
    #totalWords is entire number of words in dataset including dupes
    for line in f:  
        sentence = list(line.split())
        sentence.append('<STOP>')
        for i in range(0,len(sentence),1):
            PerPlexSize+=1
            if i == 0 and (sentence[i], "<START>") in bigram:
                total += np.log10(bigram[(sentence[i], "<START>")]/ occurences["<START>"])

            elif (sentence[i],sentence[i-1]) in bigram:
                total += np.log10(bigram[(sentence[i], sentence[i-1])]/ occurences[sentence[i-1]])

    total = ( -1 / PerPlexSize) * total
    total = 10 ** total
    return total


def handleOOV(occurences):
    for key in list(occurences.keys()):
        if occurences[key] < 3 and key != '<UNK>' and key != '<STOP>':
            occurences.pop(key)
            occurences["<UNK>"]+= 1
    return occurences
        
def makebigrams(f):
    bigram = dict()
    for newline in f:  
        sentence = list(newline.split())
        for i in range(len(sentence)):
             # check if the first P(word | <START> ) exists or not
            if i == 0:
                if (sentence[i], "<START>") in bigram:
                    bigram[(sentence[i], "<START>")] += 1
                else:
                    bigram[(sentence[i], "<START>")] = 1

            # if we are on the last word, we want to add P(STOP | word)
            elif i == len(sentence) - 1:
                if (sentence[i], sentence[i - 1]) in bigram:
                    bigram[(sentence[i],sentence[i - 1])] +=1
                else:
                    bigram[(sentence[i], sentence[i - 1])] = 1
                
                if("<STOP>", sentence[i]) in bigram:
                    bigram[("<STOP>", sentence[i])] += 1
                else:
                    bigram[("<STOP>", sentence[i])] = 1

            # if not in any of the two above scenarios, just add in regular bigram with curr and previous word
            else:
                if (sentence[i], sentence[i - 1]) in bigram:
                    bigram[(sentence[i],sentence[i - 1])] += 1
                else:
                    bigram[(sentence[i], sentence[i - 1])] = 1
    return bigram



def main():
    occurences = dict()
    totalWords = 0
    occurences["<STOP>"] = 0
    occurences["<UNK>"] = 0
    total = 0
    file_path = "./A2-Data/1b_benchmark.train.tokens"
    f = open(file_path, "r", encoding="utf-8")

    # iterate over each sentence
    for line in f:  
        occurences["<STOP>"] += 1
        totalWords += 1
        # for each word in the sentence, check if it exists in dictionary 
        for word in line.split():
            totalWords += 1
            if word in occurences:
                occurences[word] += 1
            else:
                occurences[word] = 1

    
    # remove OOV words
    #occurences = handleOOV(occurences)
    
    print("Number of Occurances:", len(occurences))

    #print("Unigram Perplexity:", unigramPP(totalWords,occurences))
    temp = dict()
    temp = occurences
    #remove OOV words
    #temp = handleOOV(temp)
    
   # print(len(occurences))

    

    f = open(file_path, "r", encoding="utf-8")

    bigram = dict()
    bigram = makebigrams(f)

        
   
    print(bigramPP(totalWords, bigram, occurences))
    

                
if __name__ == "__main__":
    main()
