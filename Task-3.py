def count_word_frequencies(text):
  """Counts the frequency of each word in a given text.

  Args:
    text: A string containing the text to be analyzed.

  Returns:
    A dictionary mapping each word to its frequency in the text.
  """

# Split the text into words.
  words = text.split()

# Create a dictionary to store the word frequencies.
  word_frequencies = {}

# Iterate over the words and count their frequencies.
  for word in words:
    if word in word_frequencies:
      word_frequencies[word] += 1
    else:
      word_frequencies[word] = 1

# Return the dictionary of word frequencies.
  return word_frequencies


# Example usage:

text = input()

word_frequencies = count_word_frequencies(text)

print(word_frequencies)
