# Assignment: Comparing Groups

This repo starts you with no code! Egads. When you're in the Jupyter Notebook
browser, there's a menu
on the right where you create a new Python 3 notebook, so that's a good place to start.

In this assignment, I'd like you to write a function, similar to the "Patterns in Text" one, 
where we built a function that calculated descriptive statistics on a single corpus. 

This function will compare two groups of corpora. Expect text to come in as a long
string, as we did with the patterns assignment. Text should be tokenized on whitespace
and normalized by removing punctuation, folding to lower case, and removing stopwords. 

Once you've written your function, run it twice with the output printing to the 
screen so that I can verify correctness. The first time run it comparing the 
Republican National Convention corpus (in spot 1) to the Democratic National Convention
(in spot 2). The second time compare either one of the national conventions to the 
text `big.txt` we used for spell checking. 

Set `num_words = 10` when you call the function on the two conventions. When you compare
one convention to the `big.txt`, set `num_words = 5`. In both cases, set `ratio_cutoff` to 
5. 

**Input**
* A corpus called `corpus_1`.
* A corpus called `corpus_2`. 
* An argument called `num_words`.
* An argument called `ratio_cutoff`.

**Output**

This function should output a dictionary. The first set of keys will be these four 
strings: "one", "two", "one_vs_two" and "two_vs_one". The keys for "one" and "two" 
will just be summary statistics on `corpus_1` and `corpus_2` respectively. I'll explain
the other two keys down below.

For keys "one" and "two", the second layer of keys will be the following strings 
with associated values: 
* `tokens`: the number of tokens in the corpus.
* `unique_tokens`: the unique tokens in the corpus. 
* `avg_token_length`: the average token length in the corpus.
* `lexical_diversity`: the lexical diversity in the corpus.
* `top_words`: the top `num_words` in the data set.

For "one_vs_two", have the value be a dictionary. The key of this sub-dictionary
will be a word and the value will be an index. If p_1 is the fraction of words
in corpus one made up of this word and p_2 is the fraction in corpus two, then 
the index will be p_1/p_2. For instance, if "dog" was used 5 times in a 1000 word
corpus and 2 times in a 10000 word corpus, the dictionary entry would be this:
`results["one_vs_two"]["dog"] = (5/1000)/(2/10000)`. Only return `num_words`
words for each corpus, where those words have the highest ratio in the data set. Only 
words that have at least `ratio_cutoff` usages in *each* data set will be returned. 
Typically we'll set `ratio_cutoff` to something relatively small, like 5. 

