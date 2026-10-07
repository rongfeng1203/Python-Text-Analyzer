"""
Author: [Rina Feng]
Date: [Oct 1st, 2026]
Sources: [https://chatgpt.com/share/6ac3f542-fb44-83e9-9831-e42c5c667fbf]
"""
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


def load_words(file_path):

  """
  Loads words from a text file into a list.
  
  Args:
    file_path: The path to the text file.
    
  Returns:
    A list of strings, where each string is a word from the file.
    Returns an empty list if the file cannot be found.
  """
  try:
    with open(file_path, 'r') as file:
      # Use a list comprehension for a concise way to read lines and strip whitespace
      words = [line.strip() for line in file]
    print(f"\nCurrently have {len(words)} words in memory.\n")
    return words
  except FileNotFoundError:
    print(f"Error: The file at {file_path} was not found.")
    return []


def main():
  """
  The main function to run the word analysis application.
  """
  word_list = []

  while True:
    print("Menu:")
    print("1. Load words from file")
    print("2. Filter by length")
    print("3. Find palindromes")
    print("4. Find anagrams")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
      word_list = load_words("words.txt")

    elif choice == '2':
      if not word_list:
        print('List is empty. Choose "1" to load it.')
      else:
        try:
          length = int(input("> "))
        except ValueError:
          print("Please enter a positive whole number.")
          continue
        if length <= 0:
          print("Please enter a positive whole number.")
          continue

        filtered_words = filter_by_length(word_list, length)
        word_list = filtered_words
        print(f"Found {len(filtered_words)} words of length {length}.")
        for word in filtered_words:
          print(word)

    elif choice == '3':
      if not word_list:
        print('List is empty. Choose "1" to load it.')
      else:
        find_palindromes(word_list)

    elif choice == '4':
      if not word_list:
        print('List is empty. Choose "1" to load it.')
      else:
        target = input("Enter the target word for anagram search: ")
        find_anagrams(word_list, target)

    elif choice == '5':
      print("Exiting the program.")
      break

    else:
      print("Invalid choice. Please try again.")


if __name__ == "__main__":
  main()
