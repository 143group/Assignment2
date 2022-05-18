Group Members:

- John Le
- Chen Kai Zhang
- Jay Patel
- Brad Byun

# Problem 1: Programming n-gram language modeling

For our procedure, when taking the probability of the unigrams, we would take the total count of the words over all words. As for bigram, we would take the count of the the word occurring in succession after the previous word, over the count of the previous word. And for trigram, we did the same, except with the count of the word occurring in succession after the two previous words, over the count of the two previous words. We stored all of these in a dictionary in their respective n-grams.

We then took the total summation of the log of the probability of the n-gram for each word in a sentence, multiplied by 1 over the total number of words in the corpus. Then finding perplety of the n-gram was having the log base to the power of the total.

**1. Report the perplexity scores of the unigram, bigram, and trigram language models for your training, development, and test sets. Briefly discuss the experimental results.**

```
===== Train Data =====
Unigram Perplexity: 976.5437422251438
Bigram Perplexity: inf
Trigram Perplexity: inf
===== Dev Data =====
Unigram Perplexity: 892.2466475165686
Bigram Perplexity: inf
Trigram Perplexity: inf
===== Test Data =====
Unigram Perplexity: 896.4994914385062
Bigram Perplexity: inf
Trigram Perplexity: inf
```

# Problem 2: Additive smoothing

**1. For additive smoothing with α = 1, report the perplexity scores of the unigram, bigram, and trigram language models for your training, and development sets.**

```
===== Train Data =====
Unigram Perplexity: 977.5079364805702
Bigram Perplexity: 1334.4325432826663
Trigram Perplexity: 7212.499816031937
===== Dev Data =====
Unigram Perplexity: 894.3907520465264
Bigram Perplexity: 2309.799385059791
Trigram Perplexity: 12097.912929168193
===== Test Data =====
Unigram Perplexity: 898.5567420819071
Bigram Perplexity: 2292.344750171113
Trigram Perplexity: 12041.311117634672
```

**2. Repeat for two other values of α > 0 of your choosing.**


For α = 2:
```
===== Train Data =====
Unigram Perplexity: 979.9251974597048
Bigram Perplexity: 1935.7095670324397
Trigram Perplexity: 10292.013753150293
===== Dev Data =====
Unigram Perplexity: 897.6601133019157
Bigram Perplexity: 3112.7486345941047
Trigram Perplexity: 14090.152437942645
===== Test Data =====
Unigram Perplexity: 901.7619544790897
Bigram Perplexity: 3090.9996411543466
Trigram Perplexity: 14032.515400181412
```

For α = 3:
```
===== Train Data =====
Unigram Perplexity: 983.3398949724618
Bigram Perplexity: 2385.296469990075
Trigram Perplexity: 12155.613420887077
===== Dev Data =====
Unigram Perplexity: 901.7052966189376
Bigram Perplexity: 3710.1765289044642
Trigram Perplexity: 15272.0588188918
===== Test Data =====
Unigram Perplexity: 905.7584606411255
Bigram Perplexity: 3685.511442763651
Trigram Perplexity: 15214.076489832418
```

**3. Report the perplexity scores for best values of the hyperparameters for the unigram, bigram, and trigram language models on the test set. Remember to pick the best values of the hyperparameters for each model using the dev set, not the test set. Briefly discuss your results.**

The best value of the hyperparameter seems to be when α = 1, as α begins to increase the perplexities only rise more and more. Could not find out the bug causing this to happen.

```
===== Train Data =====
Unigram Perplexity: 977.5079364805702
Bigram Perplexity: 1334.4325432826663
Trigram Perplexity: 7212.499816031937
===== Dev Data =====
Unigram Perplexity: 894.3907520465264
Bigram Perplexity: 2309.799385059791
Trigram Perplexity: 12097.912929168193
===== Test Data =====
Unigram Perplexity: 898.5567420819071
Bigram Perplexity: 2292.344750171113
Trigram Perplexity: 12041.311117634672
```

# Problem 3: Smoothing with linear interpolation

**1. Report perplexity scores on training and development sets for various values of λ1, λ2, λ3. Report no more than 5 different sets of λ’s. In addition to this, report the training and development perplexity for the values λ1 = 0.1, λ2 = 0.3, λ3 = 0.6.**

λ1 = 0.1, λ2 = 0.3, λ3 = 0.6
```
===== Train Data =====
Interpolation Perplexity: 22.258379084771605
===== Dev Data =====
Interpolation Perplexity: 8.200522182425297
```

λ1 = 0.2, λ2 = 0.3, λ3 = 0.5
```
===== Train Data =====
Interpolation Perplexity: 36.73147495510786
===== Dev Data =====
Interpolation Perplexity: 14.817863336170353
```

λ1 = 0.1, λ2 = 0.2, λ3 = 0.7
```
===== Train Data =====
Interpolation Perplexity: 17.468613019481996
===== Dev Data =====
Interpolation Perplexity: 6.635756098720184
```

λ1 = 0.05, λ2 = 0.3, λ3 = 0.65
```
===== Train Data =====
Interpolation Perplexity: 17.326909939922622
===== Dev Data =====
Interpolation Perplexity: 6.100556716259455
```

**2. Putting it all together, report perplexity on the test set, using the hyperparameters that you chose from the development set. Specify those hyperparameters.**

λ1 = 0.1, λ2 = 0.3, λ3 = 0.6
```
===== Test Data =====
Interpolation Perplexity: 8.231494227040557
```

λ1 = 0.2, λ2 = 0.3, λ3 = 0.5
```
===== Test Data =====
Interpolation Perplexity: 14.876599983296668
```

λ1 = 0.1, λ2 = 0.2, λ3 = 0.7
```
===== Test Data =====
Interpolation Perplexity: 6.659282598458705
```

λ1 = 0.05, λ2 = 0.3, λ3 = 0.65
```
===== Test Data =====
Interpolation Perplexity: 6.123026995749869
```

**3. If you use half of the training data, would it increase or decrease the perplexity on previously unseen data? Why? Provide empirical experimental evidence if necessary.**

It should decrease the perplexity. The reason being is if there is less training data, there would likely be more words that appear less than 3 times, since there's less data for it to have a chance to appear in. Thus, there would be more <unk> tokens, and if there are more <unk> tokens, that means there would be a smaller amount of types, since all of the tokens that appear less than 3 (which would be a greater proportion with less data) all fall unders <unk>. Thus there would be a decrease in perplexity.

**4.If you convert all tokens that appeared less then 5 times to <unk> (a special symbol for out-of-vocabulary tokens), would it increase or decrease the perplexity on the previously unseen data compared to an approach that converts only a fraction of words that appeared just once to <unk>? Why? Provide empirical experimental evidence if necessary.**

It should result in an decrease in perplexity. The reason being that if a token needs to appear more times for it to not be converted into <unk>, there will be more <unk> tokens, and as per the explanation in number 3 would result in a decrease in perplexity.
