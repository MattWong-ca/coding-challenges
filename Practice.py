# PYTHON SYNTAX PRACTICE - CODE YOUR ANSWERS BELOW
# ================================================

# Question 1: Count character frequencies without KeyError
# Write code that counts how many times each character appears in "hello world"
# Use the Python construct that avoids KeyError when incrementing counts
from collections import defaultdict
def count_characters(text: str):
    freq = defaultdict(int)
    clean_text = ''.join(filter(str.isalpha, text))    
    print(clean_text)
    for s in clean_text:
        freq[s] += 1
    return freq

# Question 2: Iterate with both index and value
# Write code that prints each element with its index
# For nums = [10, 20, 30], output should be:
# Index 0: 10
# Index 1: 20  
# Index 2: 30

def print_with_index(nums: list[int]):
    for i, value in enumerate(nums):
        print(f"Index {i}: {value}")

# Question 3: Join words into a string
# Write code that joins ['hello', 'world', 'python'] into "hello world python"

def join_words(words):
    return ' '.join(words)

# Question 4: Demonstrate sorted() vs .sort()
# Write code that shows the difference between these two approaches
# Show what happens to the original list in each case

def demonstrate_sorting(nums):
    print(f"Original list: {nums}")
    
    # Method 1: sorted() - creates NEW list, original unchanged
    sorted_list = sorted(nums)
    print(f"After sorted(): original={nums}, new_list={sorted_list}")
    
    # Method 2: .sort() - modifies original in-place, returns None
    nums_copy = nums.copy()  # Make a copy to show .sort() effect
    result = nums_copy.sort()
    print(f"nums: {nums}")
    print(f"After .sort(): modified_list={nums_copy}, return_value={result}")
    
    return sorted_list
    

# Question 5: Range() function examples
# Write code that demonstrates:
# a) Iterating from 0 to 4 (inclusive)
# b) Iterating backwards from 4 down to 0

def demonstrate_range():
    print("Forward iteration (0 to 4 inclusive):")
    for i in range(5):  # 0, 1, 2, 3, 4
        print(i)
    
    print("\nBackward iteration (4 down to 0):")
    for i in range(4, -1, -1):  # 4, 3, 2, 1, 0
        print(i)

# Test your functions:
if __name__ == "__main__":
    # Test Question 1
    print("Question 1 - Character counting:")
    print(count_characters("hello world"))
    
    # Test Question 2
    print("\nQuestion 2 - Index and value:")
    print_with_index([10, 20, 30])
    
    # Test Question 3
    print("\nQuestion 3 - Joining words:")
    print(join_words(['hello', 'world', 'python']))
    
    # Test Question 4
    print("\nQuestion 4 - Sorting demonstration:")
    print(demonstrate_sorting([89,29,27,1,5]))
    
    # Test Question 5
    print("\nQuestion 5 - Range examples:")
    demonstrate_range()
