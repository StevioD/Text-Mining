# Pattern Assignment

In this assignment, we'll practice building a function that processes
text data. Our goal is to have a function where you can pass in 
the text, clean it, and calculate some basic descriptive statistics
discussed in the class. 

In the notebook I've included a function outline for you to use
and a series of `assert` statements for you to test the performance
of the function you write. 

## Goal

Build a function that takes text input, cleans the data,
and returns a _dictionary_ of some key descriptive statistics. 

The cleaning should include the following: 

* Tokenize on white space
* Drop tokens that are not entirely alphabetic 
* Case fold to lowercase
* Remove stopwords

### Input

* A text string

### Output

* Dictionary of key statistics: 
  * Number of tokens
  * Number of unique tokens
  * Average token length
  * lexical diversity
  * The 10 most common tokens as a Counter object 
  
## Optional Work

There are some things you could add that would make this
more functional. Not required, but if you'd like to try, you
could add the following as inputs to the function : 

* A flag indicating whether or not stopwords are to be removed
* A flag indicating whether or not to case fold
* A flag indicating whether or not to drop tokens with punctuation
* Allowing input of a long text string _or_ a list of tokens and 
handling each case correctly. 





