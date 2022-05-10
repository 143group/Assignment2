def makeBigram(filepath):
    bigrams = {}
    file = open(filepath, "r", encoding="utf-8")
    for newline in file:
        words = list(newline.split())
        for i in range(2, len(words)):
            bigram = (words[i], words[i-1])
            bigrams[bigram] = 1 + bigrams.get(bigram, 0)
    return bigrams

def makeTrigram(filepath):
    trigrams = {}
    file = open(filepath, "r", encoding="utf-8")
    for newline in file:
        words = list(newline.split())
        for i in range(2, len(words)):
            trigram = (words[i], words[i-2], words[i-1])
            trigrams[trigram] = 1 + trigrams.get(trigram, 0)
    return trigrams

def trigramPP(filepath, trigrams, bigrams):
    PerPlexity = 1
    file = open(filepath, "r", encoding="utf-8")
    for newline in file:
        words = list(newline.split())
        for i in range(2, len(words)):
            trigram = (words[i], words[i-2], words[i-1])
            bigram = (words[i-2], words[i-1])
            if trigram not in trigrams or bigram not in bigrams:
                PerPlexity *= 0
            else:
                PerPlexity *= trigrams[trigram]/bigrams[bigram]
    return PerPlexity

def wordOccur(filepath):
    file = open(filepath, "r", encoding="utf-8")
    occurances = {}
    for newline in file:
        sentence = list(newline.split())
        for word in sentence:
            occurances[word] = 1 + occurances.get(word, 0)
    file.close()
    return occurances

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
    origin_path = "./A2-Data/1b_benchmark.train.tokens"
    copy_path = "./A2-Data/1b_benchmark.train_copy.tokens"
    
    print("[MAKING OCCURANCES...]")
    occurances = wordOccur(origin_path)
    print("[OCCURANCES MADE.]\n")

    print("[REPLACING WITH <UNK>...]")
    unknowns, stops = replaceUNK(origin_path, copy_path, occurances)
    print("[REPLACED.]\n")
    
    print("[MAKING BIGRAMS...]")
    bigrams = makeBigram(copy_path)
    print("[BIGRAMS MADE.]\n")

    print("[MAKING TRIGRAMS...]")
    trigrams = makeTrigram(copy_path)
    print("[TRIGRAMS MADE.]\n")

    print("[CALCULATING PERPLEXITY...]")
    perplexity = trigramPP(copy_path, trigrams, bigrams)
    print("[DONE.]\n")

    print("RESULTS: ")
    print("PERPLEXITY: ", perplexity)

if __name__ == "__main__":
    main()