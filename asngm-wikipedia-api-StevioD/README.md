# Wikipedia Assignment

In the Wikipedia exercise, you explored how to pull all the people off Wikipedia born within a given year. 
This assignment extends that, to generate a data set with Wikipedia people who were born in a wide range of years. 

Last year we had an interesting discussion about Wikipedia fame, based on an analysis from Stephens-Davidowitz's book, 
_Everybody Lies_. The question we asked was this: are younger people more likely to be "Wikipedia Famous" 
(i.e., *on* Wikipedia)? Why might this be true? Why might it be false? 

In order to answer this question, it'd be good to have a list of everyone on Wikipedia born in the last 150 years. 

Here are the steps your code will need to follow: 

1. Set up a container to hold the names by year. Make this a dictionary where the values are lists of names.
1. Iterate through 150 years, ending in 2015. 
1. Pull every name from Wikipedia for people born in that year. Follow the model of the 
code in the exercise. 
1. Write out your results to a text file. The text file should have two columns: "birth_year" and "name". 
1. Optional: Include a third column, occupation, to capture names like "John Chandler (Data Scientist)" where
there is an occupation-based disambiguation. 

Q: Which year had the most people and how many people did it have?  
A: 

**Note**: I have `cmlimit` set to 10 so you can test your code. It can be set as high as 500, 
as the [documentation](https://www.mediawiki.org/wiki/API:Categorymembers) 
mentions. You should probably crank it up when you go for your "final" pull. 
