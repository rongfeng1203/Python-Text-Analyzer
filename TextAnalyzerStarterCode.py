"""
Author: [Your Name]
Date: [Current Date]
Sources: [Any sources you use]
"""

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
  
  # Example of how to call the load_words function
  word_list = load_words("words.txt")
  
  # --- YOUR MENU-DRIVEN APPLICATION CODE WILL GO HERE ---
  
if __name__ == "__main__":
  main()
