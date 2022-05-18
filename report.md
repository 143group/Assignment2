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
Bigram Perplexity: 1945.2127338217174
Trigram Perplexity: 7212.6147593507685
===== Dev Data =====
Unigram Perplexity: 894.3902098296883
Bigram Perplexity: 2381.4513500009934
Trigram Perplexity: 12097.9265992677
===== Test Data =====
Unigram Perplexity: 898.556197339652
Bigram Perplexity: 2367.017041419381
Trigram Perplexity: 12041.311117634672
```

**2. Repeat for two other values of α > 0 of your choosing.**


For α = 2:
```
===== Train Data =====
Unigram Perplexity: 979.9251974597048
Bigram Perplexity: 2854.734167436604
Trigram Perplexity: 10292.111205610467
===== Dev Data =====
Unigram Perplexity: 897.65904217758
Bigram Perplexity: 3212.486036844813
Trigram Perplexity: 14090.165899158821
===== Test Data =====
Unigram Perplexity: 901.7608784601948
Bigram Perplexity: 3194.988400960591
Trigram Perplexity: 14032.515400181412
```

For α = 3:
```
===== Train Data =====
Unigram Perplexity: 983.3398949724618
Bigram Perplexity: 3534.676255300601
Trigram Perplexity: 12155.695989413105
===== Dev Data =====
Unigram Perplexity: 901.7037079050183
Bigram Perplexity: 3830.638876108767
Trigram Perplexity: 15272.07145764114
===== Test Data =====
Unigram Perplexity: 905.756864786023
Bigram Perplexity: 3811.1433546887743
Trigram Perplexity: 15214.076489832418
```

**3. Report the perplexity scores for best values of the hyperparameters for the unigram, bigram, and trigram language models on the test set. Remember to pick the best values of the hyperparameters for each model using the dev set, not the test set. Briefly discuss your results.**

The best value of the hyperparameter seems to be when α = 1, as α begins to increase the perplexities only rise more and more. Could not find out the bug causing this to happen.

```
===== Train Data =====
Unigram Perplexity: 977.5079364805702
Bigram Perplexity: 1945.2127338217174
Trigram Perplexity: 7212.6147593507685
===== Dev Data =====
Unigram Perplexity: 894.3902098296883
Bigram Perplexity: 2381.4513500009934
Trigram Perplexity: 12097.9265992677
===== Test Data =====
Unigram Perplexity: 898.556197339652
Bigram Perplexity: 2367.017041419381
Trigram Perplexity: 12041.311117634672
```

# Problem 3: Smoothing with linear interpolation

λ

**1. Report perplexity scores on training and development sets for various values of λ1, λ2, λ3. Report no more than 5 different sets of λ’s. In addition to this, report the training and development perplexity for the values λ1 = 0.1, λ2 = 0.3, λ3 = 0.6.**

λ1 = 0.1, λ2 = 0.3, λ3 = 0.6
```
===== Train Data =====
Interpolation Perplexity: 22.258462641689402
===== Dev Data =====
Interpolation Perplexity: 1.8891254558212154
```

λ1 = 0.2, λ2 = 0.3, λ3 = 0.5
```
===== Train Data =====
Interpolation Perplexity: 36.73158986194293
===== Dev Data =====
Interpolation Perplexity: 2.049248898124556
```

λ1 = 0.1, λ2 = 0.2, λ3 = 0.7
```
===== Train Data =====
Interpolation Perplexity: 17.468689525258313
===== Dev Data =====
Interpolation Perplexity: 1.8781698503022324
```

λ1 = 0.05, λ2 = 0.3, λ3 = 0.65
```
===== Train Data =====
Interpolation Perplexity: 17.326980404713794
===== Dev Data =====
Interpolation Perplexity: 1.8138185749204037
```

**2. Putting it all together, report perplexity on the test set, using the hyperparameters that you chose from the development set. Specify those hyperparameters.**

λ1 = 0.1, λ2 = 0.3, λ3 = 0.6
```
===== Test Data =====
Interpolation Perplexity: 1.874223030707083
```

λ1 = 0.2, λ2 = 0.3, λ3 = 0.5
```
===== Test Data =====
Interpolation Perplexity: 2.0308751320436174
```

λ1 = 0.1, λ2 = 0.2, λ3 = 0.7
```
===== Test Data =====
Interpolation Perplexity: 1.8634346454479223
```

λ1 = 0.05, λ2 = 0.3, λ3 = 0.65
```
===== Test Data =====
Interpolation Perplexity: 1.8004882624501728
```

**3. If you use half of the training data, would it increase or decrease the perplexity on previously unseen data? Why? Provide empirical experimental evidence if necessary.**

It should decrease the perplexity. The reason being is if there is less training data, there would likely be more words that appear less than 3 times, since there's less data for it to have a chance to appear in. Thus, there would be more <unk> tokens, and if there are more <unk> tokens, that means there would be a smaller amount of types, since all of the tokens that appear less than 3 (which would be a greater proportion with less data) all fall unders <unk>. Thus there would be a decrease in perplexity.

**4.If you convert all tokens that appeared less then 5 times to <unk> (a special symbol for out-of-vocabulary tokens), would it increase or decrease the perplexity on the previously unseen data compared to an approach that converts only a fraction of words that appeared just once to <unk>? Why? Provide empirical experimental evidence if necessary.**

It should result in an decrease in perplexity. The reason being that if a token needs to appear more times for it to not be converted into <unk>, there will be more <unk> tokens, and as per the explanation in number 3 would result in a decrease in perplexity.