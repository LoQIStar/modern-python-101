# Algorithmic Coding Preparation Cheatsheet

## Data Structures to Master

### 1. Arrays and Strings

Arrays and strings are fundamental data structures that store elements sequentially in memory.

#### Array Example (Python)
```python
# Basic array operations
numbers = [1, 2, 3, 4, 5]
numbers.append(6)      # Add element: O(1)
numbers.pop()         # Remove last element: O(1)
numbers.insert(0, 0)  # Insert at index: O(n)
numbers.remove(3)     # Remove element: O(n)

# Array slicing
subarray = numbers[1:4]  # Get elements from index 1 to 3
```

#### String Example
```python
# String operations
text = "Hello, World!"
length = len(text)           # String length
substring = text[0:5]        # String slicing: "Hello"
reversed_text = text[::-1]   # Reverse string
split_words = text.split(',')  # Split into array: ["Hello", " World!"]
```

### 2. Linked Lists

A linked list is a sequence of elements where each element points to the next element.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Create a linked list: 1 -> 2 -> 3
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

# Traverse linked list
def traverse(head):
    current = head
    while current:
        print(current.val)
        current = current.next
```

### 3. Stacks and Queues

#### Stack (LIFO - Last In First Out)
```python
# Using list as a stack
stack = []
stack.append(1)    # Push
stack.append(2)
stack.append(3)
top = stack.pop()  # Pop (returns 3)

# Stack implementation using class
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
```

#### Queue (FIFO - First In First Out)
```python
from collections import deque

# Using deque as a queue
queue = deque()
queue.append(1)         # Enqueue
queue.append(2)
first = queue.popleft() # Dequeue (returns 1)
```

### 4. Trees

#### Binary Tree
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Create a binary tree:
#       1
#      / \
#     2   3
#    / \
#   4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
```

#### Binary Search Tree (BST)
```python
class BST:
    def insert(self, root, val):
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
        return root
    
    def search(self, root, val):
        if not root or root.val == val:
            return root
        if val < root.val:
            return self.search(root.left, val)
        return self.search(root.right, val)
```

### 5. Graphs

```python
# Adjacency List representation
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Adjacency Matrix representation
matrix = [
    [0, 1, 1, 0, 0, 0],  # A
    [1, 0, 0, 1, 1, 0],  # B
    [1, 0, 0, 0, 0, 1],  # C
    [0, 1, 0, 0, 0, 0],  # D
    [0, 1, 0, 0, 0, 1],  # E
    [0, 0, 1, 0, 1, 0]   # F
]
```

### 6. Hash Tables

```python
# Python dictionary as hash table
hash_table = {}
hash_table['key1'] = 'value1'
hash_table['key2'] = 'value2'

# Custom HashTable implementation
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append([key, value])
```

## Algorithm Techniques

### 1. Two-pointer Approach

```python
# Example: Find pair with target sum in sorted array
def find_pair(arr, target):
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []
```

### 2. Sliding Window

```python
# Example: Find maximum sum subarray of size k
def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return None
    
    # Compute sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide window and update max_sum
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

### 3. Depth-First Search (DFS)

```python
# DFS for Graph
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=' ')
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# DFS for Binary Tree
def dfs_tree(root):
    if not root:
        return
    
    print(root.val, end=' ')  # Pre-order
    dfs_tree(root.left)
    dfs_tree(root.right)
```

### 4. Breadth-First Search (BFS)

```python
from collections import deque

# BFS for Graph
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# BFS for Binary Tree
def bfs_tree(root):
    if not root:
        return
    
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val, end=' ')
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

### 5. Dynamic Programming

```python
# Example: Fibonacci using DP
def fibonacci_dp(n):
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

# Example: 0/1 Knapsack
def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(
                    values[i-1] + dp[i-1][w-weights[i-1]],
                    dp[i-1][w]
                )
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]
```

### 6. Greedy Algorithms

```python
# Example: Activity Selection
def activity_selection(start, finish):
    n = len(start)
    activities = sorted(zip(finish, start))
    
    selected = [activities[0]]
    last_finish = activities[0][0]
    
    for i in range(1, n):
        if activities[i][1] >= last_finish:
            selected.append(activities[i])
            last_finish = activities[i][0]
    
    return selected
```

### 7. Divide and Conquer

```python
# Example: Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

## Time Complexity Reference

### Common Data Structure Operations
- Array: Access O(1), Search O(n), Insert/Delete O(n)
- Linked List: Access O(n), Search O(n), Insert/Delete O(1)
- Hash Table: Access/Insert/Delete O(1) average, O(n) worst
- Binary Search Tree: Access/Search/Insert/Delete O(log n) average, O(n) worst

### Common Sorting Algorithms
- Bubble Sort: O(n²)
- Selection Sort: O(n²)
- Insertion Sort: O(n²)
- Merge Sort: O(n log n)
- Quick Sort: O(n log n) average, O(n²) worst
- Heap Sort: O(n log n)

### Graph Algorithms
- BFS/DFS: O(V + E)
- Dijkstra's: O((V + E) log V)
- Floyd-Warshall: O(V³)
- Kruskal's: O(E log E)
- Prim's: O(E log V) 