import numpy as np

def makeBigram(filepath):
    bigrams = {}
    file = open(filepath, "r", encoding="utf-8")
    for newline in file:
        sentence = "<START> " + newline + " <STOP>"
        words = list(sentence.split())
        for i in range(2, len(words)):
            bigram = (words[i], words[i-1])
            bigrams[bigram] = 1 + bigrams.get(bigram, 0)
    return bigrams

def makeTrigram(filepath):
    trigrams = {}
    file = open(filepath, "r", encoding="utf-8")
    for newline in file:
        sentence = "<START> <START> " + newline + " <STOP>"
        words = list(sentence.split())
        for i in range(2, len(words)):
            trigram = (words[i], words[i-2], words[i-1])
            trigrams[trigram] = 1 + trigrams.get(trigram, 0)
    return trigrams

def trigramPP(filepath, trigrams, bigrams, totalWords):
    perplexSize= 0
    total = 0

    file = open(filepath, "r", encoding="utf-8")
    for newline in file:
        sentence = "<START> <START> " + newline + " <STOP>"
        words = list(sentence.split())
        for i in range(2, len(words)):
            perplexSize += 1
            trigram = (words[i], words[i-2], words[i-1])
            bigram = (words[i-2], words[i-1])
            if trigram in trigrams and bigram in bigrams:
                total += np.log10(trigrams[trigram] / bigrams[bigram])
    total = (-1 / perplexSize) * total
    return 10 ** total


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
            if occurances[word] < 3:
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
    return unknowns, stops

def main():
    train_path = "./A2-Data/1b_benchmark.train.tokens"
    test_path = "./A2-Data/1b_benchmark.test.tokens"
    dev_path = "./A2-Data/1b_benchmark.dev.tokens"
    # copy_path = "./A2-Data/1b_benchmark.train_copy.tokens"
    
    print("[MAKING OCCURANCES...]")
    occurances, totalWords = wordOccur(train_path)
    print("[OCCURANCES MADE.]\n")

    # print("[REPLACING WITH <UNK>...]")
    # unknowns, stops = replaceUNK(origin_path, copy_path, occurances)
    # print("[REPLACED.]\n")
    
    print("[MAKING BIGRAMS...]")
    bigrams = makeBigram(train_path)
    print("[BIGRAMS MADE.]\n")

    print("[MAKING TRIGRAMS...]")
    trigrams = makeTrigram(train_path)
    print("[TRIGRAMS MADE.]\n")

    print("[CALCULATING TRAIN PERPLEXITY...]")
    trainPP= trigramPP(train_path, trigrams, bigrams, totalWords)
    print("[DONE.]\n")

    print("[CALCULATING TEST PERPLEXITY...]")
    testPP= trigramPP(test_path, trigrams, bigrams, totalWords)
    print("[DONE.]\n")

    print("[CALCULATING DEV PERPLEXITY...]")
    devPP= trigramPP(dev_path, trigrams, bigrams, totalWords)
    print("[DONE.]\n")

    print("RESULTS: ")
    print("TRAIN PERPLEXITY: ", trainPP)
    print("TEST PERPLEXITY: ", testPP)
    print("DEV PERPLEXITY: ", devPP)

if __name__ == "__main__":
    main()