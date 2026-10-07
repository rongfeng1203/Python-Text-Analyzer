"""
Author: [Rina Feng]
Date: [Oct 1st, 2026]
Sources: [https://chatgpt.com/share/6ac3f542-fb44-83e9-9831-e42c5c667fbf]

Peer testing:
Tester and date: Teske, Oct 7th, 2026
Inputs tried and results: 
Mixed-case palindromes and anagrams, passed
loaded words.txt, filtered to length 5, found palindromes and anagrams, passed
Empty strings, single-character palindromes, repeated letters, unequal lengths, and same-word exclusion, passed
Feedback: None
Changes made in response: None
"""


def is_palindrome(s):
  """
  Returns a boolean value corresponding to whether the String s is a palindrome or not.
  Compares strings case-insensitively.

  Args:
    s: String to be tested

  Returns:
    boolean
  """
  s = s.lower()
  # Compare the word with its reverse.
  return s == s[::-1]

  # Old logic:
    # for i in range(len(s) // 2): #cut half the string, and 
    #     if s[i] != s[-(i + 1)]:#check if the first and last character are the same, then second and second last character, etc.
    #         return False # if it immediately finds a character that is not the same, it will return false. Wait till the end to confirm whole thing is true  

    # return True


def is_anagram(original, s):
  """
  Returns a boolean value corresponding to whether the String s is an anagram or not.
  Compares strings case-insensitively and requires a different letter order.

  Args:
    original: String that is to be compared against
    s: String to be tested as a potential anagram of original

  Returns:
    boolean
  """
  original = original.lower()
  s = s.lower()
  # Sorting compares both the letters and how many times each occurs.
  return original != s and sorted(original) == sorted(s)

  # Old logic:
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


def find_palindromes(word_list):
  """
  Finds all palindromes in a list of strings and displays them in the terminal.
  Uses the is_palindrome() helper function.

  Args:
    word_list: A list of strings
  """
  palindromes = []
  for word in word_list:
    if is_palindrome(word):
      palindromes.append(word)

  print(f"Palindromes found: {len(palindromes)}")
  print("\nHere they are:")
  for word in palindromes:
    print(word)


def find_anagrams(word_list, target):
  """
  Finds all anagrams in a list of strings and displays them in the terminal.
  Uses the is_anagram() helper function.

  Args:
    word_list: A list of strings
    target: Target string for potential anagrams to be compared with
  """
  anagrams = []
  for word in word_list:
    if is_anagram(target, word):
      anagrams.append(word)
  print(f"I found {len(anagrams)} Anagrams")
  for word in anagrams:
    print(word)


def filter_by_length(word_list, length):
  """
  Returns a new list of strings after going through each item of the original list
  to find any that are the same as the provided length.
  Does not modify the original list.

  Args:
    word_list: A list of strings
    length: The target length of the words to keep

  Returns:
    A new list of strings
  """
  filtered_words = []
  for word in word_list:
    if len(word) == length:
      filtered_words.append(word)
  return filtered_words


def load_words(file_path):

  """
  Loads words from a text file into a list.
  
  Args:
    file_path: The path to the text file.
    
  Returns:
    A list of strings, where each string is a word from the file.
    Returns an empty list if the file is missing or unreadable.
  """
  try:
    with open(file_path, 'r', encoding='utf-8') as file:
      # Use a list comprehension for a concise way to read lines and strip whitespace
      words = [line.strip() for line in file]
    print(f"\nCurrently have {len(words)} words in memory.\n")
    return words
  except FileNotFoundError:
    print(f"Error: The file at {file_path} was not found.")
    return []

  except (OSError, UnicodeError):
    print(f"Error: The file at {file_path} could not be read.")
    return []


def main():
  """
  The main function to run the word analysis application.
  """
  word_list = []

  while True:
    print("\nWord Analysis\n")
    print("1 - Load/reload words from file")
    print("2 - Update word list by word length")
    print("3 - Find palindromes")
    print("4 - Find anagrams")
    print("5 - Quit")

    choice = input("> ").strip()

    if choice == '1':
      word_list = load_words("words.txt")

    elif choice == '2':
      if not word_list:
        print('List is empty. Choose "1" to load it.')
      else:
        try:
          length = int(input("Which length words would you like to keep?\n> "))
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
        target = input("Enter the target word for anagram search: ").strip()
        find_anagrams(word_list, target)

    elif choice == '5':
      print("Thank you")
      break

    else:
      print("Invalid choice. Please try again.")


if __name__ == "__main__":
  main()
