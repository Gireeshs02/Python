def reverse_string(s):
  """Reverses a string.

  Args:
    s: A string.

  Returns:
    A string containing the reversed characters of s.
  """
  reversed = ""
  for i in range(len(s) - 1, -1, -1):
    reversed += s[i]
  return reversed


def main():
  """Reverses the string 'Hello, world!' and prints it to the console."""

  input_string = "Hello, world!"
  reversed_string = reverse_string(input_string)
  print(f"Reversed string: {reversed_string}")


if __name__ == "__main__":
  main()

"""Output:
Reversed string: !dlrow ,olleH"""