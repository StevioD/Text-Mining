# N-Gram Assignment

In this assignment you'll build text generators using 
Unigram and Bigram models of language. The goal is to create two functions, 
`generate_unigram_text` and `generate_bigram_text`. These functions
will take in a text (such as `text1` in NLTK) and will output
a string of
a given number of tokens using a the input text as the underlying corpus. 

I've created stubs for you of both functions in the Notebook. You'll
want to make use of the `choices` function in the `random` library 
to do the weighted choice (like `sample` in R) of the unigrams or 
bigrams.

Your bigram function should allow the user to pass in a starting
word to begin building the chain of words. 
