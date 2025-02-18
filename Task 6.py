# 39. Sudoku Validator
def is_valid_sudoku(board):
    # Check rows and columns
    for i in range(9):
        row = set()
        col = set()
        for j in range(9):
            # Check row
            if board[i][j] != '.' and board[i][j] in row:
                return False
            row.add(board[i][j])

            # Check column
            if board[j][i] != '.' and board[j][i] in col:
                return False
            col.add(board[j][i])

    # Check 3x3 subgrids
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            box = set()
            for x in range(3):
                for y in range(3):
                    val = board[i + x][j + y]
                    if val != '.' and val in box:
                        return False
                    box.add(val)

    return True

# Example Usage
sudoku_board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

print(is_valid_sudoku(sudoku_board))

# 40. Word Frequency in Text
from collections import Counter
import string

def word_frequency(text):
    # Remove punctuation and convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    words = text.split()
    return dict(Counter(words))

# Example Usage
sample_text = "Hello world! Hello Python. Python is amazing."
print(word_frequency(sample_text))

#41. Knapsack Problem (0/1)
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0]*(capacity+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, capacity+1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]

# Example Usage
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
print(knapsack(weights, values, capacity))

# 42. Merge Intervals
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []

    for interval in intervals:
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

# Example Usage
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))

# 43. Find the Median of Two Sorted Arrays
def find_median_sorted_arrays(nums1, nums2):
    nums = sorted(nums1 + nums2)
    n = len(nums)
    mid = n // 2
    return (nums[mid] + nums[mid - 1]) / 2 if n % 2 == 0 else nums[mid]

# Example Usage
arr1 = [1, 3]
arr2 = [2, 4]
print(find_median_sorted_arrays(arr1, arr2))

# 44. Maximium Rectangle in Binary Matrix
def maximal_rectangle(matrix):
    if not matrix:
        return 0

    def largest_rectangle_histogram(heights):
        stack = [-1]
        max_area = 0
        for i, h in enumerate(heights + [0]):
            while heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area

    max_area = 0
    dp = [0] * len(matrix[0])
    for row in matrix:
        for i in range(len(row)):
            dp[i] = dp[i] + 1 if row[i] == "1" else 0
        max_area = max(max_area, largest_rectangle_histogram(dp))
    return max_area

# Example Usage
binary_matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]
print(maximal_rectangle(binary_matrix))

# 45. Largest Sum Contiguous Subarray (Kadane's Algorithm)
def max_subarray_sum(arr):
    max_current = max_global = arr[0]

    for num in arr[1:]:
        max_current = max(num, max_current + num)
        max_global = max(max_global, max_current)

    return max_global

# Example Usage
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(arr))

# 46. Word Ladder Problem
from collections import deque

def word_ladder(start, end, word_list):
    word_list = set(word_list)
    queue = deque([(start, 1)])

    while queue:
        word, length = queue.popleft()
        if word == end:
            return length

        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i+1:]
                if new_word in word_list:
                    word_list.remove(new_word)
                    queue.append((new_word, length + 1))

    return 0

# Example Usage
start_word = "hit"
end_word = "cog"
dictionary = ["hot", "dot", "dog", "lot", "log", "cog"]
print(word_ladder(start_word, end_word, dictionary))

