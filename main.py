# import pandas as pd
from cmath import inf
import numpy as np

def unigramPP(totalWords, occurences, file_path, alpha):
    f = open(file_path, "r", encoding="utf-8")
    PerPlexSize = 0
    total = 0
    # log probability for our unique words in dataset
    # totalWords is entire number of words in dataset including dupes
    for line in f:  
        sentence = list(line.split())
        sentence.append("<STOP>")
        for i in range(len(sentence)):
            PerPlexSize+= 1
            if sentence[i] in occurences:
                total += np.log2((occurences[sentence[i]] + alpha)
                                / 
                                (totalWords + (len(occurences) * alpha)))
            else:
                total += np.log2((occurences["<UNK>"] + alpha)/ (totalWords + (len(occurences) * alpha)))


    total = (-1 / PerPlexSize) * total
    total = 2 ** total
    return total

def bigramPP(totalWords, bigram, occurences, file_path, alpha):
    f = open(file_path, "r", encoding="utf-8")
    PerPlexSize = 0
    
    total = 0
    occurences["<START>"] = occurences["<STOP>"]
    #log probability for our unique words in dataset
    #totalWords is entire number of words in dataset including dupes
    for line in f:  
        sentence = list(line.split())
        sentence.append("<STOP>")
        for i in range(0,len(sentence),1):
            PerPlexSize+=1
            if i == 0:
                if (sentence[i], "<START>") in bigram:
                    total += np.log10((bigram[(sentence[i], "<START>")] + alpha) 
                                        /
                                        (occurences["<START>"] + (26602 * alpha)))
                elif alpha == 0 and (sentence[i], "<START>") not in bigram:  
                    return inf                       
            elif (sentence[i],sentence[i-1]) in bigram:
                total += np.log10( (bigram[(sentence[i], sentence[i-1])] + alpha)
                                    / 
                                    (occurences[sentence[i-1]] + (26602 * alpha) ) )
            elif alpha == 0 and (sentence[i],sentence[i-1]) not in bigram:
                return inf
            elif alpha > 0:
                total += np.log10( (alpha)
                                    / 
                                    (26602 * alpha) )


    total = ( -1 / PerPlexSize) * total
    total = 10 ** total
    return total


def trigramPP(totalWords, trigrams, bigrams, file_path, alpha, unigrams):
    f = open(file_path, "r", encoding="utf-8")
    perPlexSize = 0
    total = 0
    for line in f:
        sentence = list(("<START> <START> " + line + " <STOP>").split())
        for i in range(2, len(sentence)):
            perPlexSize += 1
            trigram = (sentence[i], sentence[i-2], sentence[i-1])
            if trigram in trigrams:
                bigram = (sentence[i-1], sentence[i-2])
                if bigram == ('<START>','<START>'):
                    total += np.log10((trigrams[trigram] + alpha )/ ( unigrams["<STOP>"] + (26602 * alpha)))
                else:
                    total += np.log10((trigrams[trigram] + alpha )/ ( bigrams[(sentence[i-1], sentence[i-2])] + (26602 * alpha)))
            elif alpha == 0:
                return inf
            elif alpha > 0:
                total += np.log10( (alpha) / (26602 * alpha))
    total = (-1 / perPlexSize) * total
    perplexity = 10 ** total
    return perplexity


def linearinterpolation(totalWords, trigrams, bigrams, file_path, unigrams):
    f = open(file_path, "r", encoding="utf-8")
    perPlexSize = 0
    total = 0
    unigrams["<START>"] = unigrams["<STOP>"]
    for line in f:
        sentence = list(("<START> " + line + " <STOP>").split())
        for i in range(1, len(sentence)):
            uni, bi, tri = 0, 0, 0 
            perPlexSize += 1
            unigram = sentence[i]
            bigram = (sentence[i], sentence[i-1])

            # get unigram, bigram, trigram perplexities
            if unigram in unigrams:
                uni = (unigrams[unigram]) / totalWords
            else:
                uni = unigrams["<UNK>"] / totalWords

            if bigram in bigrams and sentence[i-1] in unigrams:
                bi = (bigrams[bigram]) / (unigrams[sentence[i-1]]) 
                tri = bi
            if i > 1:
                trigram = (sentence[i], sentence[i-2], sentence[i-1])
                if trigram in trigrams and (sentence[i-1], sentence[i-2]) in bigrams:
                    tri = (trigrams[trigram]) / bigrams[(sentence[i-1], sentence[i-2])]
            if uni > 0: uni = np.log2(uni) * 0.1
            if bi > 0: bi = np.log2(bi) * 0.3
            if tri > 0: tri = np.log2(tri) * 0.6
            total += (uni + bi + tri)
    total = (-1 / totalWords) * total
    perplexity = 2 ** total
    return perplexity          

def handleOOV(occurences):
    for key in list(occurences.keys()):
        if occurences[key] < 3 and key != '<UNK>' and key != '<STOP>':
            increment = occurences[key]
            occurences.pop(key)
            occurences["<UNK>"]+= increment
    return occurences


def makeunigrams():
    occurences = dict()
    totalWords = 0
    occurences["<STOP>"] = 0
    occurences["<UNK>"] = 0
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
    return occurences, totalWords

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

def maketrigrams(f, bigrams):
    trigrams = dict()
    for newline in f:  
        sentence = list(newline.split())
        for i in range(len(sentence)):
            if i == 0:
                trigram = (sentence[i], "<START>", "<START>")
                if trigram in trigrams:
                    trigrams[trigram] += 1
                else:
                    trigrams[trigram] = bigrams[(sentence[i], "<START>")]
                continue
            # check if the second P(word | <START>, prevword ) exists or not
            if i == 1:
                trigram = (sentence[i], "<START>", sentence[i-1])
            # if we are on the last word, we want to add P(STOP | preprevword, prevword)
            elif i == len(sentence) - 1:
                trigram = ("<STOP>", sentence[i-1], sentence[i])
                trigrams[trigram] = 1 + trigrams.get(trigram, 0)
                trigram = (sentence[i], sentence[i-2], sentence[i-1])
            # if not in any of the two above scenarios, just add in regular trigrams with curr and previous word
            else:
                trigram = (sentence[i], sentence[i-2], sentence[i-1])
            trigrams[trigram] = 1 + trigrams.get(trigram, 0)
    return trigrams
 
def getPerplexity(file_path, totalWords, trigrams, bigrams, original, temp, alpha):
    print("Unigram Perplexity:", unigramPP(totalWords, temp, file_path, alpha))
    print("Bigram Perplexity:", bigramPP(totalWords, bigrams, original, file_path, alpha))
    print("Trigram Perplexity:", trigramPP(totalWords, trigrams, bigrams, file_path, alpha, original))
    #print("Interpolation Perplexity:", linearinterpolation(totalWords, trigrams, bigrams, file_path, temp))

def main():

    occurences = dict()
    totalWords = 0
    occurences["<STOP>"] = 0
    occurences["<UNK>"] = 0
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
    file_path = "A2-Data/1b_benchmark.train.tokens"
    original = occurences.copy()
    #remove OOV words
    temp = handleOOV(occurences)
    
    f = open(file_path, "r", encoding="utf-8")
    bigrams = makebigrams(f)


    f = open(file_path, "r", encoding="utf-8")
    trigrams = maketrigrams(f, bigrams)
    
    trainPath = "./A2-Data/1b_benchmark.train.tokens"
    devPath = "./A2-Data/1b_benchmark.dev.tokens"
    testPath = "./A2-Data/1b_benchmark.test.tokens"

    print("===== Train Data =====")
    getPerplexity(trainPath, totalWords, trigrams, bigrams, original, temp, 1)
    print("===== Dev Data =====")
    getPerplexity(devPath, totalWords, trigrams, bigrams, original, temp, 1)
    print("===== Test Data =====")
    getPerplexity(testPath, totalWords, trigrams, bigrams, original, temp, 1)
if __name__ == "__main__":
    main()