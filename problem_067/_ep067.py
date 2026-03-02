# Project Euler - Problem 67: Maximum Path Sum II

# PROBLEM SUMMARY:
#   You have a triangle made of numbers, like this:
#
#            3
#           7 4
#          2 4 6
#         8 5 9 3
#
#   Starting from the very top (3), you move DOWN one step at a time.
#   Each step you can go to ONE of the two numbers directly below you.
#   Your goal: find the path that gives the HIGHEST total sum.
#
#   For the example above, the best path is:
#   3 → 7 → 4 → 9  =  23

#   Instead of solving the whole problem at once (top to bottom),
#   we BREAK IT INTO SMALLER PIECES and solve from the bottom up.
# ---------------------------------------------------------------
# STEP 1: READ THE FILE
# ---------------------------------------------------------------
#
# It opens "0067_triangle.txt" which contains 100 rows of numbers.
# Each row is a line of space-separated integers
# The 'with' keyword opens the file and automatically closes it when it's done.'r' means it opens it in READ mode

import time            # We will use time to measure how long the program takes
begin = time.time()

with open("0067_triangle.txt", "r") as file:

    # .readlines() reads the entire file and gives us a list where each item is one line of text (including "\n" at the end).
    lines = file.readlines()

# ---------------------------------------------------------------
# STEP 2: CONVERT THE TEXT INTO A LIST OF LISTS (of integers)
# ---------------------------------------------------------------
# Right now each line is a STRING like "73 41\n".
# We need to turn each line into a LIST OF INTEGERS like [73, 41].
#
# Here's how we do it line by line:
#
#   line.split()
#     → Splits the string by whitespace (spaces AND newlines).
#       "73 41\n"  becomes  ["73", "41"]
#       (The \n disappears automatically .split() handles it)
#
#   map(int, ...)
#      Applies the int() function to every item in the list.
#      ["73", "41"]  becomes  [73, 41]  (strings → integers)
#
#   list(..)
#     map() returns a "lazy" object, so we wrap it in list() to get a proper Python list we can work with.

triangle = []                              # start with an empty list

for line in lines:                         # go through each line of text
    row = list(map(int, line.split()))     # convert line → list of ints
    triangle.append(row)                   # add this row to our triangle

# ---------------------------------------------------------------
# STEP 3: THE BOTTOM-UP ALGORITHM
# ---------------------------------------------------------------
# We want to start at the SECOND-TO-LAST row and work UPWARD.
# Why second-to-last? Because the LAST row has no children below it, there's nothing to add. It stays as is.
# len(triangle) gives us the total number of rows (100).
# So the last row is at index 99, and the second-to-last is at 98.
#
# We use range() to count BACKWARDS:
#
#   range(start, stop, step)
#
#   start = len(triangle) - 2
#         = 100 - 2 = 98       (second-to-last row index)
#
#   stop  = -1
#         = Python stops BEFORE reaching this number, so the last value produced will be 0 (the top row). Using -1 as stop ensures we DO process row 0.
#
#   step  = -1
#         = Count down by 1 each time: 98, 97, 96, ..., 1, 0
#
# So range(98, -1, -1) produces: 98, 97, 96, ..., 1, 0
# triangle[row_index][col_index] gives us any specific number.
# For example: triangle[1][0] = 73, triangle[1][1] = 41

for row_index in range(len(triangle) - 2, -1, -1):

    # Now we look at every single number in the current row.
    # len(triangle[row_index]) tells us how many numbers are in this row.
    # Row 0 has 1 number, row 1 has 2, row 2 has 3, etc. So range(len(triangle[row_index])) gives: 0, 1, 2, ..., up to row length.

    for col_index in range(len(triangle[row_index])):

        # ── FINDING THE TWO CHILDREN ──────────────────────────
        # In a triangle like this:
        #   row:   ...  A  ...         ← current position: [row_index][col_index]
        #   row+1: ...  L  R  ...      ← children one row below
        #
        # The LEFT child is at the SAME column index in the row below:
        #   triangle[row_index + 1][col_index]
        #
        # The RIGHT child is one column to the RIGHT in the row below:
        #   triangle[row_index + 1][col_index + 1]
        # This works because of how triangle rows are structured: each number at position [r][c] is "above" positions [r+1][c] and [r+1][c+1] in the next row.

        left_child  = triangle[row_index + 1][col_index]
        right_child = triangle[row_index + 1][col_index + 1]

        # ── CHOOSING THE BETTER CHILD ─────────────────────────
        # max(left_child, right_child) returns whichever is larger.
        # We want to go in the direction that gives us the most points.
        # Remember: by the time we process a row, ALL rows BELOW it have already been updated.
        # So left_child and right_child don't just represent the number at that position, they represent the BEST TOTAL SCORE reachable from that position all the way down to the bottom.

        best_child = max(left_child, right_child)

        # ── UPDATING THE CURRENT POSITION ────────────────────
        # We add the best child's score to the current number.
        # This "collapses" the best future path into the current number.
        # After this update, triangle[row_index][col_index] no longer means just "the number at this cell" it now means:"the maximum sum reachable starting from this cell going down."

        triangle[row_index][col_index] += best_child


# ---------------------------------------------------------------
# STEP 4: READ THE ANSWER FROM THE TOP
# ---------------------------------------------------------------
# After the loop finishes, every cell has been updated.
# The very top of the triangle — triangle[0][0] — has absorbed the best possible path sum all the way from top to bottom.
# That single number IS our answer.

answer = triangle[0][0]

print("Maximum path sum:", answer)

end = time.time()
print(f"Finished in {end - begin} seconds.")