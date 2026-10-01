# Tasks (complete all in the same .py file):

# 1. Create the function:
def is_palindrome(s):
  """
  Returns a boolean value corresponding to whether the String s is a palindrome or not.
  
  Args:
    s: String to be tested
  
  Returns:
    boolean
  """
  pass

# 2. Create the function:
def is_anagram(original, s):
  """
  Returns a boolean value corresponding to whether the String s is an anagram or not.
  
  Args:
    original: String that is to be compared against
    s: String to be tested as a potential anagram of original
  
  Returns:
    boolean
  """
  pass

# 3. Create the function:
def find_palindromes(word_list):
  """
  Finds all palindromes in a list of strings and displays them in the terminal. 
  Uses the is_palindrome() helper function.
  
  Args:
    word_list: A list of strings
  """
  pass

# 4. Create the function:
def find_anagrams(word_list, target):
  """
  Finds all anagrams in a list of strings and displays them in the terminal. 
  Uses the is_anagram() helper function.
  
  Args:
    word_list: A list of strings
    target: Target string for potential anagrams to be compared with
  """
  pass

# 5. Create the function:
def filter_by_length(word_list, length):
  """
  Returns a new list of strings after going through each item of the original list 
  to find any that are the same as the provided length.
  
  Args:
    word_list: A list of strings
    length: The target length of the words to keep
  
  Returns:
    A new list of strings
  """
  pass

# 6. Download the file words.txt, and place in your project folder.
#    With the help of the starter code provided, create a small menu-driven 
#    application to analyze a text file with more than 300,000 words.
#    Have a peer test your program for errors.

"""
The required functionality of your program is: 
1. Able to load/reload data from a file called "words.txt" (each word will be 
   on a separate line in the file). The data should be loaded into a list for 
   further analysis.
2. Prune the list based on the word size provided by the user.
3. Find all of the palindromes in the word list and display them.
4. Find anagrams for a given word.
5. Quit the program.
"""


# Example menu-driven interface (Note: The following sample isn't a thorough test of the program.)
"""
Word Analysis

1 - Load/reload words from file
2 - Update word list by word length
3 - Find palindromes
4 - Find anagrams
5 - Quit
> 3

List is empty. Choose "1" to load it.

Word Analysis

1 - Load/reload words from file
2 - Update word list by word length
3 - Find palindromes
4 - Find anagrams
5 - Quit
> 1

Currently have 370103 words in memory.

Word Analysis

1 - Load/reload words from file
2 - Update word list by word length
3 - Find palindromes
4 - Find anagrams
5 - Quit
> 2
Prune Word List by Length
Which length words would you like to keep?
> 5

Currently have 15918 words in memory.

Word Analysis

1 - Load/reload words from file
2 - Update word list by word length
3 - Find palindromes
4 - Find anagrams
5 - Quit
> 3
Palindromes found: 41

Here they are:
addda
ajaja
...
ululu

Word Analysis

1 - Load/reload words from file
2 - Update word list by word length
3 - Find palindromes
4 - Find anagrams
5 - Quit
> 4
Type a word to find its anagrams: later
I found 7 Anagrams
alert
alter
artel
ratel
retal
taler
telar

Word Analysis

1 - Load/reload words from file
2 - Update word list by word length
3 - Find palindromes
4 - Find anagrams
5 - Quit
> 5
Thank you
"""
