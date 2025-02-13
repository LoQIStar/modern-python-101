"""
Python 101: Coding Challenges
============================

This file contains HackerRank-style coding challenges to help you master Python programming concepts.
"""

def find_longest_sequence(arr: list[int], target: int) -> list[int]:
    """
    Problem 1: Array Manipulation
    ---------------------------
    Given an array of integers, find the longest sequence of consecutive numbers that sum up to a target value.
    
    Example:
    Input: arr = [1, 2, 3, 4, 5], target = 9
    Output: [4, 5]  # longest sequence that sums to 9
    """
    n = len(arr)
    max_length = 0
    result = []
    
    # Try all possible sequences
    for start in range(n):
        current_sum = 0
        for end in range(start, n):
            current_sum += arr[end]
            if current_sum == target:
                if end - start + 1 > max_length:
                    max_length = end - start + 1
                    result = arr[start:end + 1]
            elif current_sum > target:
                break
                
    return result

def find_tree_height(tree: dict) -> int:
    """
    Problem 2: Tree Height Calculator
    ------------------------------
    Given a tree represented as a dictionary where each key is a node and its value is a list of children,
    calculate the height of the tree.
    
    Example:
    tree = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': [],
        'D': [],
        'E': ['F'],
        'F': []
    }
    Output: 3 (A -> B -> E -> F)
    """
    def dfs(node: str) -> int:
        if not tree[node]:  # leaf node
            return 0
        return 1 + max(dfs(child) for child in tree[node])
    
    return dfs(list(tree.keys())[0]) if tree else 0

def decode_message(matrix: list[list[str]]) -> str:
    """
    Problem 3: Matrix Message Decoder
    -----------------------------
    Given a matrix of characters, decode the hidden message by reading the characters in a spiral pattern,
    starting from the top-left corner and moving clockwise.
    
    Example:
    matrix = [
        ['H', 'E', 'L'],
        ['O', 'L', 'L'],
        ['W', 'O', '!']
    ]
    Output: "HELLO WORLD!"
    """
    if not matrix or not matrix[0]:
        return ""
        
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Move right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        
        # Move down
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        if top <= bottom:
            # Move left
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
            
        if left <= right:
            # Move up
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
            
    return ''.join(result)

# Test cases
if __name__ == "__main__":
    # Test Problem 1
    test_cases_1 = [
        ([1, 2, 3, 4, 5], 9),
        ([1, 1, 1, 1, 1], 3),
        ([2, 4, 6, 8], 10)
    ]
    
    print("Problem 1: Array Manipulation")
    print("----------------------------")
    for arr, target in test_cases_1:
        result = find_longest_sequence(arr, target)
        print(f"Array: {arr}")
        print(f"Target: {target}")
        print(f"Longest sequence: {result}\n")
    
    # Test Problem 2
    test_tree = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': [],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    print("\nProblem 2: Tree Height Calculator")
    print("-------------------------------")
    print(f"Tree height: {find_tree_height(test_tree)}\n")
    
    # Test Problem 3
    test_matrix = [
        ['H', 'E', 'L'],
        ['O', 'L', 'L'],
        ['W', 'O', '!']
    ]
    
    print("\nProblem 3: Matrix Message Decoder")
    print("------------------------------")
    print(f"Decoded message: {decode_message(test_matrix)}") 