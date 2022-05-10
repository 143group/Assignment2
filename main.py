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


def bigramPP(totalWords, bigram, unigram):
    file_path = "./A2-Data/1b_benchmark.train.tokens"
    f = open(file_path, "r", encoding="utf-8")
    PerPlexSize = 0
    total = 0

    # log probability for our unique words in dataset
    # totalWords is entire number of words in dataset including dupes
    sentence = line1.split()


    unigram["<START>"] = unigram["<STOP>"]
    for i in range(1,len(sentence),1):
        PerPlexSize+= 1
        if((sentence[i], sentence[i-1]) in bigram):
            total += np.log2(bigram[(sentence[i], sentence[i-1])] / unigram[sentence[i-1]])
        else:
            total += np.log2(unigram["<UNK>"]/ totalWords)

    
    total = (-1 / PerPlexSize) * total
    total = 2 ** total
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
                    bigram[(sentence[i], "<START>")] +=1
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

def makeBigram(filepath):
    bigrams = {}
    file = open(filepath, "r", encoding="utf-8")
    for newline in file:
        sentence = "<START> " + newline
        words = list(sentence.split())
        for i in range(1, len(words)):
            bigram = (words[i], words[i-1])
            bigrams[bigram] = 1 + bigrams.get(bigram, 0)
    return bigrams

def makeTrigram(filepath):
    trigrams = {}
    file = open(filepath, "r", encoding="utf-8")
    for newline in file:
        sentence = "<START> <START> " + newline
        words = list(sentence.split())
        for i in range(2, len(words)):
            trigram = (words[i], words[i-2], words[i-1])
            trigrams[trigram] = 1 + trigrams.get(trigram, 0)
    return trigrams

def trigramPP(filepath, trigrams, bigrams, occurances, totalWords):
    probability = 0
    file = open(filepath, "r", encoding="utf-8")
    for newline in file:
        sentence = "<START> <START> " + newline
        words = list(sentence.split())
        for i in range(2, len(words)):
            trigram = (words[i], words[i-2], words[i-1])
            bigram = (words[i-1], words[i-2])
            if trigram in trigrams and bigram in bigrams:
                # print(trigram, ": ", trigrams[trigram], bigram, ": ", bigrams[bigram])
                probability += np.log(trigrams[trigram]/(bigrams[bigram]))

    return np.exp(-(1/totalWords) * probability)

def wordOccur(filepath):
    file = open(filepath, "r", encoding="utf-8")
    occurances = {}
    totalWords = 0
    
    for newline in file:
        sentence = list(newline.split())
        for word in sentence:
            totalWords += 1
            occurances[word] = 1 + occurances.get(word, 0)
    file.close()
    return occurances, totalWords

def replaceUNK(originpath, copypath, occurances):
    replacement = ""
    unknowns, stops = 0,0
    file = open(originpath, "r", encoding="utf-8")
    copy = open(copypath, "w", encoding="utf-8")
    for newline in file:
        for word in newline.split():
            if word in occurances and occurances[word] < 3:
                del occurances[word]
                replacement += "<UNK> "
                unknowns += 1
            else:
                replacement += word + " "
        replacement += "<STOP>\n"
        stops += 1
    copy.seek(0)
    copy.write(replacement)
    copy.truncate()
    file.close()   
    copy.close
    occurances["<UNK>"] = unknowns
    occurances["<STOP>"] = stops
    return unknowns, stops

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
    print("===== Preprocessed Data =====")
    print("Unique Unigram Tokens:", len(occurences))
    print("Unique Bigram Tokens:", )
    print("Unique Trigram Tokens:", )
    print("Total Words:", )


    print("===== Train Data =====")
    print("Unigram Perplexity:", unigramPP(totalWords,occurences))
    # print("Bigram Perplexity:", )
    # print("Trigram Perplexity:", )

    # print("===== Dev Data =====")
    # print("Unigram Perplexity:", )
    # print("Bigram Perplexity:", )
    # print("Trigram Perplexity:", )

    # print("===== Test Data =====")
    # print("Unigram Perplexity:", )
    # print("Bigram Perplexity:", )
    # print("Trigram Perplexity:", )

    occurences = handleOOV(occurences)

    f = open(file_path, "r", encoding="utf-8")

    bigram = dict()
    bigram = makebigrams(f)

    # i = 0
    # for keys in bigram.keys():
    #     i = i + 1
    #     print(keys)
    #     print(bigram[keys])
    #     if( i == 20):
    #         return
                
if __name__ == "__main__":
    main()
