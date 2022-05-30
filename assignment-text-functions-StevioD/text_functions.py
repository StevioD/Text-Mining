import nltk
import re
import numpy as np 

from nltk.corpus import stopwords
from nltk import FreqDist
from collections import Counter

sw = stopwords.words('english')

#################################################################
##          Cleaning Code                                      ##
#################################################################

def clean_tokenize(text, remove_sw = True, lowercase=True, remove_non_alpha=True) :
    """Cleans and tokenizes text
    
    A utility function for cleaning and tokenizing text coming in 
    as either a list or a big string. Text is split on whitespace.
    
    Args: 
        text: a collection of text, either a list or a string. If 
              list input is detected the list is first joined.
        remove_sw: True/False should stopwords be removed.
        lowercase: True/False should tokens be folded to lowercase.
        remove_non_alpha: True/False should tokens that are false
              for is.alpha be removed? 
              
    Returns : 
        A list of tokens with appropriate operations completed. 
  
    """
    
    # your code here
    
    return(text)
    

#################################################################
##          Patterns Code                                      ##
#################################################################
    
    
def get_patterns(text,num_words=10)  :
    """Computes basic statistics on a text corpus. 
    
       This function takes text as an input and returns a dictionary of statistics,
       after cleaning the text. 
       
       Args: 
           text: a list of tokens. Calls `clean_tokenize` on the text.
           num_words: Number of words to include in the FreqDist object
           in the results. Defaults to 10. 
           
       Returns: 
           A dictionary with the following keys: 
           * tokens
           * unique_tokens
           * avg_token_length
           * lexical_diversity
           * top_words: The value is a result of a call to 
             FreqDist(text).most_common(num_words)
        
    """
    
    if(len(text)==0) :
        raise ValueError("Can't work with empty text object.")
    else :
        text = clean_tokenize(text)
        
        
    
    # your code here
    
    return(results)
    
#################################################################
##          Code for Comparing Groups                          ##
#################################################################
    
    
        
def compare_texts(text_1, text_2, num_words = 10, ratio_cutoff=5) :
    """Compares two bodies of text
    
       This function returns a nested dictionary with information comparing two groups of
       text. 
       
       Args: 
           * text_1, text_2: two bodies of text, either in a string or a list. 
           * num_words: number of words to return in our get_patterns call and our 
             usage ratio. Defaults to 10. 
           * ratio_cutoff: Only words that have at least ratio_cutoff usages in each data set
             will have their usage ratio calculated. Typically we'll set ratio_cutoff 
             to something relatively small, like 5.
      
       Returns: 
           A nested dictionary with four keys: "one", "two", "one_vs_two" and "two_vs_one". 
           The keys for "one" and "two" will just be get_patterns called on text_1 and text_2 respectively. 
           For "one_vs_two", the value will be a dictionary. The key of this sub-dictionary will be 
           a word and the value will be an index. If p_1 is the fraction of words in corpus one 
           made up of this word and p_2 is the fraction in corpus two, then the index will be p_1/p_2. 
           For instance, if "dog" was used 5 times in a 1000 word corpus and 2 times in a 10000 
           word corpus, the dictionary entry would be this: 
                   results["one_vs_two"]["dog"] = (5/1000)/(2/10000). 
           Only return num_words words for each corpus, where those words have the highest 
           ratio in the data set. Only words that have at least ratio_cutoff 
           usages in each data set will be returned. 
           
    """
    
    # your code here
    

    return(results)
    
    
#################################################################
##          Code for Spell Checking                            ##
#################################################################

# I'm not going to do a full docstring or anything here, but you should
# just use Norvig's code. I've helped you out a smidge with the 
# first part. 

def words(text): 
    return(re.findall(r'\w+', text.lower()))

try : 
    WORDS = Counter(words(open('big.txt').read()))
except : 
    raise OSError("File `big.txt` not found in same folder as functions file.")


    
# your code here
    
def correction(word) :
    
    # needs completion!
    return(word)