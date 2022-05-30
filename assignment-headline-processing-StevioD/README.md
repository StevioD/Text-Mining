# Assignment: Headline Processing

This is an assignment that is eligible for completion against your contract goals. 

In this assignment, you'll practice reshaping a pretty messy text file. This assignment
may end up being a decent amount of work, but assignment 2 will build on this one, so
you'll be making an investment in two assignments. 

## Background

In 2015 and 2016 a journalism student at UMT started capturing headlines from six 
Montana newspapers. In this assignment we'll only work with the headlines from
the Missoulian, though you can see all of the raw materials in the Excel file 
"Headlines Base Document.xlsx". 

The student wished to analyze some of the words used by the different newspapers. But,
as you'll see when you look at the file, the data are arranged in a way that makes
the headlines hard to work with. In this assignment, you'll re-arrange the data. 

## Task

You'll start with the file `missoula.txt`, which holds a copy-and-paste from the 
"Missoulian" sheet in the Excel file. Your goal is to create a file that looks 
like the file `missoula_clean.txt`. 

**Input**: The input file is arranged as a ragged table. The first row holds 
dates in a DD-MMM format. Note that dates before 01-Jan are from 2015; dates 
after 01-Jan are from 2016. The rows below a date hold the headlines from that date
and you'll notice a varying number of headlines. 

**Output**: The output file is arranged as a [tidy data set](https://cran.r-project.org/web/packages/tidyr/vignettes/tidy-data.html), 
with one headline on each row. There are three columns: the newspaper, the date, and the headline. 

Things to think about: 

1. You'll need to transform dates in this DD-MMM format into a traditional YYYY-MM-DD, 
the [one true date format](https://xkcd.com/1179/). 
1. There's no way to read a file "vertically" in Python, so you'll need to be smart
about associating a headline with its date. 

