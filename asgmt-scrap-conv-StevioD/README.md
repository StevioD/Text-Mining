# Scraping Conventions

This assignment asks you to scrape and store the transcripts
of the RNC and DNC conventions. Each convention was four 
nights long, and rev.com has published the full transcripts.

We'll use the output of this to compare the language used
by the parties. 

Start with `Scraping Convention Transcripts.ipynb`. I've created
some code for you to fill in. Your goal is to just write out
the entire visible text of the page to its own file. Again, 
each night's transcript should go in its own file, so you'll
create eight total files. Don't include the text files in the repo. The best 
practice is not to include data in repositories. I've made this easier by 
adding `*.txt` into the `.gitignore`. 

I've added some code at the end teaching you about the `textwrap` library,
which can be useful to write out long strings in a way that makes them
easier to read by a human. 

## Important Note

Now we're headed out into the world with our Python skills. This means
that we'll be hitting servers managed by people who don't want 
their servers overwhelmed by malicious actors. One way to avoid
this is to not hit servers too hard. Request a modest number of pages
and wait between requesting pages. I've set up your code to sleep 
for a while between requests. Please keep this in and be careful 
any time you're calling "request" in a loop!
