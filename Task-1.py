#Code 1:

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


#Code2:.

def get_age():
    """Gets the user's age.

    Returns:
        The user's age as an integer, or None if the user's input is invalid.
    """

    age = input("Please enter your age: ")
    while not age.isnumeric() or int(age) < 18:
        print("Invalid input. You must be at least 18 years old.")
        age = input("Please enter your age: ")
    return int(age)


def main():
    """Prompts the user for their age and prints a message depending on their age."""

    age = get_age()
    if age:
        print(f"You are {age} years old and eligible.")
    else:
        print("You are not eligible.")


if __name__ == "__main__":
    main()

"""Output:
Please enter your age: 19
You are 19 years old and eligible."""



#Code3:

def read_and_write_file(filename):
    """Reads and writes a file.

    Args:
        filename: The name of the file to read and write.

    Returns:
        None.
    """

    try:
        with open(filename, "r") as file:
            content = file.read()
        with open(filename, "w") as file:
            file.write(content.upper())
        print(f"File '{filename}' processed successfully.")
    except FileNotFoundError as e:
        print(f"The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def main():
    """Reads and writes the file 'sample.txt'."""

    filename = "sample.txt"
    read_and_write_file(filename)


if __name__ == "__main__":
    main()

"""Output:
The file 'sample.txt' does not exist."""


#Code4:

def merge_sort(arr):
    """Sorts an array using the merge sort algorithm.

    Args:
        arr: A list of elements to be sorted.

    Returns:
        A sorted list of elements.
    """

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    # Merge the sorted left and right subarrays.
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Add any remaining elements from the left subarray.
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    # Add any remaining elements from the right subarray.
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr


arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print(f"The sorted array is: {arr}")


"""Output:
The sorted array is: [3, 9, 10, 27, 38, 43, 82]"""
