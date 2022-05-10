import numpy as np

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
    training_path = "./A2-Data/1b_benchmark.train.tokens"
    train_path = "./A2-Data/1b_benchmark.train_copy.tokens"
    
    print("[MAKING OCCURANCES...]")
    occurances, totalWords = wordOccur(training_path)
    print("[OCCURANCES MADE.]\n")

    print("[REPLACING WITH <UNK>...]")
    unknowns, stops = replaceUNK(training_path, train_path, occurances)
    print("[REPLACED.]\n")

    print("NUMBER OF UNIQUE TOKENS: ", len(occurances), "\n")
    
    print("[MAKING BIGRAMS...]")
    bigrams = makeBigram(train_path)
    print("[BIGRAMS MADE.]\n")

    print("[MAKING TRIGRAMS...]")
    trigrams = makeTrigram(train_path)
    print("[TRIGRAMS MADE.]\n")

    tmp = list(trigrams.keys())
    for i in range(10):
        print(tmp[i])

    print("[CALCULATING TRAIN PERPLEXITY...]")
    trainPP= trigramPP(train_path, trigrams, bigrams, occurances, totalWords)
    print("[DONE.]\n")

    # print("[CALCULATING TEST PERPLEXITY...]")
    # testPP= trigramPP(test_path, trigrams, bigrams, totalWords)
    # print("[DONE.]\n")

    # print("[CALCULATING DEV PERPLEXITY...]")
    # devPP= trigramPP(dev_path, trigrams, bigrams, totalWords)
    # print("[DONE.]\n")

    print("RESULTS: ")
    print("TRAIN PERPLEXITY: ", trainPP)
    # print("TEST PERPLEXITY: ", testPP)
    # print("DEV PERPLEXITY: ", devPP)

if __name__ == "__main__":
    main()