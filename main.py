import numpy as np

def handleOOV(occurences):
    for key in list(occurences.keys()):
        if occurences[key] < 3 and key != '<UNK>' and key != '<STOP>':
            occurences.pop(key)
            occurences["<UNK>"]+= 1
    return occurences

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
<<<<<<< Updated upstream

    PerPlexSize = 0
    line1 = "<START> HDTV . <STOP>"
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

    
    total = ( -1 / PerPlexSize) * total
    total = 2 ** total
    return total


def handleOOV(occurences):
    for key in list(occurences.keys()):
        if occurences[key] < 3 and key != '<UNK>' and key != '<STOP>':
            occurences.pop(key)
            occurences["<UNK>"]+= 1
    return occurences
=======
    file_path = "./A2-Data/1b_benchmark.train.tokens"
    f = open(file_path, "r", encoding="utf-8")
    perPlexSize = 0 
    total = 0
    unigram["<START>"] = unigram["<STOP>"]
    # log probability for our unique words in dataset
    # totalWords is entire number of words in dataset including dupes
    prevWord = "<START>"
    for line in f:  
        sentence = list(line.split())
        sentence.append('<STOP>')
        for word in sentence:
            perPlexSize+=1
            if prevWord == "<STOP>":
                prevWord = "<START>"
            elif (word, prevWord) in bigram:
                total += np.log10(bigram[(word, prevWord)]/ unigram[prevWord])
            prevWord = word 

    total = ( -1 / perPlexSize) * total
    perplexity = 10 ** total
    return perplexity
>>>>>>> Stashed changes
        
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

    
    # remove OOV words
<<<<<<< Updated upstream
    occurences = handleOOV(occurences)
    
    print("Number of Occurances:", len(occurences))

    print("Unigram Perplexity:", unigramPP(totalWords,occurences))
=======
    # occurences = handleOOV(occurences)
    
    print("Number of Occurances:", len(occurences))

    #print("Unigram Perplexity:", unigramPP(totalWords,occurences))
    # temp = dict()
    # temp = occurences
    # remove OOV words
    # temp = handleOOV(temp)
    
    # print(len(occurences))

    
>>>>>>> Stashed changes

    f = open(file_path, "r", encoding="utf-8")

    bigram = dict()
    bigram = makebigrams(f)
<<<<<<< Updated upstream

    # i = 0
    # for keys in bigram.keys():
    #     i = i + 1
    #     print(keys)
    #     print(bigram[keys])
    #     if( i == 20):
    #         return
                
=======
   
    print("Bigram Perplexity:", bigramPP(totalWords, bigram, occurences))
    

>>>>>>> Stashed changes
if __name__ == "__main__":
    main()
