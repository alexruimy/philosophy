# Philosopedia
Wikipedia -> Philosophy finder

  This script will follow the first non italic, non parenthesis link in an arbitrary Wikipedia article until it gets to Philosophy.
  
  As it traverses Wikipedia, tab-separated wordpairs of `{page} {first valid link}` are stored in a cache to reduce the requests made.

## Checking a single article
  Run `philosophy.py`. Add an optional argument for the page of your choice, or `random` for a random article.
  
  **Sample output:**
  
  `python philosophy.py random`
  
    -Special:Random
    
    --Birkbeck, University of London
    
    ---Public university

    ----University

    -----Educational institution
    
    ------Education
    
    -------Learning
    
    --------Knowledge
    
    ---------Awareness
    
    ----------Quality (philosophy)
    
    -----------Philosophy
    
    Samuel_Guttenplan -> Philosophy in 11 clicks (6 requests)`
    
    
## Path length distribution across *n* attempts
  Run `path_lengths.py` with optional arguments `quiet` (to only output the final result for each article) or `n` (number of articles to check)
