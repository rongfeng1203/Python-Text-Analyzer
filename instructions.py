# Tasks (complete all in the same .py file):

# 1. Create the function:

def is_palindrome(s):
   #logic, if the string is same as the reverse, first and last character, then second and second last character, etc.
  return s == s[::-1]
  #simplified logic, when the string is reversed, if it is the same as the original, then it is a palindrome. If not, then it is not a palindrome.

    # for i in range(len(s) // 2): #cut half the string, and 
    #     if s[i] != s[-(i + 1)]:#check if the first and last character are the same, then second and second last character, etc.
    #         return False # if it immediately finds a character that is not the same, it will return false. Wait till the end to confirm whole thing is true  

    # return True
# """
#   Returns a boolean value corresponding to whether the String s is a palindrome or not.
  
#   Args:
#     s: String to be tested
  
#   Returns:
#     boolean
#   """

# 2. Create the function:
def is_anagram(original, s):
  return sorted(original) == sorted(s)
   #simplified logic, if sorted original and sorted s are the same, then they are anagrams.

  # #logic, if the words are the same length, and if the letters in the words are the same, then they are anagrams
  # if len(original) != len(s):
  #   return False
  
  # remaining_letters = list(s) #makes a list of words, so that it can be checked off as the letters are found in the original word. If a letter is not found, then it is not an anagram.

  # for letter in original: 
  #   if letter in remaining_letters:
  #     remaining_letters.remove(letter)
  #   else:
  #     return False

  # return True
  #orrrrr
  
# """
#   Returns a boolean value corresponding to whether the String s is an anagram or not.
  
#   Args:
#     original: String that is to be compared against
#     s: String to be tested as a potential anagram of original
  
#   Returns:
#     boolean
# """

# 3. Create the function:
def find_palindromes(word_list):
  #for loop scanning every single word in the list
  palindromes = []
  for word in word_list:
    if is_palindrome(word):
      palindromes.append(word)#add to list 

  print(f"Palindromes found: {len(palindromes)}")
  print("\nHere they are:")
  for word in palindromes:
    print(word)
  # """
  # Finds all palindromes in a list of strings and displays them in the terminal. 
  # Uses the is_palindrome() helper function.
  
  # Args:
  #   word_list: A list of strings
  # """

# 4. Create the function:
def find_anagrams(word_list, target):
  anagrams = []
  for word in word_list:
    if word != target and is_anagram(target, word): #make sure the word itself is not included in the list of anagrams, and then check if it is an anagram
      anagrams.append(word)
  print(f"I found {len(anagrams)} Anagrams")
  for word in anagrams:
    print(word)
  # """
  # Finds all anagrams in a list of strings and displays them in the terminal. 
  # Uses the is_anagram() helper function.
  
  # Args:
  #   word_list: A list of strings
  #   target: Target string for potential anagrams to be compared with
  # """


# 5. Create the function:
def filter_by_length(word_list, length):
  filtered_words = []
  for word in word_list:
    if len(word) == length:
      filtered_words.append(word)
  return filtered_words

  # """
  # Returns a new list of strings after going through each item of the original list 
  # to find any that are the same as the provided length.
  
  # Args:
  #   word_list: A list of strings
  #   length: The target length of the words to keep
  
  # Returns:
  #   A new list of strings
  # """


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
