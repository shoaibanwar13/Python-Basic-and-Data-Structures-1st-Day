 

# Function to sort a list of numbers in ascending order without using sorted()
def bubble_sort(nums):
    """
    Sorts a list of numbers in ascending order using the bubble sort algorithm.
    
    Parameters:
    nums (list): List of numbers to be sorted.
    
    Returns:
    list: Sorted list of numbers in ascending order.
    """
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

# Test case for bubble_sort
print("Bubble Sort Test:")
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))  # Expected: [11, 12, 22, 25, 34, 64, 90]

# Implementing the CustomStack class
class CustomStack:
    """
    A class to represent a stack with basic operations: push, pop, is_empty, and peek.
    """
    def __init__(self):
        self.stack = []

    def push(self, item):
        """
        Pushes an item onto the stack.
        
        Parameters:
        item: The item to be pushed onto the stack.
        """
        self.stack.append(item)

    def pop(self):
        """
        Removes and returns the top item from the stack. Returns None if the stack is empty.
        
        Returns:
        item: The top item from the stack.
        """
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        """
        Checks if the stack is empty.
        
        Returns:
        bool: True if the stack is empty, False otherwise.
        """
        return len(self.stack) == 0

    def peek(self):
        """
        Returns the top item from the stack without removing it. Returns None if the stack is empty.
        
        Returns:
        item: The top item from the stack.
        """
        if not self.is_empty():
            return self.stack[-1]
        return None

# Test cases for CustomStack
print("\nCustomStack Test:")
stack = CustomStack()
print(stack.is_empty())  # Expected: True
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())  # Expected: 3
print(stack.pop())   # Expected: 3
print(stack.pop())   # Expected: 2
print(stack.is_empty())  # Expected: False
print(stack.pop())   # Expected: 1
print(stack.is_empty())  # Expected: True

# Function to count frequency of characters in a string
def char_frequency(s):
    """
    Counts the frequency of each character in a string.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    dict: A dictionary with characters as keys and their frequencies as values.
    """
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

# Test case for char_frequency
print("\nCharacter Frequency Test:")
print(char_frequency("shoaib anwar"))  # Expected: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
